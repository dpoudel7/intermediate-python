import scrapy
import re
from urllib.parse import urljoin, urlparse, unquote
from collections import deque
import json
import logging

class KevinBaconSpider(scrapy.Spider):
    name = 'kevin_bacon'
    allowed_domains = ['en.wikipedia.org']
    
    # Target URL - Kevin Bacon's Wikipedia page
    target_url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
    target_title = 'Kevin Bacon'
    
    # Regexp to filter out non-article links
    article_pattern = re.compile(r'^/wiki/[^:]*$')
    
    # Skip patterns
    skip_patterns = [
        r'_\(identifier\)$',  # ISBN, ISSN, etc.
        r'^\d+$',             # Years
        r'List_of_',          # Lists
    ]
    skip_regex = re.compile('|'.join(skip_patterns))
    
    # Queue for BFS traversal
    queue = deque()
    
    # Sets to track visited and enqueued pages
    visited = set()
    enqueued = set()
    
    # Storage for paths
    paths = {}
    
    def __init__(self, start_url=None, max_depth=6, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set starting URL
        if not start_url:
            self.start_url = 'https://en.wikipedia.org/wiki/Special:Random'
        else:
            if not start_url.startswith('https://en.wikipedia.org/'):
                self.start_url = f'https://en.wikipedia.org/wiki/{start_url.replace(" ", "_")}'
            else:
                self.start_url = start_url
        
        # Set max depth
        self.max_depth = int(max_depth)
        
        # Start title placeholder
        self.start_title = None
        
        # Set start URLs
        self.start_urls = [self.start_url]
    
    def parse(self, response):
        """Initial parser for the starting page"""
        # Get page title
        title = self.get_title(response)
        self.start_title = title
        
        print(f"Starting from: {title} ({response.url})")
        
        # Check if already at Kevin Bacon
        if response.url == self.target_url:
            print("Starting page is already Kevin Bacon!")
            return {
                'path': [title],
                'degrees': 0,
                'success': True
            }
        
        # Initialize path tracking
        self.paths[response.url] = {'prev': None, 'title': title}
        self.visited.add(response.url)
        
        # Get links from first page
        links = self.extract_article_links(response)
        
        # Add links to queue
        for link in links:
            if link not in self.visited and link not in self.enqueued:
                self.queue.append((link, 1))  # (url, depth)
                self.enqueued.add(link)
                self.paths[link] = {
                    'prev': response.url, 
                    'title': self.get_title_from_url(link)
                }
        
        # Start BFS
        yield from self.bfs_crawl()
    
    def bfs_crawl(self):
        """Breadth-first search crawler"""
        while self.queue:
            url, depth = self.queue.popleft()
            
            # Check depth limit
            if depth > self.max_depth:
                continue
            
            # Check if target found
            if url == self.target_url:
                path = self.reconstruct_path(url)
                print(f"Found Kevin Bacon in {depth} steps!")
                print(f"Path: {' -> '.join(path)}")
                
                yield {
                    'path': path,
                    'degrees': depth,
                    'success': True
                }
                return
            
            # Request the page
            yield scrapy.Request(
                url=url,
                callback=self.parse_page,
                meta={'depth': depth}
            )
    
    def parse_page(self, response):
        """Parse subsequent pages"""
        depth = response.meta['depth']
        self.visited.add(response.url)
        
        # Check if target found
        if response.url == self.target_url:
            path = self.reconstruct_path(response.url)
            print(f"Found Kevin Bacon in {depth} steps!")
            print(f"Path: {' -> '.join(path)}")
            
            yield {
                'path': path,
                'degrees': depth,
                'success': True
            }
            return
        
        # Get links
        links = self.extract_article_links(response)
        
        # Add new links to queue
        for link in links:
            if link not in self.visited and link not in self.enqueued:
                self.queue.append((link, depth + 1))
                self.enqueued.add(link)
                
                if link not in self.paths:
                    title = self.get_title_from_url(link)
                    self.paths[link] = {
                        'prev': response.url, 
                        'title': title
                    }
        
        # Continue BFS
        yield from self.bfs_crawl()
    
    def extract_article_links(self, response):
        """Extract article links from the page"""
        content_div = response.css('div#mw-content-text')
        links = content_div.css('a::attr(href)').getall()
        
        article_links = []
        
        for link in links:
            if self.article_pattern.match(link) and ':' not in link and '#' not in link:
                # Skip based on patterns
                path = urlparse(link).path
                if path.startswith('/wiki/'):
                    page_name = path[6:]
                    if self.skip_regex.search(page_name):
                        continue
                
                full_url = urljoin('https://en.wikipedia.org', link)
                article_links.append(full_url)
        
        # Prioritize direct link to Kevin Bacon
        if self.target_url in article_links:
            article_links.remove(self.target_url)
            article_links.insert(0, self.target_url)
            print(f"Found direct link to Kevin Bacon on page {response.url}")
        
        return article_links
    
    def get_title(self, response):
        """Get page title"""
        title = response.css('h1#firstHeading ::text').get()
        if not title:
            title = self.get_title_from_url(response.url)
        return title
    
    def get_title_from_url(self, url):
        """Extract title from URL"""
        path = urlparse(url).path
        if path.startswith('/wiki/'):
            try:
                title = unquote(path[6:].replace('_', ' '))
                return title
            except:
                pass
        return "Unknown Page"
    
    def reconstruct_path(self, target_url):
        """Rebuild path from start to target"""
        path = []
        current = target_url
        
        while current is not None:
            path_info = self.paths.get(current)
            if not path_info:
                break
            
            path.append(path_info['title'])
            current = path_info['prev']
        
        return list(reversed(path))
    
    def closed(self, reason):
        """Handle spider closing"""
        if reason == 'finished' and not any(url == self.target_url for url in self.visited):
            print(f"Could not find path to Kevin Bacon within {self.max_depth} steps!")
            
            # Get start title
            start_title = self.start_title if self.start_title else "Unknown"
            
            # Write results
            result = {
                'path': [],
                'degrees': -1,
                'success': False,
                'message': f"Could not find a path from '{start_title}' to 'Kevin Bacon' within {self.max_depth} steps."
            }
            
            with open('output.json', 'w') as f:
                json.dump(result, f)


# Run this file directly with:
# scrapy runspider kevin_bacon_spider.py -a start_url="Albert_Einstein" -o results.json
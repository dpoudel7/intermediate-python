import time
import threading
import concurrent.futures
import asyncio
import aiohttp
import requests
from functools import wraps

# Timing decorator to measure execution time
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

# Async timing decorator
def async_timing_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

# 1. Traditional synchronous approach
@timing_decorator
def download_sites_sync(sites):
    """Download sites synchronously."""
    print("\nSynchronous Approach:")
    results = []
    for site in sites:
        print(f"Downloading {site}")
        response = requests.get(site)
        results.append(f"{site}: {len(response.text)} bytes")
    return results

# 2. Threading approach
@timing_decorator
def download_sites_threading(sites):
    """Download sites using multiple threads."""
    print("\nThreading Approach:")
    
    def download_site(site):
        print(f"Downloading {site} in thread {threading.current_thread().name}")
        response = requests.get(site)
        return f"{site}: {len(response.text)} bytes"
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        return list(executor.map(download_site, sites))

# 3. Multiprocessing approach
@timing_decorator
def download_sites_multiprocessing(sites):
    """Download sites using multiple processes."""
    print("\nMultiprocessing Approach:")
    
    def download_site(site):
        print(f"Downloading {site} in process {os.getpid()}")
        response = requests.get(site)
        return f"{site}: {len(response.text)} bytes"
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        return list(executor.map(download_site, sites))

# 4. Asyncio approach
@async_timing_decorator
async def download_sites_async(sites):
    """Download sites using asyncio and aiohttp."""
    print("\nAsync/Await Approach:")
    
    async def download_site(session, site):
        print(f"Downloading {site} asynchronously")
        async with session.get(site) as response:
            content = await response.text()
            return f"{site}: {len(content)} bytes"
    
    async with aiohttp.ClientSession() as session:
        tasks = [download_site(session, site) for site in sites]
        return await asyncio.gather(*tasks)

# Comparing different approaches with a simple benchmark
def compare_approaches():
    """Compare different concurrency approaches."""
    print("CONCURRENCY APPROACHES BENCHMARK")
    print("--------------------------------")
    
    # List of sites to download (using httpbin for testing)
    sites = [
        f"https://httpbin.org/delay/1?site={i}" for i in range(10)
    ]
    
    # 1. Synchronous approach
    sync_results = download_sites_sync(sites[:3])  # Using fewer sites for sync to save time
    
    # 2. Threading approach
    threading_results = download_sites_threading(sites)
    
    # 3. Multiprocessing approach
    multiprocessing_results = download_sites_multiprocessing(sites)
    
    # 4. Asyncio approach
    asyncio_results = asyncio.run(download_sites_async(sites))
    
    # Summary
    print("\nSUMMARY:")
    print("- Synchronous: Sequential, blocks during I/O, simple but slow")
    print("- Threading: Good for I/O-bound tasks, overhead for thread management")
    print("- Multiprocessing: Good for CPU-bound tasks, higher memory usage")
    print("- Asyncio: Excellent for I/O-bound tasks, single-threaded cooperative multitasking")

# Practical example: Async HTTP server
async def handle_client(reader, writer):
    """Handle a client connection asynchronously."""
    # Get client address
    addr = writer.get_extra_info('peername')
    print(f"Client connected from {addr}")
    
    # Read data
    data = await reader.read(100)
    message = data.decode()
    print(f"Received: {message}")
    
    # Simulate processing time
    await asyncio.sleep(0.1)
    
    # Send response
    response = f"Server received: {message}"
    writer.write(response.encode())
    await writer.drain()
    
    # Close connection
    writer.close()
    await writer.wait_closed()
    print(f"Closed connection with {addr}")

async def run_async_server():
    """Run an async TCP server."""
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)
    
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")
    
    async with server:
        await server.serve_forever()

# Real-world example: Async website crawler
async def fetch_url(session, url):
    """Fetch a URL asynchronously."""
    try:
        async with session.get(url, timeout=10) as response:
            print(f"Fetched {url}, status: {response.status}")
            if response.status == 200:
                return await response.text()
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def parse_links(html, base_url):
    """Parse HTML content to extract links (simplified)."""
    # This is a very simplified link extractor
    # In a real-world scenario, you would use a proper HTML parser
    links = []
    if html:
        for line in html.split('\n'):
            if 'href="' in line:
                start = line.find('href="') + 6
                end = line.find('"', start)
                if start > 6 and end > start:
                    link = line[start:end]
                    # Handle relative URLs
                    if link.startswith('/'):
                        link = f"{base_url}{link}"
                    # Only add http/https links
                    if link.startswith(('http://', 'https://')):
                        links.append(link)
    return links

async def crawl_website(start_url, max_depth=2, max_urls=20):
    """Crawl a website asynchronously to a certain depth."""
    print(f"Starting async crawl of {start_url} with depth {max_depth}")
    
    # Extract base URL
    url_parts = start_url.split('/')
    base_url = f"{url_parts[0]}//{url_parts[2]}"
    
    # Track visited URLs and discovered URLs
    visited = set()
    to_visit = [(start_url, 0)]  # (url, depth)
    results = {}
    
    async with aiohttp.ClientSession() as session:
        while to_visit and len(visited) < max_urls:
            # Get next URL to visit
            url, depth = to_visit.pop(0)
            
            # Skip if already visited or exceeds depth
            if url in visited or depth > max_depth:
                continue
            
            print(f"Crawling {url} (depth {depth})")
            visited.add(url)
            
            # Fetch the URL
            html = await fetch_url(session, url)
            if html:
                results[url] = len(html)
                
                # If not at max depth, find links to visit next
                if depth < max_depth:
                    links = await parse_links(html, base_url)
                    for link in links:
                        if link not in visited:
                            to_visit.append((link, depth + 1))
    
    print(f"Crawl complete. Visited {len(visited)} URLs.")
    return results

# Example of a real-world async task: Parallel API queries
async def fetch_api_data(session, api_url, params=None):
    """Fetch data from an API asynchronously."""
    try:
        async with session.get(api_url, params=params) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Error {response.status} for {api_url}")
                return None
    except Exception as e:
        print(f"Exception for {api_url}: {e}")
        return None

async def parallel_api_queries():
    """Execute multiple API queries in parallel."""
    # List of APIs to query (using JSONPlaceholder for example)
    apis = [
        ("https://jsonplaceholder.typicode.com/posts", None),
        ("https://jsonplaceholder.typicode.com/comments", {"postId": 1}),
        ("https://jsonplaceholder.typicode.com/albums", None),
        ("https://jsonplaceholder.typicode.com/photos", {"albumId": 1}),
        ("https://jsonplaceholder.typicode.com/todos", {"userId": 1}),
        ("https://jsonplaceholder.typicode.com/users", None),
    ]
    
    print("Starting parallel API queries")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_api_data(session, url, params) for url, params in apis]
        results = await asyncio.gather(*tasks)
        
        # Process results
        for i, result in enumerate(results):
            if result:
                url, _ = apis[i]
                if isinstance(result, list):
                    print(f"API {url}: Retrieved {len(result)} items")
                else:
                    print(f"API {url}: Retrieved data successfully")
            else:
                url, _ = apis[i]
                print(f"API {url}: Failed to retrieve data")
    
    end_time = time.time()
    print(f"Parallel API queries completed in {end_time - start_time:.2f} seconds")

# Demonstrate async in the context of a web scraper
async def async_web_scraper_demo():
    """Demonstrate using async for a simple web scraper."""
    print("\nASYNCHRONOUS WEB SCRAPER DEMONSTRATION")
    print("-------------------------------------")
    
    # List of URLs to scrape
    urls = [
        "https://example.com",
        "https://httpbin.org",
        "https://python.org",
        # Add more URLs as needed
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_url(session, url))
        
        # Execute all tasks concurrently
        results = await asyncio.gather(*tasks)
        
        # Process results
        for i, html in enumerate(results):
            if html:
                print(f"Successfully scraped {urls[i]}, size: {len(html)} bytes")
            else:
                print(f"Failed to scrape {urls[i]}")

# Main function to demonstrate different approaches
def main():
    """Main function to demonstrate concurrency approaches."""
    import os  # Import here for the multiprocessing example
    
    # Compare different approaches
    compare_approaches()
    
    # Run async demo if requested
    print("\nTo run the async web scraper demo, uncomment the following line:")
    # asyncio.run(async_web_scraper_demo())
    
    print("\nTo run the async crawler, uncomment the following line:")
    # asyncio.run(crawl_website("https://example.com", max_depth=1, max_urls=5))
    
    print("\nTo run the parallel API queries demo, uncomment the following line:")
    # asyncio.run(parallel_api_queries())
    
    print("\nTo run the async server, uncomment the following line:")
    # asyncio.run(run_async_server())

if __name__ == "__main__":
    main()
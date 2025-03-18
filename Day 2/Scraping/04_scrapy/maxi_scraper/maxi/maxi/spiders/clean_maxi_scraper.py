import scrapy
import hashlib
from scrapy.loader import ItemLoader
from ..items import MaxiItem

class MaxiSpider(scrapy.Spider):
    name = 'maxi'
    allowed_domains = ['maxi.rs']
    base_url = 'https://www.maxi.rs'
    
    def start_requests(self):
        """Start with the frozen products category"""
        categories = [
            '/online/Smrznuti-proizvodi/c/06',
        ]
        
        for category in categories:
            url = self.base_url + category
            yield scrapy.Request(
                url=url,
                callback=self.parse_category,
                meta={'category': category.split('/')[-2].replace('-', ' ')}
            )

    def parse_category(self, response):
        """Parse products from category page"""
        products = response.css('li.product-item')
        
        for product in products:
            loader = ItemLoader(item=MaxiItem(), selector=product)
            
            # Load basic information
            loader.add_css('product_name', 'div[data-testid="product-block-product-name"]::text')
            loader.add_css('brand_name', 'div[data-testid="product-block-brand-name"]::text')
            loader.add_css('quantity_measurement', 'div[data-testid="product-block-supplementary-price-2"]::text')
            loader.add_css('product_image', 'img[data-testid="product-block-image"]::attr(src)')
            
            # Handle URL
            product_url = product.css('div[data-testid="product-block-product-name"] a::attr(href)').get()
            loader.add_value('original_url', product_url)
            loader.add_value('product_id', product_url.split('/')[-1] if product_url else '')
            
            # Generate hash
            if product_url:
                full_url = self.base_url + product_url
                loader.add_value('product_hash', hashlib.md5(full_url.encode()).hexdigest())
            
            # Add category and currency
            loader.add_value('category', response.meta['category'])
            loader.add_value('currency', 'RSD')
            
            # Check availability
            is_available = not product.css('div[data-testid="product-block-unavailable-text"]')
            loader.add_value('is_available', is_available)
            
            if is_available:
                loader.add_css('price', 'div[data-testid="product-block-price"]::text')
                loader.add_css('price_per_unit', 'div[data-testid="product-block-price-per-unit"]::text')
            
            # Check for discount
            old_price = product.css('span[data-testid="product-block-old-price"]::text').get()
            if old_price:
                loader.add_value('discount', True)
                loader.add_css('old_price', 'span[data-testid="product-block-old-price"]::text')
                loader.add_css('old_price_per_unit', 'span[data-testid="product-block-old-ppu"]::text')
                
                # Get discount dates from product page
                yield scrapy.Request(
                    url=self.base_url + product_url,
                    callback=self.parse_discount_dates,
                    meta={'loader': loader}
                )
            else:
                loader.add_value('discount', False)
                yield loader.load_item()

        # Handle pagination
        current_page = response.meta.get('page', 1)
        next_page = current_page + 1
        next_page_url = f"{response.url}?page={next_page}"
        
        if products:
            yield scrapy.Request(
                url=next_page_url,
                callback=self.parse_category,
                meta={
                    'category': response.meta['category'],
                    'page': next_page
                }
            )

    def parse_discount_dates(self, response):
        """Extract discount dates from product page"""
        loader = response.meta['loader']
        
        date_text = response.css('span[data-testid="promo-expiration-date"]::text').get()
        if date_text:
            parts = date_text.lower().split('do')
            loader.add_value('discount_end', parts[-1])
            loader.add_value('discount_start', parts[0].split()[1])
        
        yield loader.load_item()
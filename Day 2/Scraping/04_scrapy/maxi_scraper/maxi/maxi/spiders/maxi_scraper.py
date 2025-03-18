import scrapy
import hashlib
from datetime import datetime

class MaxiSpider(scrapy.Spider):
    name = 'maxi'
    allowed_domains = ['maxi.rs']
    base_url = 'https://www.maxi.rs'
    
    def start_requests(self):
        """Start with the frozen products category"""
        categories = [
            '/online/Smrznuti-proizvodi/c/06',
            # Add more categories as needed
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
        # Extract all products from the page
        products = response.css('li.product-item')
        
        for product in products:
            product_data = self.extract_product_data(product, response.meta['category'])
            
            if product_data:
                if product_data['discount']:
                    # If product is discounted, get discount dates
                    yield scrapy.Request(
                        url=product_data['original_url'],
                        callback=self.parse_discount_dates,
                        meta={'product_data': product_data}
                    )
                else:
                    yield product_data

        # Check for next page
        # Maxi uses page parameter in URL
        current_page = response.meta.get('page', 1)
        next_page = current_page + 1
        next_page_url = f"{response.url}?page={next_page}"
        
        # Check if there are more products (you might need to adjust this condition)
        if products:
            yield scrapy.Request(
                url=next_page_url,
                callback=self.parse_category,
                meta={
                    'category': response.meta['category'],
                    'page': next_page
                }
            )

    def extract_product_data(self, product, category):
        """Extract data from product HTML"""
        try:
            name_div = product.css('div[data-testid="product-block-product-name"]')
            product_url = name_div.css('a::attr(href)').get()
            
            product_data = {
                "product_name": name_div.css('::text').get(),
                "original_url": self.base_url + product_url if product_url else "",
                "currency": 'RSD',
                "category": category,
                "brand_name": product.css('div[data-testid="product-block-brand-name"]::text').get() or "",
                "quantity_measurement": product.css('div[data-testid="product-block-supplementary-price-2"]::text').get() or "",
                "product_image": product.css('img[data-testid="product-block-image"]::attr(src)').get() or "",
            }
            
            # Check availability
            unavailable = product.css('div[data-testid="product-block-unavailable-text"]')
            product_data['is_available'] = not unavailable
            
            if product_data['is_available']:
                product_data['price'] = self.clean_price(
                    product.css('div[data-testid="product-block-price"]::text').get()
                )
                product_data['price_per_unit'] = product.css('div[data-testid="product-block-price-per-unit"]::text').get() or ""
            else:
                product_data['price'] = ""
                product_data['price_per_unit'] = ""
            
            # Check for discount
            old_price = product.css('span[data-testid="product-block-old-price"]::text').get()
            if old_price:
                product_data['old_price'] = self.clean_price(old_price)
                product_data['old_price_per_unit'] = product.css('span[data-testid="product-block-old-ppu"]::text').get() or ""
                product_data['discount'] = True
            else:
                product_data['old_price'] = ""
                product_data['old_price_per_unit'] = ""
                product_data['discount'] = False
            
            # Generate hash and ID
            product_data['product_hash'] = hashlib.md5(
                product_data['original_url'].encode()
            ).hexdigest()
            product_data['product_id'] = product_url.split('/')[-1] if product_url else ""
            
            # Initialize discount dates
            product_data['discount_start'] = ""
            product_data['discount_end'] = ""
            
            return product_data
            
        except Exception as e:
            self.logger.error(f"Error extracting product data: {e}")
            return None

    def parse_discount_dates(self, response):
        """Extract discount dates from product page"""
        product_data = response.meta['product_data']
        
        try:
            date_text = response.css('span[data-testid="promo-expiration-date"]::text').get()
            if date_text:
                parts = date_text.lower().split('do')
                product_data['discount_end'] = parts[-1].strip()
                product_data['discount_start'] = parts[0].split()[1].strip()
        except Exception as e:
            self.logger.error(f"Error extracting discount dates: {e}")
        
        yield product_data

    def clean_price(self, price_text):
        """Clean price text to standard format"""
        if not price_text:
            return ""
        return price_text.split()[0].replace(",", ".")
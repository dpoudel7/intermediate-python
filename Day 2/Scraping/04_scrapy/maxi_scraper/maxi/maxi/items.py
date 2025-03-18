from scrapy import Item, Field
from itemloaders.processors import TakeFirst, Join, MapCompose
from w3lib.html import remove_tags
import re

def clean_price(value):
    """Remove currency, spaces and convert comma to dot"""
    if not value:
        return ""
    # Remove non-digit characters except comma and dot
    cleaned = re.sub(r'[^\d,.]', '', value)
    return cleaned.replace(',', '.')

def clean_text(value):
    """Remove extra whitespace and HTML tags"""
    if not value:
        return ""
    # Remove HTML tags and extra whitespace
    return ' '.join(remove_tags(value).strip().split())

def clean_url(value):
    """Ensure URL starts with https://www.maxi.rs"""
    if not value:
        return ""
    if not value.startswith('https://'):
        return f"https://www.maxi.rs{value}"
    return value

def clean_date(value):
    """Clean date string"""
    if not value:
        return ""
    # Remove extra whitespace
    return value.strip()

class MaxiItem(Item):
    # Basic product information
    product_name = Field(
        input_processor=MapCompose(clean_text),
        output_processor=TakeFirst()
    )
    brand_name = Field(
        input_processor=MapCompose(clean_text),
        output_processor=TakeFirst()
    )
    product_id = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    product_hash = Field(
        output_processor=TakeFirst()
    )
    
    # URLs and images
    original_url = Field(
        input_processor=MapCompose(clean_url),
        output_processor=TakeFirst()
    )
    product_image = Field(
        input_processor=MapCompose(clean_url),
        output_processor=TakeFirst()
    )
    
    # Price information
    currency = Field(
        output_processor=TakeFirst()
    )
    price = Field(
        input_processor=MapCompose(clean_price),
        output_processor=TakeFirst()
    )
    price_per_unit = Field(
        input_processor=MapCompose(clean_text),
        output_processor=TakeFirst()
    )
    old_price = Field(
        input_processor=MapCompose(clean_price),
        output_processor=TakeFirst()
    )
    old_price_per_unit = Field(
        input_processor=MapCompose(clean_text),
        output_processor=TakeFirst()
    )
    
    # Product details
    quantity_measurement = Field(
        input_processor=MapCompose(clean_text),
        output_processor=TakeFirst()
    )
    category = Field(
        input_processor=MapCompose(clean_text),
        output_processor=TakeFirst()
    )
    
    # Availability and discount information
    is_available = Field(
        output_processor=TakeFirst()
    )
    discount = Field(
        output_processor=TakeFirst()
    )
    discount_start = Field(
        input_processor=MapCompose(clean_date),
        output_processor=TakeFirst()
    )
    discount_end = Field(
        input_processor=MapCompose(clean_date),
        output_processor=TakeFirst()
    )
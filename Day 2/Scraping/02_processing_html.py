# -----------------------------------------------------------------------------
# PROCESSING HTML WITH BEAUTIFULSOUP
# -----------------------------------------------------------------------------

"""
This tutorial demonstrates how to extract data from HTML using BeautifulSoup.
We'll scrape a product page to extract basic product information.
"""

import requests
from bs4 import BeautifulSoup

# 1. Get the webpage content
url = "https://pypi.org/project/tensorflow/"
response = requests.get(url)

# 2. Create BeautifulSoup object
# 'html.parser' is Python's built-in parser
soup = BeautifulSoup(response.text, 'html.parser')

# class: package-header__date
print(soup.find("p", {"class": "package-header__date"}).time.text.strip())


print(soup.findAll("h1", {"class": "package-header__name"})[0].text.strip())


for el in soup.findAll("a", {"class": "vertical-tabs__tab--condensed"}):
    i = el.find("i")
    if i and "fa-home" in i.get("class"):
        print(el.get("href"))
        break


maintainers = set()
for maintainer in soup.findAll("span", {"class": "sidebar-section__maintainer"}):
    maintainers.add(maintainer.a.text.strip())


print(maintainers)









# # 3. Find all product items
# # Each product is in a <li> tag with class "product-item"
# products = soup.findAll("li", {"class": "product-item"})
# print(f"Found {len(products)} products\n")

# name = None
# # 4. Extract data from first product
# if products:
#     product = products[0]  # Get first product
    
#     # Find product name
#     # Using find() with data-testid attribute
#     name = product.find("div", attrs={'data-testid': "product-block-product-name"})
#     print(f"Product name: {name.text if name else 'Not found'}")
    
#     # Get product URL from the anchor tag inside name div
#     url = name.a.get('href') if name and name.a else 'Not found'
#     print(f"Product URL: {url}")
    
#     # Find brand name
#     brand = product.find("div", attrs={'data-testid': "product-block-brand-name"})
#     print(f"Brand: {brand.text if brand else 'Not found'}")
    
#     # Get product image URL
#     image = product.find("img", attrs={'data-testid': "product-block-image"})
#     print(f"Image URL: {image.get('src') if image else 'Not found'}")
    
#     # Check if product is available
#     unavailable = product.find("div", attrs={"data-testid": "product-block-unavailable-text"})
#     is_available = unavailable is None
#     print(f"Is available: {is_available}")
    
#     # Get price information if available
#     if is_available:
#         price = product.find("div", attrs={'data-testid': "product-block-price"})
#         price_text = price.text.split()[0].replace(",", ".") if price else 'Not found'
#         print(f"Price: {price_text} RSD")
        
#         # Get price per unit
#         ppu = product.find("div", attrs={'data-testid': "product-block-price-per-unit"})
#         print(f"Price per unit: {ppu.text if ppu else 'Not found'}")
    
#     # Check for discount
#     old_price = product.find("span", attrs={'data-testid': 'product-block-old-price'})
#     if old_price:
#         print(f"Old price: {old_price.text.split()[0].replace(',', '.')} RSD")
        
#         old_ppu = product.find("span", attrs={'data-testid': 'product-block-old-ppu'})
#         print(f"Old price per unit: {old_ppu.text if old_ppu else 'Not found'}")

# # 5. Demonstrate other useful BeautifulSoup methods
# print("\nOther useful BeautifulSoup methods:")

# # Find by CSS selector
# print("\nUsing CSS selector:")
# products_css = soup.select("li.product-item")
# print(f"Found {len(products_css)} products using CSS selector")

# # Find parent element
# if name:
#     print("\nParent element:")
#     print(name.parent.name)

# # Find next sibling
# if name:
#     print("\nNext sibling:")
#     print(name.next_sibling)

# # Get all text from page
# print("\nAll text (first 100 characters):")
# print(soup.get_text()[:100])
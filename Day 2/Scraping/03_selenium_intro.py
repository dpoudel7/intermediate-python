from selenium import webdriver 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.common.exceptions import WebDriverException 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 

import time 
import hashlib 
import pandas as pd 

from tqdm import tqdm 
from bs4 import BeautifulSoup 
 
class ScraperBase(object): 
 
    def __init__(self, headless=True): 
 
        self.headless = headless 
         
        # service = Service(executable_path=r'/usr/bin/chromedriver') 
        # driver = webdriver.Chrome(service=service, options=options) 
 
        self.chrome_options = webdriver.ChromeOptions() 
 
        self.chrome_options.add_argument("--headless") 
        self.chrome_options.add_argument('--no-sandbox') 
        self.chrome_options.add_argument('--disable-dev-shm-usage') 
        self.chrome_options.add_argument("--ignore-certificate-errors") 
        self.chrome_options.add_argument("user-agent=Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393") 
        self.chrome_options.add_argument("--disable-extensions") 
 
        self._driver_start() 
         
 
    def _driver_start(self): 
        """ 
        Call this function to define the driver. 
        """ 
        if self.headless: 
            self.driver = webdriver.Chrome(options=self.chrome_options) 
        else: 
            self.driver = webdriver.Chrome() 
 
    def _driver_stop(self): 
        """ 
        Call this function to close the driver. 
        """ 
        self.driver.close() 
        self.driver.quit() 
 
    def _is_driver_alive(self): 
        """ 
        Call this function to check if the driver is ONLINE (alive) or not. 
        :returns: Boolean, True if the driver is ONLINE, otherwise False. 
        """ 
        try: 
            self.driver.title() 
            return True 
        except WebDriverException: 
            return False 
 
    def __link_builder(self, ): 
        raise NotImplementedError 
     
    def __post_object(self,): 
         
        raise NotImplementedError 
 
    def scrape(self,): 
        raise NotImplementedError


class MaxiScraper(ScraperBase): 
 
    def __init__(self, headless=True): 
        super().__init__(headless) 
 
        self.home_link = "https://www.maxi.rs" 
         
        self.links_to_scrape = [ 
            "https://www.maxi.rs/online/Smrznuti-proizvodi/c/06", 
        ] 
         
    def __link_builder(self, link, page_num): 
 
        return link + "?pageNumber={}".format(page_num) 
 
    def __get_discount_dates(self, url): 
         
        _ = self.driver.get(url) 
         
        time.sleep(3) 
        product_page_obj = BeautifulSoup(self.driver.page_source, 'lxml') 
         
        start = None 
        end = None 
         
        try: 
            date = product_page_obj.find("span", attrs={'data-testid' : "promo-expiration-date"}).text 
 
            parts = date.lower().split("do") 
            end = parts[-1].strip() 
            start = parts[0].split()[1].strip() 
        except: 
            start = "" 
            end = "" 
        return start, end 
     
    def __post_object(self, html): 
         
        try: 
            product_obj = { 
                "product_name": html.find("div", attrs={'data-testid' : "product-block-product-name"}).text, 
                "original_url": self.home_link + html.find("div", attrs={'data-testid' : "product-block-product-name"}).a.get('href'), 
                "currency": 'RSD', 
            } 
        except: 
            return None 
 
         
        try: 
            product_obj['brand_name'] = html.find("div", attrs={'data-testid' : "product-block-brand-name"}).text 
        except: 
            product_obj['brand_name'] = "" 
         
        try: 
            product_obj["quantity_measurement"] = html.find("div", attrs={'data-testid' : "product-block-supplementary-price-2"}).text 
        except: 
            product_obj["quantity_measurement"] = "" 
 
         
        try: 
            product_obj['product_image'] = html.find("img", attrs={'data-testid' : "product-block-image"}).get("src") 
        except: 
            product_obj['product_image'] = "" 
         
        is_available = html.find("div", attrs={"data-testid": "product-block-unavailable-text"}) 
         
        if is_available is None: 
            # This means it IS available 
            try: 
                product_obj["price_per_unit"] =  html.find("div", attrs={'data-testid' : "product-block-price-per-unit"}).text 
            except: 
                product_obj['price_per_unit'] = "" 
             
            product_obj['price'] = html.find("div", attrs={'data-testid' : "product-block-price"}).text.split()[0].replace(",", ".") 
            product_obj['is_available'] = True 
        else:
            product_obj["price_per_unit"] = "" 
            product_obj['price'] = "" 
            product_obj['is_available'] = False 
             
         
        try: 
            product_obj['old_price'] = html.find("span", attrs={'data-testid': 'product-block-old-price'}).text.split()[0].replace(",", ".") 
            product_obj['old_price_per_unit'] = html.find("span", attrs={'data-testid': 'product-block-old-ppu'}).text 
            product_obj['discount'] = True 
        except: 
            product_obj['old_price'] = "" 
            product_obj['discount'] = False 
         
        product_obj['product_hash'] = hashlib.md5(product_obj['original_url'].encode()).hexdigest() 
        product_obj['product_id'] = product_obj['original_url'].split("/")[-1] 
        product_obj['discount_start'] = "" 
        product_obj['discount_end'] = "" 
         
        return product_obj 
 
    def scrape(self, file_name): 
 
        products = {} 
         
        for link in tqdm(self.links_to_scrape): 
             
            page_num = 1 
            while True: 
                 
                page_link = self.__link_builder(link, page_num) 
                page_num += 1 
                _ = self.driver.get(page_link) 
 
                time.sleep(3) 
                page_object = BeautifulSoup(self.driver.page_source, 'lxml') 
                 
                page_products = page_object.findAll("li", {"class":"product-item"}) 
                     
                if len(page_products) < 1: 
                    break 
                     
                for product in page_products: 
                    product_obj = self.__post_object(product) 
                    if product_obj is not None and product_obj['product_hash'] not in products: 
                         
                        if product_obj['discount']: 
                            start, end = self.__get_discount_dates(product_obj['original_url']) 
                            product_obj['discount_start'] = start 
                            product_obj['discount_end'] = end 
                         
                        product_obj['category'] = page_link.split("/c")[0].split("/")[-1].replace("-", " ") 
                         
                        products[product_obj['product_hash']] = product_obj 
 
                print("Scraped for link -> ", link) 
                print("Page processed: {}\n".format(page_num)) 
                pd.DataFrame(products.values()).to_csv(file_name, index=False)  
             
 
        # Close driver 
        self._driver_stop() 
 
        return products 
     
    def scrape_product_page_image(self, url): 
        _ = self.driver.get(url) 
         
        time.sleep(2) 
        product_page_obj = BeautifulSoup(self.driver.page_source, 'lxml') 
         
         
        try: 
            img = product_page_obj.find("div", attrs={'id' : "main-content"}).img 
 
            return img.get("src") 
        except Exception as e: 
            print("IMG error " + str(e)) 
            return "" 
 
 
if name == "__main__": 
         
        scraper = MaxiScraper() 
        scraper.scrape()
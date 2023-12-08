import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from sel_scrapy.items import LaptopItem 




class LaptopsSpider(scrapy.Spider):
    name = "laptops"


    def start_requests(self):
        options = Options()
        options.add_argument('--headless')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

        driver.get('https://www.lazada.com.ph/shop-laptops/')
        xpath = '//*[@data-qa-locator="product-item"]//a[text()]'
        # link_elements = driver.find_elements_by_xpath(xpath) || not valid in new selenium version
        link_elements = driver.find_elements(By.XPATH, xpath)
        for link_el in link_elements: 
            href = link_el.get_attribute("href") 
            yield scrapy.Request(href)

        driver.quit()

    def parse(self, response):
        item = LaptopItem()
        item['price'] = response.css('.pdp-price_color_orange ::text').get()
        item['name'] = response.css('h1 ::text').get()
        yield item

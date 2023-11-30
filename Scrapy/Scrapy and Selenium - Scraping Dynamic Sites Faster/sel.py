from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.lazada.com.ph/shop-laptops/')

xpath = '//*[@data-qa-locator="product-item"]//a[text()]'
# link_elements = driver.find_elements_by_xpath(xpath) || not valid in new selenium version
link_elements = driver.find_elements(By.XPATH, xpath)

links = [] 

for link_el in link_elements: 
    href = link_el.get_attribute("href") 
    print(href)
    links.append(href) 

driver.quit()
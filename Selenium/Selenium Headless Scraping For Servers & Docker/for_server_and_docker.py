import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




chrome_options = Options()
chrome_options.add_argument('--no-sandbox') # it is for security concern, it does not allow chrome to open sandbox
# it is used when containerizing the selenium application
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--disable-dev-shm-usage') #by default selenium-chrome uses short term memory, which is slower in size,
# by disabling it, it then uses disk memory || the CON is it's slower 


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) 


url = 'https://www.neuralnine.com/books'

driver.get(url)

soup = BeautifulSoup(driver.page_source, features='lxml') 


headings = soup.find_all(name = "h2", attrs = {'class':'elementor-heading-title'})

for heading in headings:
    print(heading.getText())


time.sleep(10)

driver.quit()
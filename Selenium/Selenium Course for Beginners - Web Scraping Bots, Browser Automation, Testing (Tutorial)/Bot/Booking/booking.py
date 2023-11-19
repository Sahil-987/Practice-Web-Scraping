from selenium import webdriver 
import Booking.constants as const
from selenium.webdriver.common.by import By



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Booking(webdriver.Chrome):

    def __init__(self,  teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)


    def change_currency(self, currency=None):
        # currency_element = self.find_element_by_css_selector(
        #     'button[data-tooltip-text="Choose your currency"]'
        # )

        # selenium has changed their docs
        currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
from selenium.webdriver.common.by import By
from PythonPytestHomework43.Selenium_commands.POM.lib.helpers import Helpers


class HomePage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    shoes_section = (By.XPATH, '//*[@href ="/shoes"]')
    customer_service_icon = (By.CLASS_NAME, 'V-z')

    def click_on_shoes_part(self):
        self.find_and_click(self.shoes_section)

    def click_on_customer_service_icon(self):
        self.find_and_click(self.customer_service_icon)



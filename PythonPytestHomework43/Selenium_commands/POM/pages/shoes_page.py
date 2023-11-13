# from hamcrest import equal_to

from selenium.webdriver.common.by import By
from PythonPytestHomework43.Selenium_commands.POM.lib.helpers import Helpers


class ShoesPage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    text_for_women_on_shoes_page = (By.CLASS_NAME, 'fX-z')
    best_sellers_btn = (By.CLASS_NAME, "Gda-z")
    first_item_on_best_sellers_part = (By.CLASS_NAME, 'pR-z')
    add_to_shipping_bag_btn = (By.ID, 'add-to-cart-button')

    def assert_text_on_women_shoes_page(self, text="Top Shoe Categories for Women"):
        selected_item = self.find(self.text_for_women_on_shoes_page, get_text=True)
        assert selected_item == text

    def click_on_shop_all_women_best_selling_shoes_btn(self):
        self.find_and_click(self.best_sellers_btn)

    def click_on_the_first_shoes_item(self):
        self.find_and_click(self.first_item_on_best_sellers_part)

    def click_on_add_shopping_bag_btn(self):
        self.find_and_click(self.add_to_shipping_bag_btn)

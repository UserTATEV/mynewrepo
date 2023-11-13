import pytest

from PythonPytestHomework43.Selenium_commands.POM.pages.customer_service_center_page import CustomerServicePage
from PythonPytestHomework43.Selenium_commands.POM.pages.home_page import HomePage
from PythonPytestHomework43.Selenium_commands.POM.pages.shoes_page import ShoesPage


@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def navigate_to_home_page_shoes_part(self):
        self.homepage.click_on_shoes_part()

    def check_text_on_women_shoes_page(self):
        self.shoespage.assert_text_on_women_shoes_page()

    def navigate_to_women_best_sellers_part(self):
        self.shoespage.click_on_shop_all_women_best_selling_shoes_btn()
        self.shoespage.click_on_the_first_shoes_item()
        self.homepage.click_on_customer_service_icon()

    def navigate_to_customer_service_center_and_assert_header(self):
        self.customerservice_center_page.assert_header_on_customer_service_page()




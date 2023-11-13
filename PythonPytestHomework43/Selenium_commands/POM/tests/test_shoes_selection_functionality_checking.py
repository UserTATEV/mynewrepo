import pytest

from PythonPytestHomework43.Selenium_commands.POM.tests.base_test import BaseTest


class TestShoesSelection(BaseTest):
    def test_shoes_part(self):
        self.navigate_to_home_page_shoes_part()
        self.check_text_on_women_shoes_page()
        self.navigate_to_women_best_sellers_part()
        self.navigate_to_customer_service_center_and_assert_header()



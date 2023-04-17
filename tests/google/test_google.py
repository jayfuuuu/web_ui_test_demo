import json
from time import sleep

import pytest

from page.google.home_page.home_page import HomePage


class TestClass:

    home_page_test_data = json.load(open("./test_data/google/home_page.json"))

    @pytest.mark.parametrize("data", home_page_test_data)
    def test_google_web(self, data, chrome_driver):
        driver = chrome_driver

        driver.get(data['url'])
        HomePage(driver).search_text_field()
        sleep(5)

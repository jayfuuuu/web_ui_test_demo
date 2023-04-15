import json
from time import sleep

import pytest


class TestClass:

    home_page_test_data = json.load(open("./test_data/google/home_page.json"))

    @pytest.mark.parametrize("data", home_page_test_data)
    def test_google_web(self, data, chrome_driver, safari_driver):
        if data['driver'] == "chrome":
            driver = chrome_driver
        elif data['driver'] == "safari":
            driver = safari_driver

        driver.get(data['url'])
        sleep(5)

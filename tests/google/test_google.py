import json
from time import sleep

import pytest
from page.facebook.login_page import LoginPage

from page.google.home_page import HomePage
from page.google.search_result_page import SearchResultPage


class TestClass:

    home_page_test_data = json.load(open("./test_data/google/home_page.json"))

    @pytest.mark.parametrize("data", home_page_test_data)
    def test_google_web(self, data, chrome_driver):
        # TODO: enhancement declare data methods
        test_data = data['test']
        request_data = data['request']
        # init driver and pages
        driver = chrome_driver
        driver.get(data['url'])
        home_page, search_result_page, login_page = HomePage(driver), SearchResultPage(driver), LoginPage(driver)
        # step 1: google text
        home_page.search_text(request_data['search_text'])
        home_page.click_search_btn()
        res = search_result_page.search_result(test_data['result_text'])
        # test
        assert res.text == test_data['result_text']
        # step 2: select result
        res = search_result_page.click_search_result(test_data['result_text'])
        assert login_page.is_exist(res)

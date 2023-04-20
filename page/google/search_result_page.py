from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page.base_page import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, page_name="SearchResultPage")

    def is_exist(self, element):
        return self.check_exist(element)

    def search_result(self, text):
        return self.wait_for_element(
            By.XPATH, f"//*[contains(text(), '{text}')]"
        )

    def click_search_result(self, text):
        return self.wait_for_element(
            By.XPATH, f"//*[contains(text(), '{text}')]"
        ).click()

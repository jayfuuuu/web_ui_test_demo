from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, page_name="HomePage")

    def is_exist(self, element):
        return self.check_exist(element)

    def search_text(self, text: str):
        return self.wait_for_element(
            By.XPATH, '//*[@id="APjFqb"]'
        ).send_keys(text)

    def click_search_btn(self):
        return self.find_element(
            By.NAME, 'btnK'
        ).click()

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, page_name="LoginPage")

    def is_exist(self, element):
        return self.check_exist(element)

    def type_email(self, text):
        return self.wait_for_element(
            By.NAME, 'email'
        ).send_keys(text)

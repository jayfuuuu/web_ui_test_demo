from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_text_field(self):
        self.driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys("webdriver" + Keys.ENTER)

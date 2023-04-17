from logging import Logger
import os
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # def screenshot(self, msg=""):
    #     now = Time.now(format="%H:%M:%S")
    #     file_name = f"{msg}_{now}.png"
    #     screenshot_dir = "../screenshots/"
    #     current_dir = os.path.dirname(__file__)
    #     destination_dir = os.path.join(current_dir, screenshot_dir)
    #     destination_file = os.path.join(destination_dir, file_name)
    #     try:
    #         if not os.path.exists(destination_dir):
    #             os.makedirs(destination_dir)
    #         self.driver.save_screenshot(destination_file)
    #         LOGGER.info(f"Screenshot save to directory: {destination_file}")
    #     except Exception as e:
    #         LOGGER.error(f"# Exception: Exception Occurred when taking screenshot, {e}")
    #     return destination_file

    def find_element(self, type, locator):
        element = None
        try:
            element = self.driver.find_element(type, locator)
            Logger.info(f"Element found with locator: \'{locator}\', locatorType: {type}")
        except Exception as e:
            self.screenshot(msg="ElementNotFound")
            Logger.error(f"# Exception: Element not found with locator: \'{locator}\', locatorType: {type}.")
        return element

    def find_elements(self, type, locator):
        elements = None
        try:
            elements = self.driver.find_elements(type, locator)
            Logger.info(f"Element found with locator: \'{locator}\', locatorType: {type}")
        except Exception as e:
            self.screenshot(msg="ElementNotFound")
            Logger.error(f"# Exception: Element not found with locator: \'{locator}\', locatorType: {type}.")
        return elements

    def wait_for_element(self, type, locator, timeout=10, frequency=1):
        element = None
        try:
            Logger.info(f"Waiting for maximum {timeout} seconds for element to be present, Locator: \'{locator}\'")
            wait = WebDriverWait(self.driver, timeout, frequency)
            element = wait.until(EC.presence_of_element_located((type, locator)))
            Logger.info(f"Element found with locator: \'{locator}\', locatorType: {type}")
        except Exception as e:
            self.screenshot(msg="ElementNotFound")
            Logger.error(f"# Exception: Element not found with locator: \'{locator}\', locatorType: {type}.")
        return element

    def wait_for_elements(self, type, locator, timeout=10, frequency=1):
        elements = None
        try:
            Logger.info(f"Waiting for maximum {timeout} seconds for elements to be present, Locator: \'{locator}\'")
            wait = WebDriverWait(self.driver, timeout, frequency)
            elements = wait.until(EC.presence_of_all_elements_located((type, locator)))
            Logger.info(f"Elements found with locator: \'{locator}\', locatorType: {type}")
        except Exception as e:
            self.screenshot(msg="ElementsNotFound")
            Logger.error(f"# Exception: Elements not found with locator: \'{locator}\', locatorType: {type}.")
        return elements

    def wait_for_element_invisibility(self, element, timeout=10, frequency=1):
        try:
            Logger.info(f"Waiting for maximum {timeout} seconds for element to be invisibility, Locator: \'{element}\'")
            wait = WebDriverWait(self.driver, timeout, frequency)
            element = wait.until(EC.invisibility_of_element(element))
            Logger.info(f"Element invisibility with element: \'{element}\'")
        except Exception as e:
            self.screenshot(msg="ElementNotInvisibility")
            Logger.error(f"# Exception: Element not invisibility with locator: \'{element}\'")
        return element

    def is_exist(self, element):
        try:
            if element is None:
                Logger.info(f"Element not exist or not present.")
                return False
        except Exception as e:
            self.screenshot(msg="ElementNotExistException")
            Logger.error(f"# Exception: Element not exist or not present.")
            return False
        else:
            Logger.info(f"Element is exist and present.")
            return True

    def on(self, page):
        return page(self.driver)

    def tap(self, x, y):
        sleep(1)
        actions = TouchAction(self.driver)
        actions.press(x=x, y=y).release().perform()

from logging import Logger
import os
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from utils.screenshot import screenshot


class BasePage:

    def __init__(self, driver, page_name):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.logger = Logger(name=page_name)

    def find_element(self, type, locator):
        element = None
        try:
            element = self.driver.find_element(type, locator)
            self.logger.info(msg=f"Element found with locator: \'{locator}\', locatorType: {type}")
        except Exception as e:
            screenshot(self.driver, msg="ElementNotFound")
            self.logger.error(msg=f"# Exception: Element not found with locator: \'{locator}\', locatorType: {type}.")
        return element

    def find_elements(self, type, locator):
        elements = None
        try:
            elements = self.driver.find_elements(type, locator)
            self.logger.info(msg=f"Element found with locator: \'{locator}\', locatorType: {type}")
        except Exception as e:
            screenshot(self.driver, msg="ElementNotFound")
            self.logger.error(msg=f"# Exception: Element not found with locator: \'{locator}\', locatorType: {type}.")
        return elements

    def wait_for_element(self, type, locator, timeout=10, frequency=1):
        element = None
        try:
            self.logger.info(
                msg=f"Waiting for maximum {timeout} seconds for element to be present, Locator: \'{locator}\'")
            wait = WebDriverWait(self.driver, timeout, frequency)
            element = wait.until(EC.presence_of_element_located((type, locator)))
            self.logger.info(msg=f"Element found with locator: \'{locator}\', locatorType: {type}")
        except Exception as e:
            screenshot(self.driver, msg="ElementNotFound")
            self.logger.error(msg=f"# Exception: Element not found with locator: \'{locator}\', locatorType: {type}.")
        return element

    def wait_for_elements(self, type, locator, timeout=10, frequency=1):
        elements = None
        try:
            self.logger.info(
                msg=f"Waiting for maximum {timeout} seconds for elements to be present, Locator: \'{locator}\'")
            wait = WebDriverWait(self.driver, timeout, frequency)
            elements = wait.until(EC.presence_of_all_elements_located((type, locator)))
            self.logger.info(msg=f"Elements found with locator: \'{locator}\', locatorType: {type}")
        except Exception as e:
            screenshot(self.driver, msg="ElementNotFound")
            self.logger.error(msg=f"# Exception: Elements not found with locator: \'{locator}\', locatorType: {type}.")
        return elements

    def wait_for_element_invisibility(self, element, timeout=10, frequency=1):
        try:
            self.logger.info(
                msg=f"Waiting for maximum {timeout} seconds for element to be invisibility, Locator: \'{element}\'")
            wait = WebDriverWait(self.driver, timeout, frequency)
            element = wait.until(EC.invisibility_of_element(element))
            self.logger.info(msg=f"Element invisibility with element: \'{element}\'")
        except Exception as e:
            screenshot(self.driver, msg="ElementNotFound")
            self.logger.error(msg=f"# Exception: Element not invisibility with locator: \'{element}\'")
        return element

    def check_exist(self, element):
        try:
            if element:
                self.logger.info(f"Element not exist or not present.")
                return False
        except Exception as e:
            self.screenshot(msg="ElementNotExistException")
            self.logger.error(f"# Exception: Element not exist or not present.")
            return False
        else:
            self.logger.info(f"Element is exist and present.")
            return True

    def tap(self, x, y):
        sleep(1)
        actions = TouchAction(self.driver)
        actions.press(x=x, y=y).release().perform()

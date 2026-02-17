from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logger import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        logger.info(f"Clicking element: {locator}")
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        logger.info(f"Entering text in: {locator}")
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        text = element.text
        logger.info(f"Got text from {locator}: {text}")
        return text

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
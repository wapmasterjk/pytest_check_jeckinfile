from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'pass')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Log in")]')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error')
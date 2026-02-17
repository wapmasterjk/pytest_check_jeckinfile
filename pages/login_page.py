from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from config.config import Config

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.enter_text(LoginLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(LoginLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(LoginLocators.LOGIN_BUTTON)

    def login(self, username=None, password=None):
        if username is None:
            username = Config.USERNAME
        if password is None:
            password = Config.PASSWORD
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # def get_error_message(self):
    #     return self.get_text(LoginLocators.ERROR_MESSAGE)
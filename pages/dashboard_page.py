from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_welcome_message(self):
        return self.get_text(DashboardLocators.WELCOME_MESSAGE)

    def click_logout(self):
        self.click_element(DashboardLocators.LOGOUT_BUTTON)

    def click_organization_link(self):
        self.click_element(DashboardLocators.ORGANIZATION_LINK)
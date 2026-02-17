from pages.base_page import BasePage
from locators.organization_locators import OrganizationLocators

class OrganizationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_org_name(self):
        return self.get_text(OrganizationLocators.ORG_NAME)

    def get_members_list(self):
        return self.get_text(OrganizationLocators.MEMBERS_LIST)

    def click_settings(self):
        self.click_element(OrganizationLocators.SETTINGS_BUTTON)
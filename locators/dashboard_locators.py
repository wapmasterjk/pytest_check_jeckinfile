from selenium.webdriver.common.by import By

class DashboardLocators:
    WELCOME_MESSAGE = (By.ID, 'welcome')
    LOGOUT_BUTTON = (By.ID, 'logout')
    ORGANIZATION_LINK = (By.ID, 'org-link')
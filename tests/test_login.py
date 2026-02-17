import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.feature('Login')
@allure.story('Valid Login')
@pytest.mark.ui
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login()

    dashboard_page = DashboardPage(driver)
    assert 'Welcome' in dashboard_page.get_welcome_message()

@allure.feature('Login')
@allure.story('Invalid Login')
@pytest.mark.ui
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login('invalid', 'invalid')

    assert login_page.is_element_visible(login_page.locators.ERROR_MESSAGE)
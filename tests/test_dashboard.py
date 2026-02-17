import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login()
    yield driver

@allure.feature('Dashboard')
@allure.story('Welcome Message')
@pytest.mark.ui
def test_welcome_message(logged_in_driver):
    dashboard_page = DashboardPage(logged_in_driver)
    message = dashboard_page.get_welcome_message()
    assert 'Welcome' in message

@allure.feature('Dashboard')
@allure.story('Navigate to Organization')
@pytest.mark.ui
def test_navigate_to_organization(logged_in_driver):
    dashboard_page = DashboardPage(logged_in_driver)
    dashboard_page.click_organization_link()
    # Assume organization page loads
    assert 'Organization' in logged_in_driver.title
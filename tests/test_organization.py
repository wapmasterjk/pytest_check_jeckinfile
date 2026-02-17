import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.organization_page import OrganizationPage

@pytest.fixture
def org_driver(driver):
    login_page = LoginPage(driver)
    login_page.login()
    dashboard_page = DashboardPage(driver)
    dashboard_page.click_organization_link()
    yield driver

@allure.feature('Organization')
@allure.story('View Organization Name')
@pytest.mark.ui
def test_org_name(org_driver):
    org_page = OrganizationPage(org_driver)
    name = org_page.get_org_name()
    assert name is not None

@allure.feature('Organization')
@allure.story('View Members')
@pytest.mark.ui
def test_members_list(org_driver):
    org_page = OrganizationPage(org_driver)
    members = org_page.get_members_list()
    assert members is not None
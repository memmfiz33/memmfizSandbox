import pytest
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators

def test_should_check_login_and_registration_forms(browser):
    page = LoginPage(browser, LoginPageLocators.URL)
    page.open()

    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()


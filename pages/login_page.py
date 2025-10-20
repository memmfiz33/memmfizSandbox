import os
from dotenv import load_dotenv
from .base_page import BasePage
from .locators import LoginPageLocators

load_dotenv()
LOGIN = os.environ["selenium1py_email"]
PASSWORD = os.environ["selenium1py_password"]

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert True == (self.browser.current_url == LoginPageLocators.URL), \
            f"EXPECTED URL: '{LoginPageLocators.URL}', ACTUAL URL: '{self.browser.current_url}'"

    def should_be_login_form(self):
        assert True == self.is_element_present(*LoginPageLocators.EMAIL_INPUT_LOGIN), \
            "Login form input is not presented"
        assert True == self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_LOGIN), \
            "Password form input is not presented"

    def should_be_register_form(self):
        assert True == self.is_element_present(*LoginPageLocators.EMAIL_INPUT_REGISTRATION), \
            "Registration email form is not presented"
        assert True == self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_REGISTRATION), \
            "Registration password form is not presented"
        assert True == self.is_element_present(*LoginPageLocators.PASSWORD_CONFIRMATION_REGISTRATION), \
            "Registration password confirmation form is not presented"








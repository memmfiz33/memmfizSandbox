import os
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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

    def register_new_user(self, email, password):
        wait = WebDriverWait(self.browser, 10)

        email_input = wait.until(EC.visibility_of_element_located(
            LoginPageLocators.EMAIL_INPUT_REGISTRATION))
        email_input.send_keys(email)

        password_input = wait.until(EC.visibility_of_element_located(
            LoginPageLocators.PASSWORD_INPUT_REGISTRATION))
        password_input.send_keys(password)

        password_confirm_input = wait.until(EC.visibility_of_element_located(
            LoginPageLocators.PASSWORD_CONFIRMATION_REGISTRATION))
        password_confirm_input.send_keys(password)

        register_btn = wait.until(EC.element_to_be_clickable(
            LoginPageLocators.REGISTER_BUTTON))
        register_btn.click()












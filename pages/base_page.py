from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LoginPageLocators, BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        from pages.login_page import LoginPage  # ✅ локальный импорт
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(self.browser, self.browser.current_url)

    def go_to_basket_page(self):
        link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(BasePageLocators.BASKET_LINK)
        )
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented'

    def should_be_registration_link(self):
        assert self.is_element_present(*BasePageLocators.REGISTRATION_LINK), 'Login link is not presented'
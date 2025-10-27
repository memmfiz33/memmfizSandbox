from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import time
import math
from .base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def open(self):
        self.browser.get(self.url)

    def should_be_product_page(self):
        self.click_add_to_basket_button()
        self.solve_quiz_and_get_code()
        self.should_see_success_message_with_correct_product_name()
        self.should_see_correct_price_for_basket()

    def click_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), \
            "Add to basket button is not presented"
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_see_success_message_with_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_NAME).text
        assert product_name == message_name, f'Product name does not match message name. EXPECTED: {message_name}, ACTUAL: {product_name}'


    def should_see_correct_price_for_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_ALERT).text
        assert product_price == basket_price, f'Product price does not match basket price. EXPECTED: {product_price}, ACTUAL: {basket_price}'



from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        empty_state_text = self.browser.find_element(*BasketPageLocators.EMPTY_STATE_TEXT).text
        expected_text = "Your basket is empty. Continue shopping"
        assert expected_text in empty_state_text, f'ACTUAL: {empty_state_text}, EXPECTED: {expected_text}'
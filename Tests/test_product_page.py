from pages import locators
from pages.locators import ProductPageLocators
from pages.product_page import ProductPage

def test_click_submit_button_and_input_the_answer(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.should_open_product_page()
    product_page.click_add_to_basket_button()
    product_page.solve_quiz_and_get_code()





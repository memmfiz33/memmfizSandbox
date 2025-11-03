import time
from pages.product_page import ProductPage
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
promo_urls = [f'{product_base_link}?promo=offer{i}' for i in range(10)]
full_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"

@pytest.mark.parametrize('link', promo_urls)
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    time.sleep(3)

@pytest.mark.parametrize('link', [full_link])
@pytest.mark.three_tests_run
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    time.sleep(2)

@pytest.mark.parametrize('link', [full_link])
@pytest.mark.three_tests_run
def test_guest_cant_see_success_message1(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    time.sleep(2)

@pytest.mark.parametrize('link', [full_link])
@pytest.mark.three_tests_run
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_disappeared_success_message()


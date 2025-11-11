import time
import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


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
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    time.sleep(2)

@pytest.mark.parametrize('link', [full_link])
def test_guest_cant_see_success_message1(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    time.sleep(2)

@pytest.mark.two_tests_run
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.two_tests_run
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.parametrize('link', [full_link])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_disappeared_success_message()

@pytest.mark.parametrize('link', [full_link])
@pytest.mark.new_test
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    time.sleep(3)

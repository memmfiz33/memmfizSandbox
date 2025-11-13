import time
import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
promo_urls = [f'{product_base_link}?promo=offer{i}' for i in range(10)]
full_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"

class TestGuestUserTestFromProductPage():
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [full_link])
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()

    @pytest.mark.parametrize('link', promo_urls)
    def test_guest_can_add_product_to_basket_promo(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()

    @pytest.mark.parametrize('link', [full_link])
    def test_guest_cant_see_success_message1(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.parametrize('link', [full_link])
    @pytest.mark.xfail(reason="Expected fail due to existing message")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_button()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.parametrize('link', [full_link])
    @pytest.mark.xfail(reason="Expected fail: message does not disappear")
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_button()
        page.solve_quiz_and_get_code()
        page.should_disappeared_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [full_link])
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()

class TestUserAddToBasketFromProductPage():
    full_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = f"{time.time()}@testmail.com"
        password = "testpassword1234"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.full_link)
        page.open()
        page.should_be_product_page()

    def test_user_cant_see_success_message1(self, browser):
        page = ProductPage(browser, self.full_link)
        page.open()
        page.should_not_be_success_message()
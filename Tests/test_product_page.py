import time
from pages.product_page import ProductPage
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
promo_urls = [f'{product_base_link}?promo=offer{i}' for i in range(10)]

@pytest.mark.parametrize('link', promo_urls)
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    time.sleep(3)





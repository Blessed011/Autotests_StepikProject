from pages.main_page import MainPage
from pages.product_page import ProductPage
import pytest
import time

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [f"{base_link}{n}" for n in range(7)]

@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    time.sleep(5)
    product_page.should_be_book_name_in_message()
    product_page.should_be_book_price_equal_basket_price()
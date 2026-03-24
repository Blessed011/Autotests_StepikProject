from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"

    def should_be_book_name_in_message(self):
        book_header = self.browser.find_element(*ProductPageLocators.BOOK_HEADER)
        book_name_in_msg = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MESSAGE)
        assert book_header.text == book_name_in_msg.text, 'Book name is not same in message'

    def should_be_book_price_equal_basket_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert book_price.text == basket_price.text, 'Prices are not equal'
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are items in basket though there should not be"

    def should_be_empty_basket_text(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text == "Your basket is empty. Continue shopping", "There is no empty basket text"
from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > .btn-group > a.btn.btn-default")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form button[type="submit"]')
    BOOK_HEADER = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_NAME_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info.fade.in > div p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in')

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > P")
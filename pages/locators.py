from selenium.webdriver.common.by import By


class ProductPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    CONFIRMATION_MESSAGE1 = (By.CSS_SELECTOR, '.alert:first-child strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    CONFIRMATION_MESSAGE2 = (By.CSS_SELECTOR, '.alert:last-child strong')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

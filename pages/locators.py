from selenium.webdriver.common.by import By


class ProductPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    CONFIRMATION_MESSAGE1 = (By.CSS_SELECTOR, '.alert:first-child strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    CONFIRMATION_MESSAGE2 = (By.CSS_SELECTOR, '.alert:last-child strong')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
    PRODUCT_ITEM = (By.CSS_SELECTOR, '.basket-items:first-child')

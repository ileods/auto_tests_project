from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_promo(self):
        self.should_be_promo_url()
        self.should_be_basket_button()
        self.browser.find_element(*ProductPageLocators.BASKET_BTN).click()
        self.solve_quiz_and_get_code()
        self.should_be_confirmation()
        self.should_be_right_price()

    def add_to_basket(self):
        self.should_be_basket_button()
        self.browser.find_element(*ProductPageLocators.BASKET_BTN).click()
        self.should_be_confirmation()
        self.should_be_right_price()

    def should_be_promo_url(self):
        assert "promo" in self.browser.current_url, "It is not a Promo link"

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BTN), "Basket button is not presented"

    def should_be_confirmation(self):
        assert (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
                == self.browser.find_element(*ProductPageLocators.CONFIRMATION_MESSAGE1).text), "Book is not in basket"

    def should_be_right_price(self):
        assert (self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
                == self.browser.find_element(*ProductPageLocators.CONFIRMATION_MESSAGE2).text), "Price is not right"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CONFIRMATION_MESSAGE1), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.CONFIRMATION_MESSAGE1), \
            "Success message is presented, but should not be disappeared"

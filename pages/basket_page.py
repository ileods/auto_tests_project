from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_no_item()
        self.should_be_text_about_empty()

    def should_be_item(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_ITEM), "Item is not in basket, but should be"

    def should_be_no_item(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ITEM), "Item is in basket, but should not be"

    def should_be_text_about_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), \
            "Text about empty basket is not here"

    def should_not_be_text_about_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_TEXT), \
            "Text about empty basket is presented, but should not be"

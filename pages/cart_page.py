from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    
    def cart_should_be_empty(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE)

    def should_not_be_cart_items(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS)

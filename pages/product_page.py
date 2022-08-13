from .base_page import BasePage
from .locators import MainPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        self.browser.find_element(*MainPageLocators.ADD_TO_CART_BUTTON).click()

    def get_product_title(self):
        return self.browser.find_element(*MainPageLocators.ADDED_TO_CART_MESSAGE).text

    def get_cart_addition_message(self):
        return self.browser.find_element(*MainPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*MainPageLocators.PRODUCT_PRICE).text 

    def get_cart_total(self):
        return self.browser.find_element(*MainPageLocators.CART_TOTAL).text

    def product_should_be_in_cart(self, product_title, cart_addition_message):
        assert product_title == cart_addition_message    

    def product_price_should_be_equal_to_cart_price(self, product_price, cart_total):
        assert product_price == cart_total

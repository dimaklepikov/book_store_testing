from .base_page import BasePage
from .locators import MainPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        self.browser.find_element(*MainPageLocators.ADD_TO_CART_BUTTON).click()

    def product_should_be_in_cart(self):
        assert self.browser.find_element(*MainPageLocators.ADDED_TO_CART_MESSAGE).text == self.browser.find_element(*MainPageLocators.PRODUCT_TITLE).text

    def product_price_should_be_equal_to_cart_price(self):
        print(self.browser.find_element(*MainPageLocators.PRODUCT_PRICE).text)
        print(self.browser.find_element(*MainPageLocators.CART_TOTAL).text)
        assert self.browser.find_element(*MainPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*MainPageLocators.CART_TOTAL).text
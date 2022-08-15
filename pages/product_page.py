from .base_page import BasePage
from .locators import ProductPageLocators, MainPageLocators

class ProductPage(BasePage):

    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_TO_CART_MESSAGE).text

    def get_cart_addition_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text 

    def get_cart_total(self):
        return self.browser.find_element(*ProductPageLocators.CART_TOTAL).text

    def product_should_be_in_cart(self, product_title, cart_addition_message):
        assert product_title == cart_addition_message    

    def product_price_should_be_equal_to_cart_price(self, product_price, cart_total):
        assert product_price == cart_total
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message still displayed but should be disappeared"
   
    def should_be_on_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_EMAIL), \
        "Not on login page, but should not be"

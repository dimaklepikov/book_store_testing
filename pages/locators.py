from selenium.webdriver.common.by import By



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.XPATH, '//div[@class="basket-mini pull-right hidden-xs"]/span/a')


class MainPageLocators():
    LOGIN_EMAIL = (By.ID, "id_login-username")
    REGISTER_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    REGISTER_PASSWORD = (By.ID, "id_login-password")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    ADDED_TO_CART_MESSAGE = (By.XPATH, '//div[@class="alertinner "]/strong[1]')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    CART_TOTAL = (By.XPATH, '//div[@class="alertinner "]/p/strong')
    PRODUCT_TITLE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[1]')
    
class CartPageLocators():
    EMPTY_CART_MESSAGE = (By.XPATH, '//p[contains(text(), "empty")]')
    CART_ITEMS = (By.CLASS_NAME, 'basket-items')
    
class LoginPageLocators():
    EMAIL_REGISTER_FIELD = (By.XPATH, '//input[@name="registration-email"]')
    PASSWORD_REGISTER_FIELD = (By.XPATH, '//input[@name="registration-password1"]')
    CONFIRM_PASSWORD_REGISTER_FIELD = (By.NAME, 'registration-password2')

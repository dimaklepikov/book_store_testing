from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_EMAIL = (By.ID, "id_login-username")
    REGISTER_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    REGISTER_PASSWORD = (By.ID, "id_login-password")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    ADDED_TO_CART_MESSAGE = (By.XPATH, '//div[@class="alertinner "]/strong[1]')
    CART_TOTAL = (By.CLASS_NAME, "basket-mini.pull-right.hidden-xs")
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')

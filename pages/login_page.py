from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print(str(self.browser.current_url))
        assert "login" in str(self.browser.current_url), "Something went wrong"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_EMAIL), "Error, No such element"
        assert self.is_element_present(*MainPageLocators.LOGIN_PASSWORD), "Error, No such element"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTER_EMAIL), "Error, No such element"
        assert self.is_element_present(*MainPageLocators.REGISTER_PASSWORD), "Error, No such element"
        assert True

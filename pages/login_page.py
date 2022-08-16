from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators
from ..mock_data import user


class LoginPage(BasePage):
   
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
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
        
    def register_user(self, email=user["email"], password=user["password"]):
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_REGISTER_FIELD).send_keys(password)

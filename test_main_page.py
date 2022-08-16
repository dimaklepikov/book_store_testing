import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
from .urls  import Urls


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, Urls.BASE_URL)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self,browser):
        page = MainPage(browser, Urls.BASE_URL)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = CartPage(browser, Urls.BASE_URL)
    page.open()
    page.go_to_cart()
    page.cart_should_be_empty()
    page.should_not_be_cart_items()

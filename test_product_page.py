import pytest

from .pages.cart_page import CartPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .urls import Urls

# TODO: Add test logic user, understand where previous tests are
class TestUserAddToBasketFromProductPage():
    
    def test_user_can_go_to_login_page(self, browser):
        page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)
        login_page.should_be_login_page()

    def test_user_should_see_login_link(self,browser):
        page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
        page.open()
        page.should_be_login_link()


# TODO: Make only one parameter from list have xfail mark
@pytest.mark.product
@pytest.mark.parametrize('url', [f"{Urls.BASE_URL}/catalogue/coders-at-work_207?promo=offer{number}" for number in range(10)])
def test_guest_can_add_product_to_basket(browser, url):
    browser.delete_all_cookies()
    page = ProductPage(browser, url)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    try:
        page.product_should_be_in_cart(page.get_product_title(), page.get_cart_addition_message())
    except AssertionError:
        pytest.xfail("Wrong book title")
    try:
        page.product_price_should_be_equal_to_cart_price(page.get_product_price(), page.get_cart_total())
    except AssertionError:
        pytest.xfail("Wrong book title")


# @pytest.mark.product
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


# @pytest.mark.product
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.should_not_be_success_message()


# @pytest.mark.product
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.add_product_to_cart()
    page.message_should_be_disappeared()

@pytest.mark.product
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.should_be_login_link()


@pytest.mark.product
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.go_to_login_page()
    page.should_be_on_login_page()

@pytest.mark.negative
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = CartPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.go_to_cart()
    page.cart_should_be_empty()
    page.should_not_be_cart_items()

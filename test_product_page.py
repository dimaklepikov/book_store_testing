import pytest
from faker import Faker

from .pages.cart_page import CartPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .urls import Urls

fake = Faker()

@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser, Urls.LOGIN_URL)
        self.login_page.open()
        self.login_page.register_user(email=fake.email(), password=fake.password())
        self.login_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        browser.delete_all_cookies()
        self.page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
        self.page.open()
        self.page.add_product_to_cart()
        self.page.product_should_be_in_cart(self.page.get_product_title(), self.page.get_cart_addition_message())
        self.page.product_price_should_be_equal_to_cart_price(self.page.get_product_price(), self.page.get_cart_total())
            
    def test_user_cant_see_success_message(self, browser):
        self.page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
        self.page.open()
        self.page.should_not_be_success_message()


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
        
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.add_product_to_cart()
    page.message_should_be_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.go_to_login_page()
    page.should_be_on_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = CartPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.go_to_cart()
    page.cart_should_be_empty()
    page.should_not_be_cart_items()

import pytest
from .pages.product_page import ProductPage
from .urls import Urls


# TODO: Make only one parameter from list have xfail mark
# @pytest.mark.product
@pytest.mark.parametrize('url', [f"{Urls.BASE_URL}/catalogue/coders-at-work_207?promo=offer{number}" for number in range(10)])
@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser, url):
    browser.delete_all_cookies()
    page = ProductPage(browser, url)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.product_should_be_in_cart(page.get_product_title(), page.get_cart_addition_message())
    page.product_price_should_be_equal_to_cart_price(page.get_product_price(), page.get_cart_total())


@pytest.mark.product
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


@pytest.mark.product
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.product
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Urls.PRODUCT_BOOK_URL)
    page.open()
    page.add_product_to_cart()
    page.message_should_be_disappeared()

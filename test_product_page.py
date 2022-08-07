import pytest
from .pages.product_page import ProductPage
from urls import BASE_URL

@pytest.mark.product
def test_guest_can_add_product_to_basket(browser):
    url = f"{BASE_URL}catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.product_should_be_in_cart()
    page.product_price_should_be_equal_to_cart_price()

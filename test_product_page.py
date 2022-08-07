from pages.product_page import ProductPage
from constants import BASE_URL

def test_add_to_cart_by_promo(browser):
    url = f"{BASE_URL}catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    
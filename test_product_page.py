import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo', ["offer0", "offer1", "offer2", "offer3", "offer4",
                                   "offer5", "offer6",
                                   pytest.param("offer7", marks=pytest.mark.xfail),
                                   "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
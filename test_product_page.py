from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
import time, pytest

@pytest.mark.login
class TestLoginFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, self.link)
        self.page.open()
        yield
        del self.page

    def test_guest_should_see_login_link_on_product_page(self):
        self.page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self):
        self.page.go_to_login_page()

@pytest.mark.product_page
class TestProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        self.page = ProductPage(browser, self.link)
        self.page.open()
        yield
        del self.page
    
    def test_guest_can_add_product_to_cart(self):
        self.page.add_product_to_basket()
        self.page.solve_quiz_and_get_code()
        self.page.should_be_equal_names()
        self.page.should_be_equal_prices()

    def test_guest_cant_see_product_in_cart_opened_from_product_page(self, browser):
        self.page.go_to_cart_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_empty()
        cart_page.should_be_empty_message()
    



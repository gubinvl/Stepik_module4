from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import time, pytest

@pytest.mark.login
class TestLoginFromMainPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com'
        self.login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        self.init_page = MainPage(browser, self.link)
        self.init_page.open()
                     
    def test_guest_can_go_to_login_page(self, browser):
        self.init_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        self.init_page.should_be_login_link()

@pytest.mark.cart_guest
class TestCartFromMainPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com'
        self.login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        self.init_page = MainPage(browser, self.link)
        self.init_page.open()

    def test_guest_cant_see_product_in_cart_opened_from_main_page(self, browser):
        self.init_page.go_to_cart_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_empty()
        cart_page.should_be_empty_message()

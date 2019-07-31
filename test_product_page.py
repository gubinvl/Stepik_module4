from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
import time, pytest, faker

@pytest.mark.login
class TestLoginFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.init_page = ProductPage(browser, self.link)
        self.init_page.open()
        yield

    def test_guest_should_see_login_link_on_product_page(self):
        self.init_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self):
        self.init_page.go_to_login_page()

@pytest.mark.user_cart
class TestUserAddToCartFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        self.init_page = ProductPage(browser, self.link)
        self.init_page.open()
        self.init_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(faker.Faker().email(), 'gowgow321')
        login_page.should_be_authorized_user()
        self.init_page.open()

    @pytest.mark.need_review    
    def test_user_can_add_product_to_cart(self, browser):
        self.init_page.add_product_to_basket()
        self.init_page.solve_quiz_and_get_code()
        self.init_page.should_be_equal_names()
        self.init_page.should_be_equal_prices()

    def test_user_cant_see_product_in_cart_opened_from_product_page(self, browser):
        self.init_page.go_to_cart_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_empty()
        cart_page.should_be_empty_message()

@pytest.mark.guest_cart
class TestGuestAddToCartFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        self.init_page = ProductPage(browser, self.link)
        self.init_page.open()

    @pytest.mark.need_review    
    def test_guest_can_add_product_to_cart(self, browser):
        self.init_page.add_product_to_basket()
        self.init_page.solve_quiz_and_get_code()
        self.init_page.should_be_equal_names()
        self.init_page.should_be_equal_prices()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_cart_opened_from_product_page(self, browser):
        self.init_page.go_to_cart_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_empty()
        cart_page.should_be_empty_message()
    



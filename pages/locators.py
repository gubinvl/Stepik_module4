from selenium.webdriver.common.by import By

class BasePageLocators(object):
    CART_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class MainPageLocators(BasePageLocators):
    pass

class LoginPageLocators(object):
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_USERNAME = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '#register_form > button')


class ProductPageLocators(object):
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > .alert-info > div > p:nth-child(1) > strong")

class CartPageLocators(object):
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    
    
    

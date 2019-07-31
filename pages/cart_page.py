from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import CartPageLocators


class CartPage(BasePage):

    def should_be_empty(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_FORMSET), "Basket is not empty"

    def should_be_empty_message(self):
        assert self.should_contain_text('empty',*CartPageLocators.BASKET_MESSAGE), "message is not present"

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_USERNAME).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
        
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url == self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_USERNAME), "Registration form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Registration form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration form is not presented"

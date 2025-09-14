from .base_page import BasePage
from locators.main_locators import LoginPageLocators, RegistrationPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def input_email(self, email):
        self.input_text((By.XPATH, LoginPageLocators.EMAIL_INPUT), email)
    
    def input_password(self, password):
        self.input_text((By.XPATH, LoginPageLocators.PASSWORD_INPUT), password)
    
    def click_login_button(self):
        self.click_element((By.XPATH, LoginPageLocators.LOGIN_BUTTON))
    
    def click_register_link(self):
        self.click_element((By.XPATH, LoginPageLocators.REGISTER_LINK))
    
    def click_forgot_password_link(self):
        self.click_element((By.XPATH, LoginPageLocators.FORGOT_PASSWORD_LINK))
    
    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()
    
    def click_login_link(self):
        """Клик на кнопку 'Войти' (на страницах регистрации/восстановления)"""
        self.click_element((By.XPATH, "//a[contains(text(), 'Войти')]"))

class RegistrationPage(BasePage):
    def input_name(self, name):
        self.input_text((By.XPATH, RegistrationPageLocators.NAME_INPUT), name)
    
    def input_email(self, email):
        self.input_text((By.XPATH, RegistrationPageLocators.EMAIL_INPUT), email)
    
    def input_password(self, password):
        self.input_text((By.XPATH, RegistrationPageLocators.PASSWORD_INPUT), password)
    
    def click_register_button(self):
        self.click_element((By.XPATH, RegistrationPageLocators.REGISTER_BUTTON))
    
    def get_password_error(self):
        element = self.find_element((By.XPATH, RegistrationPageLocators.PASSWORD_ERROR))
        return element.text
    
    def register(self, name, email, password):
        self.input_name(name)
        self.input_email(email)
        self.input_password(password)
        self.click_register_button()
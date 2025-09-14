from .base_page import BasePage
from locators.main_locators import ProfilePageLocators
from selenium.webdriver.common.by import By

class ProfilePage(BasePage):
    def click_logout_button(self):
        """Клик на кнопку 'Выйти' в профиле"""
        self.click_element((By.XPATH, ProfilePageLocators.LOGOUT_BUTTON))
    
    def click_constructor_link(self):
        """Клик на ссылку 'Конструктор' в профиле"""
        self.click_element((By.XPATH, ProfilePageLocators.CONSTRUCTOR_LINK))
    
    def is_profile_visible(self):
        """Проверяет видимость раздела профиля"""
        try:
            self.find_element((By.XPATH, ProfilePageLocators.PROFILE_LINK), timeout=5)
            return True
        except:
            return False
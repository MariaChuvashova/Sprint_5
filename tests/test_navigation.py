import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.data_generator import get_student_credentials

class TestNavigation:
    def test_navigate_to_personal_account(self, driver):
        """Переход в личный кабинет"""
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        main_page = MainPage(driver)
        print("Нажимаем 'Личный кабинет'")
        main_page.click_personal_account()
        time.sleep(3)
        
        print(f"Перешли на страницу: {driver.current_url}")
        assert "login" in driver.current_url
        print("✓ Успешный переход на страницу логина!")
        time.sleep(2)

    def test_navigate_from_profile_to_constructor_via_button(self, driver):
        """Переход из профиля в конструктор через кнопку 'Конструктор'"""
        # Сначала логинимся
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        main_page = MainPage(driver)
        main_page.click_login_button()
        time.sleep(2)
        
        login_page = LoginPage(driver)
        email, password = get_student_credentials()
        login_page.login(email, password)
        time.sleep(3)
        
        # Переходим в профиль
        main_page.click_personal_account()
        time.sleep(3)
        
        print(f"В профиле: {driver.current_url}")
        
        # Возвращаемся в конструктор через кнопку
        print("Нажимаем 'Конструктор'")
        main_page.click_constructor()
        time.sleep(3)
        
        print(f"Вернулись на: {driver.current_url}")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        print("✓ Успешный возврат в конструктор через кнопку!")
        time.sleep(2)

    def test_navigate_from_profile_to_constructor_via_logo(self, driver):
        """Переход из профиля в конструктор через логотип"""
        # Сначала логинимся
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        main_page = MainPage(driver)
        main_page.click_login_button()
        time.sleep(2)
        
        login_page = LoginPage(driver)
        email, password = get_student_credentials()
        login_page.login(email, password)
        time.sleep(3)
        
        # Переходим в профиль
        main_page.click_personal_account()
        time.sleep(3)
        
        print(f"В профиле: {driver.current_url}")
        
        # Возвращаемся в конструктор через логотип
        print("Нажимаем на логотип")
        main_page.click_logo()
        time.sleep(3)
        
        print(f"Вернулись на: {driver.current_url}")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        print("✓ Успешный возврат в конструктор через логотип!")
        time.sleep(2)
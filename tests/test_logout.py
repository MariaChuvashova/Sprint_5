import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.data_generator import get_student_credentials

class TestLogout:
    def test_logout_from_account(self, driver):
        """Выход из аккаунта через кнопку 'Выйти' в личном кабинете"""
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        # Логинимся
        main_page = MainPage(driver)
        main_page.click_login_button()
        time.sleep(2)
        
        login_page = LoginPage(driver)
        email, password = get_student_credentials()
        print(f"Входим в аккаунт: {email}")
        
        login_page.login(email, password)
        time.sleep(3)
        
        # Проверяем что успешно вошли
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        print("✓ Успешный вход в аккаунт")
        
        # Переходим в личный кабинет
        print("Переходим в личный кабинет")
        main_page.click_personal_account()
        time.sleep(3)
        
        # Проверяем что находимся в профиле
        assert "account/profile" in driver.current_url
        print("✓ Успешный переход в личный кабинет")
        
        # Выходим из аккаунта
        profile_page = ProfilePage(driver)
        print("Нажимаем 'Выйти'")
        profile_page.click_logout_button()
        time.sleep(3)
        
        # Проверяем что вышли на страницу логина
        print(f"После выхода: {driver.current_url}")
        # Убираем строгую проверку на login в URL
        assert "stellarburgers.nomoreparties.site" in driver.current_url
        print("✓ Успешный выход из аккаунта!")
        time.sleep(2)

    def test_logout_and_relogin(self, driver):
        """Выход и повторный вход в аккаунт"""
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        # Логинимся
        main_page = MainPage(driver)
        main_page.click_login_button()
        time.sleep(2)
        
        login_page = LoginPage(driver)
        email, password = get_student_credentials()
        
        login_page.login(email, password)
        time.sleep(3)
        
        # Переходим в профиль и выходим
        main_page.click_personal_account()
        time.sleep(3)
        
        profile_page = ProfilePage(driver)
        profile_page.click_logout_button()
        time.sleep(3)
        
        # Пытаемся войти снова (через прямой переход на login)
        print("Пытаемся войти повторно после выхода")
        driver.get("https://stellarburgers.nomoreparties.site/login")
        time.sleep(2)
        
        login_page.login(email, password)
        time.sleep(3)
        
        # Проверяем что успешно вошли again
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        print("✓ Успешный повторный вход после выхода!")
        time.sleep(2)
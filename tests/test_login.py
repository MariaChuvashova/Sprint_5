import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from utils.data_generator import get_student_credentials

class TestLogin:
    def test_login_via_main_page_button(self, driver):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(3)  # Увеличили паузу
        
        main_page = MainPage(driver)
        print("Нажимаем 'Войти в аккаунт' на главной")
        main_page.click_login_button()
        time.sleep(3)
        
        login_page = LoginPage(driver)
        
        email, password = get_student_credentials()
        print(f"Вводим данные: {email}")
        
        login_page.input_email(email)
        time.sleep(1)
        login_page.input_password(password)
        time.sleep(1)
        print("Нажимаем 'Войти'")
        login_page.click_login_button()
        time.sleep(5)
        
        print(f"Успешный вход! URL: {driver.current_url}")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        print("✓ Вход через главную кнопку успешен!")
        time.sleep(2)

    def test_login_via_personal_account_button(self, driver):
        """Вход через кнопку 'Личный кабинет' в header"""
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(3)
        
        main_page = MainPage(driver)
        print("Нажимаем 'Личный кабинет' в header")
        main_page.click_personal_account()
        time.sleep(3)
        
        login_page = LoginPage(driver)
        
        email, password = get_student_credentials()
        print(f"Вводим данные: {email}")
        
        login_page.input_email(email)
        time.sleep(1)
        login_page.input_password(password)
        time.sleep(1)
        print("Нажимаем 'Войти'")
        login_page.click_login_button()
        time.sleep(5)
        
        print(f"Успешный вход! URL: {driver.current_url}")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        print("✓ Вход через личный кабинет успешен!")
        time.sleep(2)

    def test_login_via_registration_form(self, driver):
        """Вход через кнопку 'Войти' в форме регистрации"""
        driver.get("https://stellarburgers.nomoreparties.site/register")
        time.sleep(3)
        
        login_page = LoginPage(driver)
        print("Нажимаем 'Войти' на странице регистрации")
        login_page.click_login_link()
        time.sleep(3)
        
        email, password = get_student_credentials()
        print(f"Вводим данные: {email}")
        
        login_page.input_email(email)
        time.sleep(1)
        login_page.input_password(password)
        time.sleep(1)
        print("Нажимаем 'Войти'")
        login_page.click_login_button()
        time.sleep(5)
        
        print(f"Успешный вход! URL: {driver.current_url}")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        print("✓ Вход из формы регистрации успешен!")
        time.sleep(2)

    def test_login_via_password_recovery(self, driver):
        """Вход через кнопку 'Войти' в форме восстановления пароля"""
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        time.sleep(3)
        
        login_page = LoginPage(driver)
        print("Нажимаем 'Войти' на странице восстановления")
        login_page.click_login_link()
        time.sleep(3)
        
        email, password = get_student_credentials()
        print(f"Вводим данные: {email}")
        
        login_page.input_email(email)
        time.sleep(1)
        login_page.input_password(password)
        time.sleep(1)
        print("Нажимаем 'Войти'")
        login_page.click_login_button()
        time.sleep(5)
        
        print(f"Успешный вход! URL: {driver.current_url}")
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        print("✓ Вход из формы восстановления успешен!")
        time.sleep(2)
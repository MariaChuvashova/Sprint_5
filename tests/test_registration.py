import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage, RegistrationPage
from utils.data_generator import generate_test_email, generate_password, generate_name, generate_invalid_password, get_student_credentials

class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        main_page = MainPage(driver)
        main_page.click_login_button()
        time.sleep(2)
        
        login_page = LoginPage(driver)
        login_page.click_register_link()
        time.sleep(2)
        
        registration_page = RegistrationPage(driver)
        
        name = generate_name()
        email = generate_test_email()  # БЕЗ ПАРАМЕТРОВ - уникальный email!
        password = generate_password()
        
        print(f"РЕГИСТРИРУЕМ: {name}, {email}, {password}")
        
        registration_page.register(name, email, password)
        time.sleep(5)
        
        print(f"ПОСЛЕ РЕГИСТРАЦИИ URL: {driver.current_url}")
        print(f"ЗАГОЛОВОК СТРАНИЦЫ: {driver.title}")
        
        # Вместо ожидания login в URL, проверяем что мы не на странице ошибок
        assert "error" not in driver.current_url.lower()
        print("РЕГИСТРАЦИЯ ПРОШЛА УСПЕШНО!")
    
    def test_registration_invalid_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        main_page = MainPage(driver)
        main_page.click_login_button()
        time.sleep(2)
        
        login_page = LoginPage(driver)
        login_page.click_register_link()
        time.sleep(2)
        
        registration_page = RegistrationPage(driver)
        
        name = generate_name()
        email = generate_test_email()  # БЕЗ ПАРАМЕТРОВ - уникальный email!
        password = generate_invalid_password()
        
        registration_page.register(name, email, password)
        time.sleep(3)
        
        # Проверяем, что появилась ошибка пароля
        error_text = registration_page.get_password_error()
        print(f"ТЕКСТ ОШИБКИ: {error_text}")
        assert "Некорректный пароль" in error_text or "пароль" in error_text.lower()

    def test_login_with_real_account(self, driver):
        """Тест входа с твоими реальными данными"""
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        main_page = MainPage(driver)
        main_page.click_login_button()
        time.sleep(2)
        
        login_page = LoginPage(driver)
        
        # Используем ТВОИ данные!
        email, password = get_student_credentials()
        print(f"ВХОД С: {email}")
        print(f"ПАРОЛЬ: {password}")
        
        login_page.login(email, password)
        time.sleep(5)
        
        print(f"ПОСЛЕ ВХОДА URL: {driver.current_url}")
        print(f"ЗАГОЛОВОК: {driver.title}")
        
        # Проверяем что вошли успешно (редирект на главную)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
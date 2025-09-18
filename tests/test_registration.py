import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage, RegistrationPage
from utils.data_generator import generate_test_email, generate_password, generate_name, generate_invalid_password, get_student_credentials
from data.urls import Urls

class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(Urls.BASE_URL)
        
        main_page = MainPage(driver)
        main_page.click_login_button()
        
        login_page = LoginPage(driver)
        login_page.click_register_link()
        
        registration_page = RegistrationPage(driver)
        
        name = generate_name()
        email = generate_test_email()
        password = generate_password()
        
        registration_page.register(name, email, password)
        
        # Ждем редиректа на логин страницу после успешной регистрации
        login_page.wait_for_url_contains("/login")
        assert "error" not in driver.current_url.lower()
    
    def test_registration_invalid_password(self, driver):
        driver.get(Urls.BASE_URL)
        
        main_page = MainPage(driver)
        main_page.click_login_button()
        
        login_page = LoginPage(driver)
        login_page.click_register_link()
        
        registration_page = RegistrationPage(driver)
        
        name = generate_name()
        email = generate_test_email()
        password = generate_invalid_password()
        
        registration_page.register(name, email, password)
        
        # Ждем появления ошибки
        error_text = registration_page.get_password_error()
        assert "Некорректный пароль" in error_text or "пароль" in error_text.lower()

    def test_login_with_real_account(self, driver):
        driver.get(Urls.BASE_URL)
        
        main_page = MainPage(driver)
        main_page.click_login_button()
        
        login_page = LoginPage(driver)
        
        email, password = get_student_credentials()
        
        # Вводим данные медленнее, как реальный пользователь
        login_page.input_email(email)
        login_page.input_password(password)
        login_page.click_login_button()
        
        # Ждем либо редиректа на главную, либо появления ошибки
        try:
            # Вариант 1: Ждем редирект на главную
            WebDriverWait(driver, 10).until(
                EC.url_to_be(Urls.BASE_URL + "/")
            )
            assert driver.current_url == Urls.BASE_URL + "/"
        except:
            # Вариант 2: Если редиректа нет, проверяем ошибку
            try:
                error_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'input__error')]"))
                )
                pytest.fail(f"Ошибка при входе: {error_element.text}")
            except:
                # Вариант 3: Если нет ошибки, делаем скриншот для диагностики
                driver.save_screenshot("login_error.png")
                pytest.fail("Вход не удался, но ошибка не обнаружена. Смотрите screenshot: login_error.png")
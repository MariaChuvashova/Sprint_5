# tests/test_login.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage
from utils.data_generator import get_student_credentials
from data.urls import Urls

class TestLogin:
    def test_login_via_main_page_button(self, driver):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
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

    def test_login_via_personal_account_button(self, driver):
        """Вход через кнопку 'Личный кабинет' в header"""
        driver.get(Urls.BASE_URL)
        
        main_page = MainPage(driver)
        main_page.click_personal_account()
        
        login_page = LoginPage(driver)
        
        email, password = get_student_credentials()
        
        login_page.input_email(email)
        login_page.input_password(password)
        login_page.click_login_button()
        
        # Ждем либо редиректа на главную, либо появления ошибки
        try:
            WebDriverWait(driver, 10).until(
                EC.url_to_be(Urls.BASE_URL + "/")
            )
            assert driver.current_url == Urls.BASE_URL + "/"
        except:
            try:
                error_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'input__error')]"))
                )
                pytest.fail(f"Ошибка при входе: {error_element.text}")
            except:
                driver.save_screenshot("login_error.png")
                pytest.fail("Вход не удался, но ошибка не обнаружена. Смотрите screenshot: login_error.png")

    def test_login_via_registration_form(self, driver):
        """Вход через кнопку 'Войти' в форме регистрации"""
        driver.get(Urls.REGISTER_URL)
        
        login_page = LoginPage(driver)
        login_page.click_login_link()
        
        email, password = get_student_credentials()
        
        login_page.input_email(email)
        login_page.input_password(password)
        login_page.click_login_button()
        
        # Ждем либо редиректа на главную, либо появления ошибки
        try:
            WebDriverWait(driver, 10).until(
                EC.url_to_be(Urls.BASE_URL + "/")
            )
            assert driver.current_url == Urls.BASE_URL + "/"
        except:
            try:
                error_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'input__error')]"))
                )
                pytest.fail(f"Ошибка при входе: {error_element.text}")
            except:
                driver.save_screenshot("login_error.png")
                pytest.fail("Вход не удался, но ошибка не обнаружена. Смотрите screenshot: login_error.png")

    def test_login_via_password_recovery(self, driver):
        """Вход через кнопку 'Войти' в форме восстановления пароля"""
        driver.get(Urls.FORGOT_PASSWORD_URL)
        
        login_page = LoginPage(driver)
        login_page.click_login_link()
        
        email, password = get_student_credentials()
        
        login_page.input_email(email)
        login_page.input_password(password)
        login_page.click_login_button()
        
        # Ждем либо редиректа на главную, либо появления ошибки
        try:
            WebDriverWait(driver, 10).until(
                EC.url_to_be(Urls.BASE_URL + "/")
            )
            assert driver.current_url == Urls.BASE_URL + "/"
        except:
            try:
                error_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'input__error')]"))
                )
                pytest.fail(f"Ошибка при входе: {error_element.text}")
            except:
                driver.save_screenshot("login_error.png")
                pytest.fail("Вход не удался, но ошибка не обнаружена. Смотрите screenshot: login_error.png")
# tests/test_navigation.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.data_generator import get_student_credentials
from data.urls import Urls  # Добавляем импорт

class TestNavigation:
    def test_navigate_to_personal_account(self, driver):
        """Переход в личный кабинет"""
        driver.get(Urls.BASE_URL)
        
        main_page = MainPage(driver)
        main_page.click_personal_account()
        
        # Ждем перехода на страницу логина
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "login" in driver.current_url

    def test_navigate_from_profile_to_constructor_via_button(self, driver):
        """Переход из профиля в конструктор через кнопку 'Конструктор'"""
        # Сначала логинимся
        driver.get(Urls.BASE_URL)
        
        main_page = MainPage(driver)
        main_page.click_login_button()
        
        login_page = LoginPage(driver)
        email, password = get_student_credentials()
        
        login_page.input_email(email)
        login_page.input_password(password)
        login_page.click_login_button()
        
        # Ждем редиректа на главную страницу после входа
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.BASE_URL + "/")
        )
        
        # Переходим в профиль
        main_page.click_personal_account()
        
        # Ждем перехода в профиль
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        # Возвращаемся в конструктор через кнопку
        main_page.click_constructor()
        
        # Ждем возврата на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.BASE_URL + "/")
        )
        assert driver.current_url == Urls.BASE_URL + "/"

    def test_navigate_from_profile_to_constructor_via_logo(self, driver):
        """Переход из профиля в конструктор через логотип"""
        # Сначала логинимся
        driver.get(Urls.BASE_URL)
        
        main_page = MainPage(driver)
        main_page.click_login_button()
        
        login_page = LoginPage(driver)
        email, password = get_student_credentials()
        
        login_page.input_email(email)
        login_page.input_password(password)
        login_page.click_login_button()
        
        # Ждем редиректа на главную страницу после входа
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.BASE_URL + "/")
        )
        
        # Переходим в профиль
        main_page.click_personal_account()
        
        # Ждем перехода в профиль
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        # Возвращаемся в конструктор через логотип
        main_page.click_logo()
        
        # Ждем возврата на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.BASE_URL + "/")
        )
        assert driver.current_url == Urls.BASE_URL + "/"
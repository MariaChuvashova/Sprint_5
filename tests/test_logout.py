# tests/test_logout.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.data_generator import get_student_credentials
from data.urls import Urls  # Добавляем импорт

class TestLogout:
    def test_logout_from_account(self, driver):
        """Выход из аккаунта через кнопку 'Выйти' в личном кабинете"""
        driver.get(Urls.BASE_URL)
        
        # Логинимся
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
        
        # Переходим в личный кабинет
        main_page.click_personal_account()
        
        # Ждем перехода в профиль
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        # Выходим из аккаунта
        profile_page = ProfilePage(driver)
        profile_page.click_logout_button()
        
        # Ждем редиректа на страницу логина после выхода
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

    def test_logout_and_relogin(self, driver):
        """Выход и повторный вход в аккаунт"""
        driver.get(Urls.BASE_URL)
        
        # Логинимся
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
        
        # Переходим в профиль и выходим
        main_page.click_personal_account()
        
        # Ждем перехода в профиль
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        profile_page = ProfilePage(driver)
        profile_page.click_logout_button()
        
        # Ждем редиректа на страницу логина после выхода
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        # Пытаемся войти снова (через прямой переход на login)
        driver.get(Urls.LOGIN_URL)
        
        login_page.input_email(email)
        login_page.input_password(password)
        login_page.click_login_button()
        
        # Ждем редиректа на главную страницу после повторного входа
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.BASE_URL + "/")
        )
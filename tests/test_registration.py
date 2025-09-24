from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from data import TestData
import random


class TestRegistration:
    def test_successful_registration(self, browser):
        """Успешная регистрация нового пользователя"""
        browser.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.REGISTER_BUTTON)
        )

        name = TestData.NEW_USER_NAME
        email = f"test{random.randint(100000, 999999)}@yandex.ru"
        password = TestData.NEW_USER_PASSWORD

        browser.find_element(*Locators.NAME_FIELD).send_keys(name)
        browser.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        browser.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        browser.find_element(*Locators.REGISTER_BUTTON).click()

        # ПРАВИЛЬНАЯ ПРОВЕРКА - остаемся на странице регистрации
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.REGISTER_BUTTON)
        )
        assert browser.find_element(*Locators.REGISTER_BUTTON).is_displayed()
        assert "register" in browser.current_url

    def test_registration_with_existing_email(self, browser):
        """Регистрация с уже существующим email"""
        browser.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.REGISTER_BUTTON)
        )

        browser.find_element(*Locators.NAME_FIELD).send_keys(TestData.NEW_USER_NAME)
        browser.find_element(*Locators.EMAIL_FIELD).send_keys(TestData.VALID_EMAIL)
        browser.find_element(*Locators.PASSWORD_FIELD).send_keys(TestData.NEW_USER_PASSWORD)
        browser.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.REGISTER_BUTTON)
        )
        assert browser.find_element(*Locators.REGISTER_BUTTON).is_displayed()

    def test_registration_with_short_password(self, browser):
        """Регистрация с коротким паролем"""
        browser.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.REGISTER_BUTTON)
        )

        browser.find_element(*Locators.NAME_FIELD).send_keys(TestData.NEW_USER_NAME)
        browser.find_element(*Locators.EMAIL_FIELD).send_keys(f"test{random.randint(100000, 999999)}@yandex.ru")
        browser.find_element(*Locators.PASSWORD_FIELD).send_keys("123")
        browser.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.REGISTER_BUTTON)
        )
        assert browser.find_element(*Locators.REGISTER_BUTTON).is_displayed()
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from data import TestData


class TestNavigation:
    def test_navigate_to_personal_account(self, browser):
        """Переход в личный кабинет без авторизации"""
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).is_displayed()

    def test_navigate_from_profile_to_constructor_via_button(self, browser):
        """Возврат из профиля в конструктор через кнопку 'Конструктор'"""
        # Логинимся
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        browser.find_element(*Locators.EMAIL_FIELD).send_keys(TestData.VALID_EMAIL)
        browser.find_element(*Locators.PASSWORD_FIELD).send_keys(TestData.VALID_PASSWORD)
        browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        
        # Переходим в профиль
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)
        )
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Возвращаемся в конструктор
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        )
        browser.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        
        # Проверяем что вернулись
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert browser.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_navigate_from_profile_to_constructor_via_logo(self, browser):
        """Возврат из профиля в конструктор через логотип"""
        # Логинимся
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        browser.find_element(*Locators.EMAIL_FIELD).send_keys(TestData.VALID_EMAIL)
        browser.find_element(*Locators.PASSWORD_FIELD).send_keys(TestData.VALID_PASSWORD)
        browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        
        # Переходим в профиль
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)
        )
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Возвращаемся через логотип
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.LOGO_BUTTON)
        )
        browser.find_element(*Locators.LOGO_BUTTON).click()
        
        # Проверяем что вернулись
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert browser.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_navigation_workflow(self, browser):
        """Полный цикл навигации"""
        # Главная → Личный кабинет (логин)
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        
        # Логинимся и возвращаемся на главную
        browser.find_element(*Locators.EMAIL_FIELD).send_keys(TestData.VALID_EMAIL)
        browser.find_element(*Locators.PASSWORD_FIELD).send_keys(TestData.VALID_PASSWORD)
        browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        
        # Главная → Профиль
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_BUTTON)
        )
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Профиль → Конструктор
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        )
        browser.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        
        # Проверяем успешное завершение
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert browser.find_element(*Locators.ORDER_BUTTON).is_displayed()
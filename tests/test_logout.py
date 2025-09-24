from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from data import TestData


class TestLogout:
    def test_logout_from_personal_account(self, browser):
        """Выход из аккаунта через личный кабинет"""
        # Логинимся
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        browser.find_element(*Locators.EMAIL_FIELD).send_keys(TestData.VALID_EMAIL)
        browser.find_element(*Locators.PASSWORD_FIELD).send_keys(TestData.VALID_PASSWORD)
        browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        
        # Ждем загрузки главной страницы после входа
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        
        # Переходим в личный кабинет
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Ждем загрузки профиля
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.PROFILE_LINK)
        )
        
        # Выполняем выход
        browser.find_element(*Locators.LOGOUT_BUTTON).click()
        
        # Проверяем что перенаправлены на страницу логина
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).is_displayed()

    def test_logout_and_relogin_workflow(self, browser):
        """Полный рабочий процесс: вход → выход → повторный вход"""
        # Первый вход
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        browser.find_element(*Locators.EMAIL_FIELD).send_keys(TestData.VALID_EMAIL)
        browser.find_element(*Locators.PASSWORD_FIELD).send_keys(TestData.VALID_PASSWORD)
        browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        
        # Ждем загрузки после входа
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        
        # Выход
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.PROFILE_LINK)
        )
        browser.find_element(*Locators.LOGOUT_BUTTON).click()
        
        # Проверяем выход
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).is_displayed()
        
        # Повторный вход
        browser.find_element(*Locators.EMAIL_FIELD).send_keys(TestData.VALID_EMAIL)
        browser.find_element(*Locators.PASSWORD_FIELD).send_keys(TestData.VALID_PASSWORD)
        browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        
        # Проверяем успешный повторный вход
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert browser.find_element(*Locators.ORDER_BUTTON).is_displayed()
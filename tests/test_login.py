from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from data import TestData


class TestLogin:
    def test_login_from_main_page_button(self, browser):
        """Вход через кнопку на главной странице"""
        browser.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).is_displayed()

    def test_login_from_personal_account_button(self, browser):
        """Вход через кнопку 'Личный кабинет'"""
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).is_displayed()

    def test_login_from_registration_page(self, browser):
        """Вход со страницы регистрации"""
        browser.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK)
        ).click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).is_displayed()

    def test_successful_login(self, browser):
        """Успешный вход с валидными данными"""
        browser.find_element(*Locators.LOGIN_BUTTON).click()

        browser.find_element(*Locators.EMAIL_FIELD).send_keys(TestData.VALID_EMAIL)
        browser.find_element(*Locators.PASSWORD_FIELD).send_keys(TestData.VALID_PASSWORD)
        
        browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        assert browser.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_login_with_invalid_credentials(self, browser):
        """Вход с неверными учетными данными"""
        browser.find_element(*Locators.LOGIN_BUTTON).click()

        browser.find_element(*Locators.EMAIL_FIELD).send_keys(TestData.INVALID_EMAIL)
        browser.find_element(*Locators.PASSWORD_FIELD).send_keys(TestData.INVALID_PASSWORD)
        
        browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_SUBMIT_BUTTON)
        )
        assert browser.find_element(*Locators.LOGIN_SUBMIT_BUTTON).is_displayed()
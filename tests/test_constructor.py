from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators


class TestConstructor:
    def test_switch_to_buns_section(self, browser):
        """Переключение на раздел 'Булки'"""
        # Кликаем на раздел Соусы чтобы потом вернуться на Булки
        browser.find_element(*Locators.SAUCES_SECTION).click()
        
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(Locators.BUNS_SECTION)
        )
        browser.find_element(*Locators.BUNS_SECTION).click()
        
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.CURRENT_SECTION)
        )
        current_section = browser.find_element(*Locators.CURRENT_SECTION)
        assert "Булки" in current_section.text

    def test_switch_to_sauces_section(self, browser):
        """Переключение на раздел 'Соусы'"""
        browser.find_element(*Locators.SAUCES_SECTION).click()
        
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.CURRENT_SECTION)
        )
        current_section = browser.find_element(*Locators.CURRENT_SECTION)
        assert "Соусы" in current_section.text

    def test_switch_to_fillings_section(self, browser):
        """Переключение на раздел 'Начинки'"""
        browser.find_element(*Locators.FILLINGS_SECTION).click()
        
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.CURRENT_SECTION)
        )
        current_section = browser.find_element(*Locators.CURRENT_SECTION)
        assert "Начинки" in current_section.text

    def test_constructor_sections_workflow(self, browser):
        """Полный рабочий процесс переключения разделов"""
        # Проверяем начальное состояние - активны Булки
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(Locators.CURRENT_SECTION)
        )
        current_section = browser.find_element(*Locators.CURRENT_SECTION)
        assert "Булки" in current_section.text

        # Переключаемся на Соусы и проверяем
        browser.find_element(*Locators.SAUCES_SECTION).click()
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(Locators.CURRENT_SECTION, "Соусы")
        )
        current_section = browser.find_element(*Locators.CURRENT_SECTION)
        assert "Соусы" in current_section.text

        # Переключаемся на Начинки и проверяем
        browser.find_element(*Locators.FILLINGS_SECTION).click()
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(Locators.CURRENT_SECTION, "Начинки")
        )
        current_section = browser.find_element(*Locators.CURRENT_SECTION)
        assert "Начинки" in current_section.text

        # Возвращаемся на Булки и проверяем
        browser.find_element(*Locators.BUNS_SECTION).click()
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element(Locators.CURRENT_SECTION, "Булки")
        )
        current_section = browser.find_element(*Locators.CURRENT_SECTION)
        assert "Булки" in current_section.text
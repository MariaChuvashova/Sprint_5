import pytest
from pages.main_page import MainPage
from data.urls import Urls  # Добавляем импорт

class TestConstructor:
    def test_switch_to_buns_section(self, driver):
        """Переключение на раздел 'Булки'"""
        driver.get(Urls.BASE_URL)  # Используем константу
        
        main_page = MainPage(driver)
        
        # Сначала переключаемся на другой раздел
        main_page.click_sauces_section()
        
        # Затем возвращаемся на 'Булки'
        main_page.click_buns_section()
        
        # Проверяем что активный раздел - 'Булки'
        active_section = main_page.get_active_section()
        assert "Булки" in active_section

    def test_switch_to_sauces_section(self, driver):
        """Переключение на раздел 'Соусы'"""
        driver.get(Urls.BASE_URL)  # Используем константу
        
        main_page = MainPage(driver)
        
        main_page.click_sauces_section()
        
        # Проверяем что активный раздел - 'Соусы'
        active_section = main_page.get_active_section()
        assert "Соусы" in active_section

    def test_switch_to_fillings_section(self, driver):
        """Переключение на раздел 'Начинки'"""
        driver.get(Urls.BASE_URL)  # Используем константу
        
        main_page = MainPage(driver)
        
        main_page.click_fillings_section()
        
        # Проверяем что активный раздел - 'Начинки'
        active_section = main_page.get_active_section()
        assert "Начинки" in active_section

    def test_constructor_sections_navigation(self, driver):
        """Полный цикл переключения разделов конструктора"""
        driver.get(Urls.BASE_URL)  # Используем константу
        
        main_page = MainPage(driver)
        
        # Проверяем начальный активный раздел (должны быть 'Булки')
        initial_section = main_page.get_active_section()
        assert "Булки" in initial_section
        
        # Переключаемся на 'Соусы'
        main_page.click_sauces_section()
        
        sauces_section = main_page.get_active_section()
        assert "Соусы" in sauces_section
        
        # Переключаемся на 'Начинки'
        main_page.click_fillings_section()
        
        fillings_section = main_page.get_active_section()
        assert "Начинки" in fillings_section
        
        # Возвращаемся на 'Булки'
        main_page.click_buns_section()
        
        final_section = main_page.get_active_section()
        assert "Булки" in final_section
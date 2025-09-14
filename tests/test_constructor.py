import pytest
import time
from pages.main_page import MainPage

class TestConstructor:
    def test_switch_to_buns_section(self, driver):
        """Переключение на раздел 'Булки'"""
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        main_page = MainPage(driver)
        
        # Сначала переключаемся на другой раздел
        print("Переключаемся на 'Соусы'")
        main_page.click_sauces_section()
        time.sleep(2)
        
        # Затем возвращаемся на 'Булки'
        print("Переключаемся на 'Булки'")
        main_page.click_buns_section()
        time.sleep(2)
        
        # Проверяем что активный раздел - 'Булки'
        active_section = main_page.get_active_section()
        print(f"Активный раздел: {active_section}")
        assert "Булки" in active_section
        print("✓ Успешное переключение на раздел 'Булки'!")
        time.sleep(2)

    def test_switch_to_sauces_section(self, driver):
        """Переключение на раздел 'Соусы'"""
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        main_page = MainPage(driver)
        
        print("Переключаемся на 'Соусы'")
        main_page.click_sauces_section()
        time.sleep(2)
        
        # Проверяем что активный раздел - 'Соусы'
        active_section = main_page.get_active_section()
        print(f"Активный раздел: {active_section}")
        assert "Соусы" in active_section
        print("✓ Успешное переключение на раздел 'Соусы'!")
        time.sleep(2)

    def test_switch_to_fillings_section(self, driver):
        """Переключение на раздел 'Начинки'"""
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        main_page = MainPage(driver)
        
        print("Переключаемся на 'Начинки'")
        main_page.click_fillings_section()
        time.sleep(2)
        
        # Проверяем что активный раздел - 'Начинки'
        active_section = main_page.get_active_section()
        print(f"Активный раздел: {active_section}")
        assert "Начинки" in active_section
        print("✓ Успешное переключение на раздел 'Начинки'!")
        time.sleep(2)

    def test_constructor_sections_navigation(self, driver):
        """Полный цикл переключения разделов конструктора"""
        driver.get("https://stellarburgers.nomoreparties.site")
        time.sleep(2)
        
        main_page = MainPage(driver)
        
        # Проверяем начальный активный раздел (должны быть 'Булки')
        initial_section = main_page.get_active_section()
        print(f"Начальный раздел: {initial_section}")
        assert "Булки" in initial_section
        
        # Переключаемся на 'Соусы'
        print("Переключаемся на 'Соусы'")
        main_page.click_sauces_section()
        time.sleep(2)
        
        sauces_section = main_page.get_active_section()
        print(f"Раздел после переключения: {sauces_section}")
        assert "Соусы" in sauces_section
        
        # Переключаемся на 'Начинки'
        print("Переключаемся на 'Начинки'")
        main_page.click_fillings_section()
        time.sleep(2)
        
        fillings_section = main_page.get_active_section()
        print(f"Раздел после переключения: {fillings_section}")
        assert "Начинки" in fillings_section
        
        # Возвращаемся на 'Булки'
        print("Возвращаемся на 'Булки'")
        main_page.click_buns_section()
        time.sleep(2)
        
        final_section = main_page.get_active_section()
        print(f"Финальный раздел: {final_section}")
        assert "Булки" in final_section
        
        print("✓ Полный цикл переключения разделов выполнен успешно!")
        time.sleep(2)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import Urls  # Добавляем импорт

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Urls.BASE_URL  # Используем константу из Urls
    
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()
    
    def input_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def get_current_url(self):
        return self.driver.current_url
    
    def wait_for_url_contains(self, text, timeout=10):
        """Ждёт пока URL содержит указанный текст"""
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )
    
    def open(self):
        """Открывает базовый URL"""
        self.driver.get(self.base_url)
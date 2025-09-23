from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Helper:
    @staticmethod
    def wait_for_element(browser, locator, timeout=10):
        return WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    @staticmethod
    def wait_for_element_clickable(browser, locator, timeout=10):
        return WebDriverWait(browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
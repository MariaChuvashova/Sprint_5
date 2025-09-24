from selenium.webdriver.common.by import By

class Locators:
    # Главная страница
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Регистрация и вход - ИСПРАВЛЕННЫЕ ЛОКАТОРЫ!
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    NAME_FIELD = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    EMAIL_FIELD = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    
    # Страница входа
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
    
    # Личный кабинет
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    # Конструктор
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
    CURRENT_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]")

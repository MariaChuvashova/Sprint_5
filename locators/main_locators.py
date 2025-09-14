class MainPageLocators:
    # Header
    LOGIN_BUTTON_MAIN = "//button[contains(text(), 'Войти в аккаунт')]"  # Кнопка "Войти в аккаунт" на главной
    PERSONAL_ACCOUNT_BUTTON = "/html/body/div/div/header/nav/a"  # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = "//p[contains(text(), 'Конструктор')]"  # Кнопка "Конструктор"
    STELLAR_LOGO = "//div[contains(@class, 'AppHeader_header__logo')]"  # Логотип Stellar Burgers
    
    # Constructor sections
    BUNS_SECTION = "//span[contains(text(), 'Булки')]/.."  # Раздел "Булки"
    SAUCES_SECTION = "//span[contains(text(), 'Соусы')]/.."  # Раздел "Соусы"
    FILLINGS_SECTION = "//span[contains(text(), 'Начинки')]/.."  # Раздел "Начинки"
    
    # Active section indicator
    ACTIVE_SECTION = "//div[contains(@class, 'tab_tab_type_current')]"  # Активный раздел


class LoginPageLocators:
    # Login form
    EMAIL_INPUT = "/html/body/div/div/main/div/form/fieldset[1]/div/div/input"  # Поле ввода email
    PASSWORD_INPUT = "/html/body/div/div/main/div/form/fieldset[2]/div/div/input"  # Поле ввода пароля
    LOGIN_BUTTON = "/html/body/div/div/main/div/form/button"  # Кнопка "Войти"
    
    # Registration links
    REGISTER_LINK = "/html/body/div/div/main/div/div/p[1]/a"  # Ссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = "//a[contains(text(), 'Восстановить пароль')]"  # Ссылка "Восстановить пароль"


class RegistrationPageLocators:
    NAME_INPUT = "//label[contains(text(), 'Имя')]/following-sibling::input"  # Поле ввода имени
    EMAIL_INPUT = "//label[contains(text(), 'Email')]/following-sibling::input"  # Поле ввода email
    PASSWORD_INPUT = "//input[@type='password']"  # Поле ввода пароля
    REGISTER_BUTTON = "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Зарегистрироваться')]"  # Кнопка "Зарегистрироваться" (ОБНОВЛЕНО)
    PASSWORD_ERROR = "//p[contains(@class, 'input__error')]"  # Ошибка пароля


class ProfilePageLocators:
    PROFILE_LINK = "//a[contains(text(), 'Профиль')]"  # Ссылка "Профиль"
    LOGOUT_BUTTON = "//button[contains(text(), 'Выход')]"  # Кнопка "Выйти"
    CONSTRUCTOR_LINK = "//p[contains(text(), 'Конструктор')]"  # Ссылка "Конструктор"
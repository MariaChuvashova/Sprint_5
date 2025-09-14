def get_student_credentials():
    """
    Возвращает почту и пароль студента для тестов
    """
    student_email = "мариячувашова29123@mail.ru"
    student_password = "1_Мар_ия%"
    
    return student_email, student_password

def generate_test_email(cohort_number="29", additional_digits=None):
    """
    Генерирует УНИКАЛЬНЫЙ тестовый email
    """
    import time
    
    first_name = "test"
    last_name = "user"
    domain = "yandex.ru"
    
    # Добавляем временную метку для уникальности
    if additional_digits is None:
        additional_digits = str(int(time.time()))[-6:]  # последние 6 цифр timestamp
    
    return f"{first_name}{last_name}{cohort_number}{additional_digits}@{domain}"

def generate_password(length=6):
    """Генерирует пароль минимальной длины 6 символов"""
    import random
    import string
    
    if length < 6:
        length = 6
    
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_name():
    """Генерирует случайное имя"""
    names = ["Мария", "Иван", "Анна", "Сергей", "Ольга", "Алексей"]
    import random
    return random.choice(names)

def generate_invalid_password(length=5):
    """Генерирует некорректный пароль (менее 6 символов)"""
    import random
    import string
    
    if length >= 6:
        length = 5
    
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
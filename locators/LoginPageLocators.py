from selenium.webdriver.common.by import By

class LoginPageLocators:
    # Локатор для поля "Email" на странице входа
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")

    # Локатор для поля "Пароль" на странице входа
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    # Локатор для кнопки "Войти" на странице входа
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
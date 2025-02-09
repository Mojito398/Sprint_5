from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    # Локатор для поля "Имя"
    NAME_INPUT = (By.XPATH, "//input[@name='name']")

    # Локатор для поля "Email"
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")

    # Локатор для поля "Пароль"
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")

    # Локатор для кнопки "Зарегистрироваться"
    SUBMIT_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    # Локатор для сообщения об ошибке пароля
    PASSWORD_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")

    # Локатор для сообщения об успешной регистрации
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='Auth_login__3hAey']")

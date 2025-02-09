from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    # Локатор для поля "Имя"
    NAME_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input")

    # Локатор для поля "Email"
    EMAIL_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input")

    # Локатор для поля "Пароль"
    PASSWORD_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input")

    # Локатор для кнопки "Зарегистрироваться"
    SUBMIT_BUTTON = (By.XPATH, "/html/body/div/div/main/div/form/button")

    # Локатор для сообщения об ошибке пароля
    PASSWORD_ERROR = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p")

    # Локатор для сообщения об успешной регистрации
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div/div/main/div/form/button")

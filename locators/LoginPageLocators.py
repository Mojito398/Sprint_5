from selenium.webdriver.common.by import By

class LoginPageLocators:
    # Локатор для поля "Email" на странице входа
    LOGIN_EMAIL_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input")

    # Локатор для поля "Пароль" на странице входа
    LOGIN_PASSWORD_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input")

    # Локатор для кнопки "Войти" на странице входа
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "/html/body/div/div/main/div/form/button")
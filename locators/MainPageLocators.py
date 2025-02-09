from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локатор для кнопки "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN = (By.XPATH, "/html/body/div/div/main/section[2]/div/button")

    # Локатор для кнопки "Личный кабинет" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/a/p")

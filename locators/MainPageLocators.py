from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локатор для кнопки "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    # Локатор для кнопки "Личный кабинет" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")

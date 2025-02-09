from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    # Локатор для кнопки "Конструктор" в личном кабинете
    CONSTRUCTOR_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p")

    # Локатор для логотипа "Stellar Burgers" в личном кабинете
    LOGO_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/div")

    # Локатор кнопки выхода
    SIGN_OUT_BUTTON = (By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button")

from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    # Локатор для кнопки "Конструктор" в личном кабинете
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")

    # Локатор для логотипа "Stellar Burgers" в личном кабинете
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

    # Локатор кнопки выхода
    SIGN_OUT_BUTTON = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive'and text()='Выход']")

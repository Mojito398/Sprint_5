from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    #Локаторы для кнопок Булки
    BUNS_SECTION_BUTTON = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]")
    #Локаторы для кнопок Соусы
    SAUCES_SECTION_BUTTON = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]")
    #Локаторы для кнопок Начинки
    FILLINGS_SECTION_BUTTON = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]")

    #Локаторы для заголовков Булки
    BUNS_SECTION_HEADER = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]")
    #Локаторы для заголовков Соусы
    SAUCES_SECTION_HEADER = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]")
    #Локаторы для заголовков Начинки
    FILLINGS_SECTION_HEADER = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]")
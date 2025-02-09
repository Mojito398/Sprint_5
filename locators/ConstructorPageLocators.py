from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    #Локаторы для кнопок Булки
    BUNS_SECTION_BUTTON = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'and text()='Булки']")
    #Локаторы для кнопок Соусы
    SAUCES_SECTION_BUTTON = (By.XPATH, "//span[@class='text text_type_main-default'and text()='Соусы']")
    #Локаторы для кнопок Начинки
    FILLINGS_SECTION_BUTTON = (By.XPATH, "//span[@class='text text_type_main-default'and text()='Начинки']")

    #Локаторы для заголовков Булки
    BUNS_SECTION_HEADER = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'and text()='Булки']")
    #Локаторы для заголовков Соусы
    SAUCES_SECTION_HEADER = (By.XPATH, "//span[@class='text text_type_main-default'and text()='Соусы']")
    #Локаторы для заголовков Начинки
    FILLINGS_SECTION_HEADER = (By.XPATH, "//span[@class='text text_type_main-default'and text()='Начинки']")
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.ConstructorPageLocators import ConstructorPageLocators
buns="https://stellarburgers.nomoreparties.site/"
# Тест для перехода к разделу "Булки"
def test_navigate_to_buns_section(driver):
    driver.get(buns)
    driver.find_element(*ConstructorPageLocators.BUNS_SECTION_BUTTON).click()
    buns_header = driver.find_element(*ConstructorPageLocators.BUNS_SECTION_HEADER)
    assert buns_header.is_displayed(), "Булки"

# Тест для перехода к разделу "Соус"
def test_navigate_to_sauces_section(driver):
        driver.get(buns)
        driver.find_element(*ConstructorPageLocators.SAUCES_SECTION_BUTTON).click()
        buns_header = driver.find_element(*ConstructorPageLocators.SAUCES_SECTION_HEADER)
        assert buns_header.is_displayed(), "Соус"

# Тест для перехода к разделу "Начинки"
def test_navigate_to_fillings_section(driver):
            driver.get(buns)
            driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION_BUTTON).click()
            buns_header = driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION_HEADER)
            assert buns_header.is_displayed(), "Начинки"
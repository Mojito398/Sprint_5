from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.MainPageLocators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Тест для перехода по клику в «Личный кабинет».
def test_go_to_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import login
from selenium import webdriver
from locators.PersonalAccountPageLocators import PersonalAccountPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.MainPageLocators import MainPageLocators


# Тест по кнопке «Выйти» в личном кабинете.
def test_logout(driver, login):
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*PersonalAccountPageLocators.SIGN_OUT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


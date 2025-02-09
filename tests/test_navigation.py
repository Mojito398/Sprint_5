from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from conftest import login
from locators.PersonalAccountPageLocators import PersonalAccountPageLocators


# Тест для перехода по клику на «Конструктор»
def test_navigate_to_constructor_via_button(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*PersonalAccountPageLocators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


# Тест для перехода из личного кабинета в конструктор через "Логотип"
def test_navigate_to_constructor_via_logo(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*PersonalAccountPageLocators.LOGO_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
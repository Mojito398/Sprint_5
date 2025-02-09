from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.MainPageLocators import MainPageLocators
from locators.LoginPageLocators import LoginPageLocators
from locators.RegistrationFormLoginButton import RegistrationFormLoginButton
from locators.PasswordRecoveryPageLocators import PasswordRecoveryPageLocators
from locators.RegistrationPageLocators import RegistrationPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест для входа через кнопку "Войти в аккаунт" на главной странице
def test_login_via_main_page_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()

    driver.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT).send_keys("dmitriy_kiryukhin_18_123@yandex.ru")
    driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

# Тест для входа через кнопку "Личный кабинет" на главной странице
def test_login_via_personal_account_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT).send_keys("dmitriy_kiryukhin_18_123@yandex.ru")
    driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

# Тест для входа через кнопку "Войти" в форме регистрации
def test_login_via_registration_form_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*RegistrationFormLoginButton.LOGIN_BUTTON_REGISTRATION).click()

    driver.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT).send_keys("dmitriy_kiryukhin_18_123@yandex.ru")
    driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

# Тест для входа через кнопку "Войти" в форме восстановления пароля
def test_login_via_password_recovery_form_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*PasswordRecoveryPageLocators.LOGIN_BUTTON_RECOVERY).click()

    driver.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT).send_keys("dmitriy_kiryukhin_18_123@yandex.ru")
    driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    assert driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()
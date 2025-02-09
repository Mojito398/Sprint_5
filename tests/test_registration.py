from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.RegistrationPageLocators import RegistrationPageLocators
import random
import string

#Генерация случайного Email пользователя.
def generate_random_email():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    tlds = ['com', 'net', 'org', 'ru', 'ua']
    tld = random.choice(tlds)
    email = f"{username}@{domain}.{tld}"
    return email

# Тест для успешной регистрации
def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Дмитрий")
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_random_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()
    success_message = driver.find_element(*RegistrationPageLocators.SUCCESS_MESSAGE).text

    assert "Зарегистрироваться" in success_message

# Тест для проверки ошибки при некорректном пароле
def test_password_error(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Дмитрий")
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("dmitriy_kiryukhin_18_123@yandex.ru")
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("123")
    driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()
    error_message = driver.find_element(*RegistrationPageLocators.PASSWORD_ERROR).text

    assert "Некорректный пароль" in error_message
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.LoginPageLocators import LoginPageLocators

#Открывает и закрывает браузер
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

#Заполнение полей входа
@pytest.fixture
def login(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT).send_keys("dmitriy_kiryukhin_18_123@yandex.ru")
    driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
    yield

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from random import randint

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    return driver

@pytest.fixture
def new_email():
    return f'Евгений_Шляпкин_12_{randint(100, 999)}@yandex.ru'

@pytest.fixture
def authorization(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, '//*[contains(text(),"Email")]/parent::*/input').send_keys('Евгений_Шляпкин_12_001@yandex.ru')
    driver.find_element(By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input').send_keys('111111')
    driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Оформить заказ")]')))


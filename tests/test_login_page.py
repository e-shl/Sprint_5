import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_authorization_from_home_is_successful_authorization(driver):
    email = 'Евгений_Шляпкин_12_001@yandex.ru'
    password = '111111'
    driver.get("https://stellarburgers.nomoreparties.site")
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')))
    driver.find_element(By.XPATH, '//button[contains(text(),"Войти в аккаунт")]').click()
    driver.find_element(By.XPATH, '//*[contains(text(),"Email")]/parent::*/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input').send_keys(password)
    driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
    assert driver.find_element(By.XPATH, '//button[contains(text(),"Оформить заказ")]').text == 'Оформить заказ'
    driver.quit()

def test_authorization_from_button_profile_is_successful_authorization(driver):
    email = 'Евгений_Шляпкин_12_001@yandex.ru'
    password = '111111'
    driver.get("https://stellarburgers.nomoreparties.site")
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, '//a[@href="/account"]')))
    driver.find_element(By.XPATH, '//a[@href="/account"]').click()
    driver.find_element(By.XPATH, '//*[contains(text(),"Email")]/parent::*/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input').send_keys(password)
    driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
    assert driver.find_element(By.XPATH, '//button[contains(text(),"Оформить заказ")]').text == 'Оформить заказ'
    driver.quit()

def test_authorization_from_register_is_successful_authorization(driver):
    email = 'Евгений_Шляпкин_12_001@yandex.ru'
    password = '111111'
    driver.get("https://stellarburgers.nomoreparties.site/register")
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, '//a[@href="/login"]')))
    driver.find_element(By.XPATH, '//a[@href="/login"]').click()
    driver.find_element(By.XPATH, '//*[contains(text(),"Email")]/parent::*/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input').send_keys(password)
    driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
    assert driver.find_element(By.XPATH, '//button[contains(text(),"Оформить заказ")]').text == 'Оформить заказ'
    driver.quit()

def test_authorization_from_forgot_password_is_successful_authorization(driver):
    email = 'Евгений_Шляпкин_12_001@yandex.ru'
    password = '111111'
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, '//a[@href="/login"]')))
    driver.find_element(By.XPATH, '//a[@href="/login"]').click()
    driver.find_element(By.XPATH, '//*[contains(text(),"Email")]/parent::*/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input').send_keys(password)
    driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
    assert driver.find_element(By.XPATH, '//button[contains(text(),"Оформить заказ")]').text == 'Оформить заказ'
    driver.quit()
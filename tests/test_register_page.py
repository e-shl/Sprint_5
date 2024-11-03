import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.parametrize('password', ["123456", "1234567", "1234567891"])
def test_registration_is_successful_registration(driver,new_email, password):
    name = 'Евгений'
    email = new_email
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH,'//*[contains(text(),"Имя")]/parent::*/input').send_keys(name)
    driver.find_element(By.XPATH, '//*[contains(text(),"Email")]/parent::*/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input').send_keys(password)
    driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Войти")]')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()

@pytest.mark.parametrize('password', ["1", "1234", "12345"])
def test_registration_less6_password_is_error_message(driver,new_email, password):
    name = 'Евгений'
    email = new_email
    test_error_message = 'Некорректный пароль'
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH,'//*[contains(text(),"Имя")]/parent::*/input').send_keys(name)
    driver.find_element(By.XPATH, '//*[contains(text(),"Email")]/parent::*/input').send_keys(email)
    driver.find_element(By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input').send_keys(password)
    driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()
    error_message = driver.find_element(By.XPATH, '//*[contains(text(),"Пароль")]/ancestor::div[contains(@class,"input__container")]//p[contains(@class, "input__error")]').text
    assert error_message == test_error_message
    driver.quit()
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_click_logo_is_opened_designer_page(driver,authorization):
    driver.get('https://stellarburgers.nomoreparties.site/account')
    driver.find_element(By.XPATH, '//*[contains(@class,"AppHeader_header__logo")]').click()
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Оформить заказ")]')))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()

def test_click_designer_button_is_opened_designer_page(driver,authorization):
    driver.get('https://stellarburgers.nomoreparties.site/account')
    driver.find_element(By.XPATH, '//*[contains(text(),"Конструктор")]').click()
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Оформить заказ")]')))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()

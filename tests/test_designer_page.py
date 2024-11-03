import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_designer_click_bun_is_opened_bun(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, '//*[contains(@class,"tab_tab") and contains(.,"Начинки")]').click()
    driver.find_element(By.XPATH, '//*[contains(@class,"tab_tab") and contains(.,"Булки")]').click()
    WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[contains(@class,"tab_tab_type_current") and contains(.,"Булки")]')))
    assert WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH,'//h2[contains(text(),"Булки")]')))
    driver.quit()


def test_designer_click_sauce_is_opened_sauce(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, '//*[contains(@class,"tab_tab") and contains(.,"Начинки")]').click()
    driver.find_element(By.XPATH, '//*[contains(@class,"tab_tab") and contains(.,"Соусы")]').click()
    WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[contains(@class,"tab_tab_type_current") and contains(.,"Соусы")]')))
    assert WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH,'//h2[contains(text(),"Соусы")]')))
    driver.quit()

def test_designer_click_topping_is_opened_topping(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, '//*[contains(@class,"tab_tab") and contains(.,"Начинки")]').click()
    WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[contains(@class,"tab_tab_type_current") and contains(.,"Начинки")]')))
    assert WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH,'//h2[contains(text(),"Начинки")]')))
    driver.quit()
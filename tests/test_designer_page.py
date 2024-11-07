from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.help.locators import *
from tests.help.urls import *


def test_designer_click_bun_is_opened_bun(driver):
    driver.get(base_domain)
    driver.find_element(*tab_topping).click()
    driver.find_element(*tab_bun).click()
    assert WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(selected_bun))
    driver.quit()

def test_designer_click_sauce_is_opened_sauce(driver):
    driver.get(base_domain)
    driver.find_element(*tab_topping).click()
    driver.find_element(*tab_sauce).click()
    assert WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(selected_sauce))
    driver.quit()

def test_designer_click_topping_is_opened_topping(driver):
    driver.get(base_domain)
    driver.find_element(*tab_topping).click()
    assert WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(selected_topping))
    driver.quit()
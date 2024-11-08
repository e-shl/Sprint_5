from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.help.data import *
from tests.help.locators import *
from tests.help.urls import *


def test_authorization_from_home_is_successful_authorization(driver):
    driver.get(base_domain)
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(button_login_account))
    driver.find_element(*button_login_account).click()
    driver.find_element(*field_email).send_keys(base_email)
    driver.find_element(*field_password).send_keys(base_password)
    driver.find_element(*button_login).click()
    assert WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(button_place_order))
    

def test_authorization_from_button_profile_is_successful_authorization(driver):
    driver.get(base_domain)
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(button_profile))
    driver.find_element(*button_profile).click()
    driver.find_element(*field_email).send_keys(base_email)
    driver.find_element(*field_password).send_keys(base_password)
    driver.find_element(*button_login).click()
    assert WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(button_place_order))
    

def test_authorization_from_register_is_successful_authorization(driver):
    driver.get(registration_page_link)
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(link_login_page))
    driver.find_element(*link_login_page).click()
    driver.find_element(*field_email).send_keys(base_email)
    driver.find_element(*field_password).send_keys(base_password)
    driver.find_element(*button_login).click()
    assert WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(button_place_order))

def test_authorization_from_forgot_password_is_successful_authorization(driver):
    driver.get(forgot_password_page_link)
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(link_login_page))
    driver.find_element(*link_login_page).click()
    driver.find_element(*field_email).send_keys(base_email)
    driver.find_element(*field_password).send_keys(base_password)
    driver.find_element(*button_login).click()
    assert WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(button_place_order))
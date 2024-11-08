from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.help.locators import *
from tests.help.urls import *


def test_click_logo_is_opened_designer_page(driver,authorization):
    driver.get(profile_page_link)
    driver.find_element(*site_logo).click()
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(button_place_order))
    assert driver.current_url == base_domain

def test_click_designer_button_is_opened_designer_page(driver,authorization):
    driver.get(profile_page_link)
    driver.find_element(*button_designer).click()
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(button_place_order))
    assert driver.current_url == base_domain
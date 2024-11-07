from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.help.locators import *
from tests.help.urls import *


def test_exit_profile_is_open_login_page(driver,authorization):
    driver.get(profile_page_link)
    driver.find_element(*button_logout).click()
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(button_login))
    assert driver.current_url == login_page_link
    driver.quit()
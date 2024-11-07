from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.help.locators import *
from tests.help.urls import *


def test_link_profile_is_opened_profile_page(driver, authorization):
    driver.find_element(*button_profile).click() # Единственный тест не работающий в Firefox
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(form_profile))
    assert driver.current_url == static_profile_page_link
    driver.quit()


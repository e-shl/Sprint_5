import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.help.data import *
from tests.help.locators import *
from tests.help.urls import *


@pytest.mark.parametrize('password', ["123456", "1234567", "1234567891"])
def test_registration_is_successful_registration(driver,new_email, password):
    driver.get(registration_page_link)
    driver.find_element(*field_name).send_keys(base_name)
    driver.find_element(*field_email).send_keys(new_email)
    driver.find_element(*field_password).send_keys(password)
    driver.find_element(*button_registration).click()
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(button_login))
    assert driver.current_url == login_page_link
    driver.quit()

@pytest.mark.parametrize('password', ["1", "1234", "12345"])
def test_registration_less6_password_is_error_message(driver,new_email, password):
    test_error_message = 'Некорректный пароль'
    driver.get(registration_page_link)
    driver.find_element(*field_name).send_keys(base_name)
    driver.find_element(*field_email).send_keys(new_email)
    driver.find_element(*field_password).send_keys(password)
    driver.find_element(*button_registration).click()
    error_message = driver.find_element(*text_error_password).text
    assert error_message == test_error_message
    driver.quit()
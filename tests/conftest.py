from random import randint

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.help.data import *
from tests.help.locators import *
from tests.help.urls import *


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    return driver

@pytest.fixture
def new_email():
    return f'Евгений_Шляпкин_12_{randint(100, 999)}@yandex.ru'

@pytest.fixture
def authorization(driver):
    driver.get(login_page_link)
    driver.find_element(*field_email).send_keys(base_email)
    driver.find_element(*field_password).send_keys(base_password)
    driver.find_element(*button_login).click()
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(button_place_order))


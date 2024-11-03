import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_link_profile_is_opened_profile_page(driver, authorization):
    driver.find_element(By.XPATH, '//a[@href="/account"]').click() # Единственный тест не работающий в Firefox
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[contains(@class, "Profile_profileList_")]')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
    driver.quit()


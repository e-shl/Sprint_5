import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_exit_profile_is_open_login_page(driver,authorization):
    driver.get('https://stellarburgers.nomoreparties.site/account')
    driver.find_element(By.XPATH, '//button[text()="Выход"]').click()
    WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Войти")]')))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    driver.quit()
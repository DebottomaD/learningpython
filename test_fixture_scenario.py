import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def setup_module():
    global driver
    driver = webdriver.Chrome(executable_path="../../resources/chromedriver.exe")
    driver.maximize_window()

    yield
    driver.quit()


def test_chrome(setup_module):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    driver.find_element(By.NAME, "Submit").submit()
    time.sleep(4)
    print(driver.title)
    assert driver.title == 'OrangeHRM'

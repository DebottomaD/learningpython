import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = None


def setup_module(module):
    global driver
    driver = webdriver.Chrome(executable_path="../../resources/chromedriver.exe")
    driver.maximize_window()


def test_chrome():

    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    driver.find_element(By.NAME, "Submit").submit()
    time.sleep(4)
    print(driver.title)
    assert driver.title == 'OrangeHRM'


def teardown_module(module):
    driver.quit()

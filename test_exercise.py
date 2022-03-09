
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../../resources/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.co.in/")
driver.minimize_window()


driver.get("https://opensource-demo.orangehrmlive.com/")
driver.back()
driver.forward()
driver.maximize_window()

print(driver.current_url)
driver.fullscreen_window()
all_links = driver.find_elements(By.TAG_NAME, 'a')


for element in all_links:
    print(element.text, ' ', '-', ' ', element.get_attribute("href"))

print(driver.title)
print(driver.current_url)

print(driver.page_source)


driver.quit()


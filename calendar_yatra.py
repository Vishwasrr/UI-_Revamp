from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.yatra.com")

date_field = driver.find_element(
    By.XPATH, "//input[@id='BE_flight_origin_date']")
date_field.click()

sleep(3)
date = driver.find_element(By.XPATH, "//td[@id='07/05/2024']")
date.click()

sleep(5)

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get()
driver.maximize_window()
driver.implicitly_wait(10)


# get attributes
driver.find_element(By.XPATH, "xpath").get_attribute("value/name/etc")


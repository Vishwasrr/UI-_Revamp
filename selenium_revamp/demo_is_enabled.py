from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://training.openspan.com/login")
driver.maximize_window()
driver.implicitly_wait(10)

sign_in_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()

if sign_in_state:
    print("Button is enabled")
else:
    print("It's not")
    
# to check hidden elements    
# another example is is_displayed()
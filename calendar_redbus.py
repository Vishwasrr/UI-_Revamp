from time import sleep

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(r"C:\Everything\Complete Preps\UI_AutomationRevamp\chromedriver.exe")
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.redbus.com/")
driver.maximize_window()
from_location = driver.find_element(By.XPATH, "//input[@id='src']")

from_location.click()
from_location.send_keys("New Delhi")
# sleep(3)

body = driver.find_element(By.XPATH, "//body")
body.click()

to_location = driver.find_element(By.XPATH, "//input[@id='dest']")
# sleep(3)
to_location.click()
to_location.send_keys("Bombay")
# sleep(3)

date = driver.find_element(By.XPATH, "//div[@id='date-box']")
date.click()

# departure_date = driver.find_element(By.XPATH, "(//span[text()='25'])[1]")
departure_date = driver.find_element(
    By.XPATH, "//span[@class='DayTiles__CalendarDaysSpan-sc-14em0t0-1 kseSaZ'][normalize-space()='27']")
departure_date.click()

sleep(5)

driver.close()

from datetime import datetime, timedelta
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(r"C:\Everything\Complete Preps\UI_AutomationRevamp\chromedriver.exe")
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get(
    "file:///C:/Everything/Complete%20Preps/UI_AutomationRevamp/calendar_simple.html")
driver.maximize_window()
driver.implicitly_wait(10)

date_picker = driver.find_element(By.XPATH, "//input[@id='date']")


# try this with direct strings, and follow this tutorial for stackoverflow
# https://www.youtube.com/watch?v=IKQ7Goi3Z4c&ab_channel=TestingFundabyZeeshanAsghar
# current_date = datetime.now()
# next_date = current_date + timedelta(days=0)
# print((next_date))
# formatted_date = next_date.strftime("%d/%m/%Y")
formatted_date = "27/04/2024"
print(formatted_date)
formatted_date = formatted_date.split('/')
formatted_date[0] = "28"
formatted_date[1] = "04"
formatted_date[2] = "2024"

date_picker.send_keys(formatted_date[0])
date_picker.send_keys(formatted_date[1])
date_picker.send_keys(Keys.TAB)
date_picker.send_keys(formatted_date[2])

sleep(5)


# NOTES:
"""
1. This file shows how to select dates from a normal date picker.
2. The second method is when the date is a Select box. This can be handled the same way any select box is handled
3. The third way is when it's a table. This is shown in PytestDDTHybrid demo

"""

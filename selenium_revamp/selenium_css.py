from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
# element = driver.find_element(By.ID, "ID_Value")
#
# elem = driver.find_element(By.CLASS_NAME, "CLASS Value")
sleep(3)
# cart = driver.find_element(By.CSS_SELECTOR, ".nav-cart-icon.nav-sprite")
cart = driver.find_element(By.CSS_SELECTOR, "span.nav-cart-count")
color_value = cart.value_of_css_property("color")
size = cart.size
print(size)
print(type(size))

location = cart.location
print(location)
print(type(location))

print(color_value)
print(type(color_value))
import re
rgb = re.findall(r"\d+", color_value)
rgb = list(map(int, rgb))
print(rgb)
cart.click()


# wait = WebDriverWait(driver, timeout=10)
# # wait.until(ec.element_to_be_clickable((By.XPATH, "XPATH")))
# alert_box = wait.until(ec.alert_is_present())
#
# alert_box = driver.switch_to.alert
# alert_box.dismiss()
#
#
sleep(5)

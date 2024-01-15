from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
print("Launching website")
url = "https://www.snapdeal.com/products/mobiles-accessories?sort=plrty&q=Price%3A104%2C2899%7C"
driver.get(url)

left_handle = driver.find_element(By.XPATH, '//a[contains(@class,"left-handle")]')
right_handle = driver.find_element(By.XPATH, '//a[contains(@class,"right-handle")]')
actions = ActionChains(driver)
print("Before dragging")
from_text = driver.find_element(By.XPATH, '//span[contains(text(), "Rs 104")]')
print(from_text.text)
print("Dragging the handle")
sleep(3)
# actions.drag_and_drop_by_offset(left_handle, 60, yoffset=0).perform()  # moves the handle by 60px
# using while loop
from_text = driver.find_element(By.XPATH, '//span[contains(@class, "from-price-text")]')
while from_text.text != 'Rs 1593':
    actions.drag_and_drop_by_offset(left_handle, 0.1, yoffset=0).perform()  # moves the handle by 60px
sleep(3)
print("After dragging")
print(from_text.text)
print("Testing done")
# alternate way: (in case there are sync issue)
# actions.click_and_hold().pause(1).move_by_offset(60, 0).release().perform()

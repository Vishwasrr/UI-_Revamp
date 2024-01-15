from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
print("Launching website")
url = "https://www.yatra.com"
driver.get(url)
handles = driver.window_handles
yatra_prime = driver.find_element(By.XPATH, "//img[@class='conta iner']")
yatra_prime.click()
driver.switch_to.window(handles[0])  # same as parent_handle = driver.current_window_handle
covid_refund = driver.find_element(By.XPATH, "//img[@class='conta iner large-banner']")
covid_refund.click()
driver.switch_to.window(handles[0])
handles = driver.window_handles

for handle in handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        sleep(5)
        print(driver.title)

driver.quit()

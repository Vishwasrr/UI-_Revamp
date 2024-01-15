from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
print("Launching website")
url = "https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert"
driver.get(url)
driver.switch_to.frame("iframeResult")
try_it = driver.find_element(By.XPATH, "//button[normalize-space()='Try it']")
try_it.click()

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
print("Accepting alert box")
sleep(2.3)
alert.accept()
# for prompt: alert.send_keys()
# for cancelling: alert.dismiss()

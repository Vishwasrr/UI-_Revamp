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
url = "https://www.tutorialspoint.com/tutor_connect/index.php"
driver.get(url)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(5)
# horizontal scrolling
# Scroll right by 250 pixels (Chrome/Chromium)
driver.execute_script("document.documentElement.scrollLeft += 250")
# Scroll to the rightmost edge
driver.execute_script("document.documentElement.scrollLeft = document.documentElement.scrollWidth")
sleep(5)

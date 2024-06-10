from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions

# @wait_for_element(driver, "sign_up")
# def test_frames():
# service = Service(executable_path=ChromeDriverManager().install())
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome()
driver.maximize_window()
print("Launching website")
url = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css"
driver.get(url)

outerframe = driver.find_element(By.XPATH, "//iframe[@id='iframeResult']")
driver.switch_to.frame(outerframe)

# innerframe = driver.find_element(By.XPATH, "//iframe[@src='default.asp']")
# driver.switch_to.frame(innerframe)
driver.switch_to.frame(1)

login = driver.find_element(By.XPATH, "//a[normalize-space()='Log in']")
login.click()


sleep(5)
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import ElementClickInterceptedException

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver = webdriver.Firefox()
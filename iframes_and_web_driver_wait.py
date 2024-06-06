# In simple terms, an iFrame is basically an html document embedded inside another
# A frame can be any embedded element: <frame>, <iframe>, <embed>, <object>
# //h3[normalize-space()='Frame1:']
from selenium import webdriver
from time import sleep
from functools import wraps
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
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
print("Launching website")
url = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css"
driver.get(url)

# switch via ID
# driver.switch_to.frame("<FrameID>")
# switch via Name
# driver.switch_to.frame("FrameName")

# switch to main frame
# driver.switch_to.default_content()

# switch via iframe locator
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
# switch via index
driver.switch_to.frame(2)
# driver.switch_to.default_content()
sign_up = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)

# poll-frequency is in milliseconds by default
sign_up = WebDriverWait(driver, 10, poll_frequency=300, ignored_exceptions=ignored_exceptions).until(
    expected_conditions.presence_of_element_located((By.XPATH, "//a[normalize-space()='Sign Up']")))
sign_up.click()
print(sign_up.text)
sleep(3)

"""
Explanation for a StaleElementReferenceException: A element becomes stale when it's no longer attached to the DOM you are 
trying to access. You can handle it refreshing the browser, handling it inside a try-catch block with the help of webdriver wait
"""
# try implementing a wait decorator


# def wait_for_element(locator):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             driver = args[0]  # Assume driver is the first argument
#             element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.ID, locator))
#             )
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator

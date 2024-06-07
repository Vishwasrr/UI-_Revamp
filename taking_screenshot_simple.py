from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pytest
# driver.maximize_window()
# print("Launching website")
# url = "https://www.google.com/"
# driver.get(url)

from web_utils import WebUtils


@pytest.mark.usefixtures("tc_setup")
class TestSample(WebUtils):
    def test_sample(self):
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        print("Launching website")
        # url = "http://www.yatra.com/"
        # self.driver.get(url)

        # assert 4 == 5
        refund = self.driver.find_element(By.XPATH, "//input[@value='Check Refund']")
        refund.click()
        # capture_screenshot()


"""Here's the easy way:"""
# driver.save_screenshot( r"C:\Users\Vishw\OneDrive\Desktop\UI_AutomationRevamp\Screenshots\ss1.jpg")  # -> bool:
# True if successfully captured w/o any IOError, else False can take any extension .jps, .png, etc

# driver.get_screenshot_as_file(
# r".\Screenshots\ss4.png")  # takes only .png extensions -> bool, True if successfully captured w/o any IOError

# driver.get_screenshot_as_png() -> bytes


"""
element.screenshot(screenshot_filepath) get a screenshot only of button, and 
driver.get_screenshot_as_file(screenshot_filepath) get a screenshot of full page

"""

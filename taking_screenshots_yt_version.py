from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class DemoScreenshot:
    @staticmethod
    def demo_screen_capture():
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        print("Launching website")
        # driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.get("https://www.yatra.com/")
        my_account = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle']")
        hover = ActionChains(driver).move_to_element(my_account)
        hover.perform()

        login = driver.find_element(By.XPATH, "//a[@id='signInBtn']")
        login.click()
        continuedemo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        print("Capturing screenshot")
        continuedemo.screenshot(".\\Screenshots\\test.png")
        continuedemo.click()
        sleep(2)
        driver.get_screenshot_as_file(".\\SeleniumErrorScreenshots\\test1.png")
        driver.save_screenshot(".\\SeleniumErrorScreenshots\\test1.png")
        # driver.save_screenshot(r"test1.png")
        print("Screenshot saved")


demo = DemoScreenshot()
demo.demo_screen_capture()

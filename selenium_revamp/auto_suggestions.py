import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# from selenium.webdriver.common.alert import Alert


class DemoAutoSuggest:
    @staticmethod
    def demo_autosuggest_drop():
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        print("Launching website")
        driver.get("https://www.yatra.com/")
        print("Maximizing window...")
        driver.maximize_window()
        driver.implicitly_wait(10)
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        print("Clicking on depart from field")
        depart_from.click()
        time.sleep(3.2)
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        time.sleep(3.2)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.clear()
        print("Clicking on going to field")
        time.sleep(3.2)
        going_to.send_keys("New")
        time.sleep(3.2)
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for result in search_results:
            if result.text == 'New York (JFK)':
                result.click()
                time.sleep(3.2)
                break
        print("All done")


dauto = DemoAutoSuggest()
dauto.demo_autosuggest_drop()

"""
An attempt to dismiss location pop-up
prefs = {"profile.default_content_setting_values.geolocation": 2,
                 "profile.managed_default_content_settings.geolocation": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-infobars")

"""

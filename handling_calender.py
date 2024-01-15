from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class DemoCalendar:
    @staticmethod
    def demo_calendar():
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
        sleep(3.2)
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        sleep(3.2)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.clear()
        print("Clicking on going to field")
        sleep(3.2)
        going_to.send_keys("New")
        sleep(3.2)
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for result in search_results:
            result_text = result.text
            result_text = result_text.split('\n')[0]
            # print(result_text)
            if result_text == 'New York (JFK)':
                sleep(5)
                print("Clicking on NY-JFK")
                result.click()
                break

        sleep(3.2)
        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        # print(origin)
        origin.click()
        sleep(3)
        # driver.find_element(By.XPATH, "//td[@id='30/12/2023").click()
        # sleep(3)
        # date xpath: //div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']
        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        WebDriverWait(driver, 20, ignored_exceptions=[ElementClickInterceptedException]).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))).click()
        # ignore_exceptions: These are the exceptions you are expecting. So you are telling the compiler to continue
        # executing despite that particular exception/list of exceptions
        # print("All dates: ", all_dates)
        for date in all_dates:
            # print("Inside for-loop")
            if date.get_attribute('data-date') == '14/01/2024':
                print("Clicking on date", date.get_attribute('data-date'))
                date.click()
                break


dauto = DemoCalendar()
dauto.demo_calendar()
print("All done")

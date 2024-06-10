from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

# Replace with the path to your WebDriver (e.g., Chrome WebDriver)
driver = webdriver.Chrome()
# Replace with the URL containing alerts
driver.get("https://www.example.com/page-with-alerts")

# Identify the element that triggers the alert
# Replace with the actual locator
alert_button = driver.find_element(By.ID, "alert_button")

# Click the button to trigger the alert
alert_button.click()

try:
    # Switch focus to the alert window
    alert = driver.switch_to.alert

    # Get the text of the alert
    alert_text = alert.text
    print(f"Alert Text: {alert_text}")

    # Handle different alert types based on the situation:

    # 1. Accepting an alert (clicking OK)
    alert.accept()

    # 2. Dismissing an alert (clicking Cancel)
    # alert.dismiss()  # Uncomment if needed

    # 3. Entering text into a prompt alert
    # if it's a prompt alert:
    #   alert.send_keys("Your text here")
    #   alert.accept()

except NoAlertPresentException:
    print("No alert was present.")

finally:
    # Close the browser window
    driver.quit()


class Prime:
    def __init__(self):
        self.n = None

    def is_prime(self):
        for i in range(2, self.n):
            if self.n % i == 0:
                return False
        return False

import time
from selenium import webdriver

# Replace with the path to your WebDriver (e.g., Chrome WebDriver)
driver = webdriver.Chrome()
driver.get("https://www.example.com")  # Visit any webpage

# Simple JavaScript to display an alert
script = "alert('Hello from Selenium!')"

# Execute the script using driver.execute_script()
driver.execute_script(script)

# Optional pause to allow the alert to be displayed before closing the browser
# You can replace this sleep with other actions you want to perform after the alert appears.
time.sleep(2)

driver.quit()

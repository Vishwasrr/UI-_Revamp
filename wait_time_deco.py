import time

def wait_decorator(seconds=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Usage:

@wait_decorator(seconds=3)
def example_function():
    print("Function executed after a 3-second wait.")

# Call the decorated function
example_function()


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

def selenium_wait_decorator(timeout=10, by=By.ID, value=None):
    def decorator(func):
        def wrapper(driver, *args, **kwargs):
            # Use WebDriverWait to wait for the specified element
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            
            # Call the original function with the driver and other arguments
            result = func(driver, element, *args, **kwargs)
            return result
        return wrapper
    return decorator

# Usage:

@selenium_wait_decorator(timeout=10, by=By.ID, value="exampleElement")
def click_element(driver, element):
    element.click()
    print("Element clicked successfully.")

# Example usage with a WebDriver instance (assuming 'driver' is an instance of WebDriver)
driver = webdriver.Chrome()
click_element(driver)

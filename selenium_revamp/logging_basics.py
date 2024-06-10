"""https://docs.python.org/3/library/logging.html#logrecord-attributes"""
"""
DEBUG: Information interesting for Developers, when trying to debug a problem.
INFO: Information interesting for Support staff trying to figure out the context of a given error
WARN to FATAL: Problems and Errors depending on the level of damage.
"""

import logging

logging.basicConfig(level=logging.DEBUG, filename=r'.\Logs\log_file.log',
                    filemode='a', format='%(asctime)s - %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

"""
Parameter explanations:
order: month, date, year, hour, minute, time
"""
logging.info("Sample logging statement")

"""
Generated using snippets
driver.find_element(By.XPATH, "//input[@class='Search']")
driver.find_element(By.XPATH, "//input[@class='Search']")
"""

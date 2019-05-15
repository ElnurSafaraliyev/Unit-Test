import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import HtmlTestRunner


# Alerts & Popups

driver = webdriver.Chrome(executable_path="C:/Users/Cissy/Desktop/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")


driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()

driver.implicitly_wait(10)

#driver.switch_to_alert().accept() # Yes, OK, Accept
driver.switch_to_alert().dismiss()  # No, Cancel, Dismiss
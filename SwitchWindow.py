import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner



# Page Scrolling

driver = webdriver.Chrome(executable_path="C:/Users/Cissy/Desktop/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.current_window_handle) #CDwindow-A2A71A6B022BBDCD662D484E27B57BEA

driver.find_element_by_xpath("//div[@id='Tabbed']//button[@class='btn btn-info'][contains(text(),'click')]").click()
print(driver.current_window_handle) #CDwindow-A2A71A6B022BBDCD662D484E27B57BEA

handles = driver.window_handles

for handle in handles:
    driver.switch_to_window(handle)
    print(driver.title, driver.current_window_handle)
    if driver.title == "Frames & windows":
        driver.close()
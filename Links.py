import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import HtmlTestRunner


#Links

driver = webdriver.Chrome(executable_path="C:/Users/Cissy/Desktop/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://newtours.demoaut.com")

links = driver.find_elements_by_tag_name("a")

print("Number of links: ", len(links))


for link in links:
    print(link.text)


driver.find_element_by_partial_link_text("Reg").click()
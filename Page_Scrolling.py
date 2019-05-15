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

# driver.get("https://testautomationpractice.blogspot.com/")

# Scroll down the Page by Pixel
# driver.execute_script("window.scrollBy(0,800)", "")


# Scroll down to the end of the Page
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

# Scroll down the page untill element found  - JDK (install Latest JDK)
# driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
# driver.execute_script("argument[0].scrollIntoView();", "//table[1]//tbody[1]//tr[12]//td[1]//img[1]")

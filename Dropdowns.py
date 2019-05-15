import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import HtmlTestRunner


#Dropdowns

driver = webdriver.Chrome(executable_path="C:/Users/Cissy/Desktop/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()



driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Select Element in dropdown by Visible text

Best_Time = driver.find_element_by_xpath("//select[@name='RESULT_RadioButton-7']")
Time = Select(Best_Time)

Time.select_by_visible_text("Morning")
time.sleep(2)

#or
Select(driver.find_element_by_xpath("//select[@name='RESULT_RadioButton-7']")).select_by_visible_text("Evening")



# Select Element in dropdown by Value
time.sleep(3)
Time.select_by_value("Radio-1")


# Select Element in a dropdown by Index

time.sleep(3)
Time.select_by_index("2")

# Capture all optins and print them as an output
print(len(Time.options))
alloptions = Time.options

for options in alloptions:
    print (options.text)
import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import openpyxl
import DataDriverTransferDDT.XUtils


path = "C:/Users/Cissy/Desktop/Canadian All Care/QA/Testing/DDT/Login.xlsx"


workbook = openpyxl.load_workbook(path)
sheet = workbook.active

driver = webdriver.Chrome(executable_path="C:/Users/Cissy/Desktop/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://newtours.demoaut.com/")

XUtils = DataDrivenTransferDDT.XUtils
rows = XUtils.getRowCount(path)
print(rows)


for r in range(2, rows+1):
    username = XUtils.readData(path,r,1)
    password = XUtils.readData(path, r, 2)
    driver.find_element_by_xpath("//input[@name='userName']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//input[@name='login']").click()



    if driver.title == "Find a Flight: Mercury Tours:":
        print("Pass")
        XUtils.writeData(path, r, 3, "PASS")
    else:
        print("Failed")
        XUtils.writeData(path, r, 3, "FAILED")

    driver.find_element_by_xpath("//a[contains(text(),'Home')]").click()
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


class demoauto_cart :

    def __init__ (self,driver):

        self.driver = driver
        driver.get("https://www.ebay.ca")
        self.driver.get("http://demo.automationtesting.in/Register.html")
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[contains(text(),'Practice Site')]").click()
        time.sleep(5)
       # x = self.driver.current_url
        #print(x)
        #self.assertEqual(x,"http://demo.automationtesting.in/Register.html")

        self.driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@id='username']").send_keys("elnursefereliyev@gmail.com")
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Elnur1984")
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//h3[contains(text(),'JS Data Structures and Algorithm')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(@class,'single_add_to_cart_button button alt')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        time.sleep(5)
        #x = self.driver.current_url
        #self.assertEqual(x,"http://practice.automationtesting.in/my-account/")

    #@classmethod
    #def tearDownClass(cls):
    #   cls.driver.close()

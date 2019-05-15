"""
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


class demoauto_cart (unittest.TestCase):
    @classmethod

    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/Cissy/Desktop/chromedriver.exe")
        time.sleep(5)
        cls.driver.maximize_window()

    def test_AddCart (self):
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
        x = self.driver.current_url
        self.assertEqual(x,"http://practice.automationtesting.in/my-account/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()




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


class demoauto_reg (unittest.TestCase):
    @classmethod

    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/Cissy/Desktop/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_Register(self):
        self.driver.get("http://demo.automationtesting.in/")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//img[@id='enterimg']").click()
        self.driver.implicitly_wait(5)
        #x = self.driver.current_url
        #print(x)
        #self.assertEqual(x,"http://demo.automationtesting.in/Register.html")

        self.driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Elnur")
        self.driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("S")
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]").send_keys("Toronto")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]").send_keys("elnursefereliyev@gmail.com")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]").send_keys("6479973520")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[5]/div[1]/label[1]/input[1]").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[6]/div[1]/div[2]/input[1]").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//div[@id='msdd']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[contains(text(),'English')]").click()
        self.driver.implicitly_wait(5)
        Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[8]/div[1]/select[1]")).select_by_visible_text("Excel")
        self.driver.implicitly_wait(5)
        Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[9]/div[1]/select[1]")).select_by_visible_text("Azerbaijan")
        self.driver.implicitly_wait(5)
        #Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[10]/div[1]/span[1]/span[1]/span[1]")).select_by_visible_text("Japan")
        self.driver.implicitly_wait(5)
        Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[11]/div[1]/select[1]")).select_by_visible_text("1984")
        self.driver.implicitly_wait(5)
        Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[11]/div[2]/select[1]")).select_by_visible_text("December")
        self.driver.implicitly_wait(5)
        Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[11]/div[3]/select[1]")).select_by_visible_text("21")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[12]/div[1]/input[1]").send_keys("Elnur1984")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[13]/div[1]/input[1]").send_keys("Elnur1984")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[14]/div[1]/button[1]").click()
        time.sleep(20)
        x = self.driver.current_url
        print(x)
        self.assertEqual(x, "http://demo.automationtesting.in/WebTable.html")



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
# unittest.main()  #testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/Cissy/Desktop/TestReport"),verbosity=2

"""
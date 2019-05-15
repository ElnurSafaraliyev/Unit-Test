import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait



class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/Cissy/Desktop/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login_1(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("// input[ @ id = 'btnLogin']").click()
        x = self.driver.current_url
        print(x)
        self.assertEqual(x, "https://opensource-demo.orangehrmlive.com/index.php/dashboard")


    def test_logout_2(self):
        self.driver.find_element_by_xpath("//a[@id='welcome']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        self.driver.implicitly_wait(5)
        x = self.driver.current_url
        print(x)
        self.assertEqual(x, "https://opensource-demo.orangehrmlive.com/index.php/auth/login")

    def test_login_3(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin56")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("// input[ @ id = 'btnLogin']").click()
        x = self.driver.current_url
        print(x)
        self.assertEqual(x, "https://opensource-demo.orangehrmlive.com/index.php/auth/dashboard")


    def test_login_4(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("@3admin")
        self.driver.find_element_by_xpath("// input[ @ id = 'btnLogin']").click()
        x = self.driver.current_url
        print(x)
        self.assertEqual(x,"https://opensource-demo.orangehrmlive.com/index.php/dashboard" )

    def test_adduser(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("// input[ @ id = 'btnLogin']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("// b[contains(text(), 'Admin')]").click()
        self.driver.find_element_by_xpath("//input[@id='btnAdd']").click()
        self.driver.find_element_by_xpath("//input[@id='systemUser_employeeName_empName']").send_keys("T")
        self.driver.find_element_by_xpath("//div[@class='ac_results']//li[2]").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@id='systemUser_userName']").send_keys("octop")
        self.driver.find_element_by_xpath("// input[ @ id = 'systemUser_password']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("// input[ @ id = 'systemUser_password']").send_keys("10111234")
        self.driver.find_element_by_xpath("// input[ @ id = 'systemUser_confirmPassword']").send_keys("10111234")
        self.driver.find_element_by_xpath("// input[ @ id = 'btnSave']").click()
        self.driver.find_element_by_xpath("//a[@id='welcome']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        self.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quick()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/Cissy/Desktop/TestReport"),verbosity=2)


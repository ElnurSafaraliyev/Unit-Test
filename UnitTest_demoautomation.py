import unittest
from POM.DemoAutomationTesting.POM.Pages.Register import demoauto_reg
from POM.DemoAutomationTesting.POM.Pages.AddCart import demoauto_cart
from selenium import webdriver
import time
import HtmlTestRunner



class Domeautomationtest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/Cissy/Desktop/chromedriver.exe")
        time.sleep(2)
        cls.driver.maximize_window()


    def test_register(self):
        self.driver.get("http://demo.automationtesting.in/")
        demoauto_reg(self.driver).register("Elnur", "Safaraliyev", "2960 D", "elnursefereliyev@gmail.com", "6479973520", "MySQL", "Japan", "1984", "Decmber", "21", "Elnur1984d", "Elnur1984d" )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="/Users/Cissy/Desktop/TestReport/"),verbosity=2)

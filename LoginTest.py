import unittest
from POM.OrangeHRM.Pages.HomePage import HomePage
from POM.OrangeHRM.Pages.LoginPage import LoginPage
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Cissy/Desktop/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        homepage = HomePage(driver)
        homepage.welcome()
        homepage.logout()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()
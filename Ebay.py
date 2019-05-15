import unittest
from selenium import webdriver
from Pages.LoginPageEbay import Login
from Pages.LogoutEbay import Logout
from Pages.AddCartEbay import SearchAdd
from Pages.SearchEbay import Search
import HtmlTestRunner


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Cissy/Desktop/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.ebay.ca")

        login = Login(driver)
        login.click_signin()
        login.enter_user_name("elnursefereliyev@gmail.com")
        login.password_enter("Elnur1984e")
        login.signIn()

        search = Search(driver)
        search.write_item_for_search("car")
        search.search_item()

        cart = SearchAdd(driver)
        cart.choose()
        cart.add_cart()

        Logout(driver).hi()
        Logout(driver).logout()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/Cissy/Desktop/TestReport/"),verbosity=2)


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


class demoauto_reg:
    def __init__(self,driver):
        self.driver = driver
        driver.implicitly_wait(5)
        driver.entering_xpath = "//img[@id='enterimg']"
        driver.implicitly_wait(5)
        driver.first_name_xpath = "//input[@placeholder='First Name']"
        driver.last_name_xpath = "//input[@placeholder='Last Name']"
        driver.address_xpath ="/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]"
        driver.implicitly_wait(5)
        driver.email_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]"
        driver.implicitly_wait(5)
        driver.phone_number_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]"
        driver.implicitly_wait(5)
        driver.gender_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[5]/div[1]/label[1]/input[1]"
        driver.implicitly_wait(5)
        driver.hobbies_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[6]/div[1]/div[2]/input[1]"
        driver.implicitly_wait(5)
        driver.lang_xpath = "//div[@id='msdd']"
        driver.implicitly_wait(5)
        driver.choose_lang_xpath = "//a[contains(text(),'English')]"
        driver.implicitly_wait(5)
        driver.skills = Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[8]/div[1]/select[1]"))
        driver.implicitly_wait(5)
        driver.country = Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[9]/div[1]/select[1]"))
        driver.implicitly_wait(5)
        # Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[10]/div[1]/span[1]/span[1]/span[1]")).select_by_visible_text("Japan")
        driver.implicitly_wait(5)
        driver.year = Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[11]/div[1]/select[1]"))
        driver.implicitly_wait(5)
        driver.month = Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[11]/div[2]/select[1]"))
        driver.implicitly_wait(5)
        driver.day = Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[11]/div[3]/select[1]"))
        driver.implicitly_wait(5)
        driver.password_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[12]/div[1]/input[1]"
        driver.implicitly_wait(5)
        driver.conf_password_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[13]/div[1]/input[1]"
        driver.implicitly_wait(5)
        driver.submite_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[14]/div[1]/button[1]"
        # time.sleep(20)

    def register(self,first_name, last_name, address, email, cell_num, skills, country, year, month, day, password, conf_password):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.driver.entering_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.driver.first_name_xpath).send_keys(first_name)
        self.driver.find_element_by_xpath(self.driver.last_name_xpath).send_keys(last_name)
        self.driver.find_element_by_xpath( self.driver.address_xpath).send_keys(address)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.driver.email_xpath).send_keys(email)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath( self.driver.phone_number_xpath ).send_keys(cell_num)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.driver.gender_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.driver.hobbies_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.driver.lang_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.driver.choose_lang_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.skills.select_by_visible_text(skills)
        self.driver.implicitly_wait(5)
        self.driver.country.select_by_visible_text(country)
        self.driver.implicitly_wait(5)
        #Select(self.driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[10]/div[1]/span[1]/span[1]/span[1]")).select_by_visible_text("Japan")
        self.driver.implicitly_wait(5)
        self.driver.year.select_by_visible_text(year)
        self.driver.implicitly_wait(5)
        self.driver.month.select_by_visible_text(month)
        self.driver.implicitly_wait(5)
        self.driver.day.select_by_visible_text(day)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.driver.password_xpath).send_keys(password)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.driver.conf_password_xpath).send_keys(conf_password)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.driver.submite_xpath).click()
        #time.sleep(20)
        #x = self.driver.current_url
        #print(x)
        #self.assertEqual(x, "http://demo.automationtesting.in/WebTable.html")



#if __name__ == '__main__':
 #   unittest.main()  #testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/Cissy/Desktop/TestReport"),verbosity=2
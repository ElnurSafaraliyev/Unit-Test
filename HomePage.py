#https://opensource-demo.orangehrmlive.com/index.php/dashboard

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.welcome_xpath = "//a[@id='welcome']"
        self.logout_xpath = "//a[contains(text(),'Logout')]"

    def welcome(self):
        self.driver.find_element_by_xpath(self.welcome_xpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()

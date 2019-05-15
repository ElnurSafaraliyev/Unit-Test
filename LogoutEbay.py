
class Logout():

    def __init__(self,driver):
        self.driver = driver
        self.hi_xpath = "//button[@id='gh-ug']"
        self.logout_textbox_xpath = "//a[contains(text(),'Sign out')]"

    def hi (self):
        self.driver.find_element_by_xpath(self.hi_xpath).click()


    def logout (self):
        self.driver.find_element_by_xpath(self.logout_textbox_xpath).click()

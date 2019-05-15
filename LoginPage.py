
class LoginPage():
    def __init__(self,driver):
        self.driver = driver
                # These are the three locators on this paage
        self.username_textbox_xpath = "//input[@id='txtUsername']"
        self.password_textbox_xpath = "//input[@id='txtPassword']"
        self.login_button_xpath ="//input[@id='btnLogin']"

    def enter_username (self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()



#https://opensource-demo.orangehrmlive.com/

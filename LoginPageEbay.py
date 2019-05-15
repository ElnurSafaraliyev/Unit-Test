
class Login():

    def __init__(self,driver):
        self.driver = driver
        self.sign_in_box_xpath = "//a[contains(text(),'Sign in')]"
        self.user_name_textbox_xpath = "//input[@id='userid']"
        self.password_textbox_xpath = "//input[@id='pass']"
        self.sign_in_button_xpath = "//button[@id='sgnBt']"

    def click_signin (self):
        self.driver.find_element_by_xpath(self.sign_in_box_xpath).click()

    def enter_user_name (self, username):
        self.driver.find_element_by_xpath(self.user_name_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.user_name_textbox_xpath).send_keys(username)

    def password_enter (self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def signIn (self):
        self.driver.find_element_by_xpath(self.sign_in_button_xpath).click()


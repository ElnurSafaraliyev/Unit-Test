
class SearchAdd():

    def __init__(self,driver):
        self.driver = driver
        self.choose_item_xpath = "//a[contains(text(),'12PCS Plastic Car Radio Door Clip Panel Trim Dash ')]"
        self.add_cart_xpath = "//a[@id='isCartBtn_btn']"

    def choose (self):
        self.driver.find_element_by_xpath(self.choose_item_xpath).click()

    def add_cart(self):
        self.driver.find_element_by_xpath(self.add_cart_xpath).click()



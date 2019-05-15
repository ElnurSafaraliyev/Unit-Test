
class Search():

    def __init__(self,driver):
        self.driver = driver
        self.search_textbox_xpath = "//input[@id='gh-ac']"
        self.search_button_xpath = "//input[@id='gh-btn']"

    def write_item_for_search (self,items):
        self.driver.find_element_by_xpath(self.search_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.search_textbox_xpath).send_keys(items)

    def search_item (self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
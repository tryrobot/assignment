__author__ = 'mranjan'

from Utility.selenium_driver import SeleniumDriver



class HomePage(SeleniumDriver):

    def __init__(self,driver):

        self.driver=driver


    search_drop_down="searchDropdownBox"
    select_item="Books"
    search_box_id = "twotabsearchtextbox"
    search_text='data catalog'
    click_button="//*[@id='nav-search']/form/div[2]/div/input"


    def select_item_from_drop_down(self):
        return self.selectElement(self.select_item, self.search_drop_down, locatorType="id")

    def put_data_into_search_box(self):
        self.sendKeys(self.search_text, self.search_box_id, locatorType="id")

    def click_search_box(self):
        self.elementClick(self.click_button,locatorType="xpath")

    def title_of_page(self):
        return self.getTitle()
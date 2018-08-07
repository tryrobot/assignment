__author__ = 'mranjan'

from Utility.selenium_driver import SeleniumDriver
from PageObjectLocator import home_page
import Utility.custom_logger as cl
import logging


class HomePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):

        self.driver = driver

    def select_item_from_drop_down(self):
        self.log.info("Selecting item from the drop down menu")
        return self.selectElement(home_page.select_item, home_page.search_drop_down, locatorType="id")

    def put_data_into_search_box(self):
        self.log.info("Writing text into the search box to carry out the search")
        self.sendKeys(home_page.search_text, home_page.search_box_id, locatorType="id")

    def put_data_into_search_box_press_enter(self):
        self.log.info("Writing text into the search box and pressing Enter")
        self.sendKeysWithEnter(home_page.search_text, home_page.search_box_id, locatorType="id")

    def click_search_box(self):
        self.log.info("Clicking on the search action to search the entered text")
        self.elementClick(home_page.click_button,locatorType="xpath")

    def title_of_page(self):
        self.log.info("Fetching the title of the page.")
        return self.getTitle()
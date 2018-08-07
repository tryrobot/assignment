__author__ = 'mranjan'


from Utility.selenium_driver import SeleniumDriver
import Utility.custom_logger as cl
import logging
from PageObjectLocator import search_result_page


class SearchResultPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def select_nth_item_on_result_set(self):
        list_items=self.getElements(search_result_page.search_result_set.split('+')[1], locatorType=search_result_page.search_result_set.split('+')[0])
        return list_items

    def click_on_nth_item(self):
        self.log.info("Selecting the nth element from the list of search result page")
        self.elementClick(search_result_page.image_tag.split('-')[1], locatorType=search_result_page.image_tag.split('-')[0])

    def get_search_category_name(self):
        self.log.info("Getting the search category name as text")
        return self.get_value_of_element(search_result_page.search_category_xpath.split('-')[1], locatorType=search_result_page.search_category_xpath.split('-')[0])

    def get_search_text(self):
        self.log.info("Getting the text value of the search text entered in the search box")
        return self.get_value_of_element(search_result_page.search_text_xpath.split('+')[1], locatorType=search_result_page.search_text_xpath.split('+')[0])
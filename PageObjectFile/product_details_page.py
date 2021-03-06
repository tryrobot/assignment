from Utility.selenium_driver import SeleniumDriver
from PageObjectLocator import product_details_page
import Utility.custom_logger as cl
import logging


class ProductDetailsPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):

        self.driver=driver


    def get_title_cost_of_book(self):
        self.log.info("Getting the details of the product ")
        title=self.get_value_of_element(product_details_page.book_title_id.split('-')[1], locatorType=product_details_page.book_title_id.split('-')[0])
        kindle_cost = self.get_value_of_element(product_details_page.kindle_cost_id.split('-')[1], locatorType=product_details_page.kindle_cost_id.split('-')[0])
        paperback_cost=self.get_value_of_element(product_details_page.paperback_cost_id.split('-')[1], locatorType=product_details_page.paperback_cost_id.split('-')[0])
        return title, kindle_cost, paperback_cost

    def get_product_details_element(self):
        self.log.info("Getting the element which contains the details about the books")
        details_element=self.getElement(product_details_page.product_details_xpath.split('-')[1], locatorType=product_details_page.product_details_xpath.split('-')[0])
        return details_element

    def get_product_details(self):
        self.log.info("Getting the details of the item")
        details=self.getElements(product_details_page.details.split('-')[1], locatorType=product_details_page.details.split('-')[0])
        return details

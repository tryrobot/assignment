__author__ = 'mranjan'

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from traceback import print_stack
import Utility.custom_logger as cl
import logging
import time
import os

"""
Customized Selenium WebDriver class which contains all the useful methods that can be re used.
These methods help to in the following cases:
To reduce the time required to write automation script.
To log

"""


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getElements(self, locator, locatorType="id"):
        elements = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return elements


    def selectElement(self, visible_text, locator ,locatorType='id'):
        list_item=[]
        try:
            element=self.getElement(locator, locatorType)
            select=Select(element)
            list_item = select.options
            select.select_by_visible_text(visible_text)
            self.log.info(str(visible_text)+ " is successfully selected from the drop down ")
            return list_item
        except:
            self.log.error("Can not find the provided text in the drop down "+
                          "With locator "+locator+" locatorType: "+locatorType )
            print(print_stack())
            return list_item

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()


    def sendKeysWithEnter(self, data, locator ,locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data, Keys.ENTER)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def get_value_of_element(self, locator, locatorType="id"):
        self.log.info("Locating the element")
        element = self.getElement(locator, locatorType)
        return element.text



__author__ = 'mranjan'

from selenium import webdriver
from utility.set_logging import logger
from utility.set_properties import get_properties
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
"""
Setting up the browser to open the particular URL for other steps to follow.It will return the driver object which can be used for other
functionality.
"""


def open_browser_with_url(url, ff_binary='', ff_driver_path=''):
    try:
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False         # Setting up the browser marionette capability false to sync with ff version and selenium driver version
        binary = FirefoxBinary(ff_binary) # Setting up the location of firefox binary
        driver = webdriver.Firefox(firefox_binary=binary, executable_path=ff_driver_path)
        logger.debug('------------------------------------------------------------------------------------------')
        logger.debug('Opening the browser with the url : '+url)
        driver.get(url)
        driver.implicitly_wait(30)       # Setting up the wait for the whole session
        return driver
    except Exception as e:
        logger.error('Exception occurred while setting up the browser'+str(e))

"""
Reusable method to select the element form the drop down and also returning the list of item's name in the drop down
"""


def select_item_from_drop_down(driver, drop_down_element_id, item_name):
    try:
        logger.debug('Selecting the elements of the drop down menu')
        select = Select(driver.find_element_by_id(drop_down_element_id))    # Selecting all the elements in the drop down
        item_element = select.options                         # Making the list of elements available in the drop down
        drop_down_item_list = []                              # Initializing a  list variable
        for item in item_element:                             # Iterating through the elements and storing names of items in the list
                drop_down_item_list.append(item.text)
        logger.debug('The list of items in the drop down:\n'+str(drop_down_item_list))
        select.select_by_visible_text(item_name)            # Selecting the particular item from the list of items
        return drop_down_item_list                          # Returning the list of items in the drop down
    except NoSuchElementException as e:
        logger.error('No drop down item found or item is not there in the list: '+str(e))
"""
This method will search the item in the search box. It will take input for search text and the method by which the search will be carried out
"""


def search_item_in_search_box(driver,search_box_element_id,search_text,mode,xpath_for_click=''):
    try:
        logger.debug('Putting text in search box and searching for entered text item by : '+str(mode))
        if str(mode).lower()=='enter':
            driver.find_element_by_id(search_box_element_id).send_keys(search_text,Keys.ENTER)
        elif str(mode).lower()=='submit':
            driver.find_element_by_id(search_box_element_id).send_keys(search_text)
            driver.find_element_by_id(search_box_element_id).submit()
        elif str(mode).lower()=='click':
            driver.find_element_by_id(search_box_element_id).send_keys(search_text)
            driver.find_element_by_xpath(xpath_for_click).click()
        else:
            logger.error('Input not correct for the click/submit/Enter options')
    except (NoSuchElementException,TimeoutException) as e:
        logger.error('Unable to type item in the search box or Unable to click on search :'+str(e))


"""
Selecting the nth element from the search list page to view its details.
"""


def select_element_on_search_list_page(driver,element_no,item_list_xpath):
    try:
        element_no=int(element_no-1)
        logger.debug('Selecting the nth item from the search page results list')
        result_list_item=driver.find_element_by_xpath(item_list_xpath)       # selecting element containing all the result
        table_items=result_list_item.find_elements_by_tag_name('li')         # storing search results as list of elements
        table_items[int(element_no)].find_element_by_tag_name('img').click() # Clicking on the nth item to view the details
    except (NoSuchElementException,ArithmeticError,TypeError) as e:
        logger.error('Unable to view '+str(element_no)+'th element on the search result list page :'+str(e))



def get_text_property(driver,xpath):
    text_value=driver.find_element_by_xpath(xpath).text
    return str(text_value)

# properties=get_properties()
# url=properties['URL']
# binary=properties['FF_BINARY_LOCATION']
# loc=properties['DRIVER_LOCATION']
# element_id='searchDropdownBox'
# item='Books'
# search_box='twotabsearchtextbox'
# x="//*[@id='nav-search']/form/div[2]/div/input"
# item_list_x="//ul[@id='s-results-list-atf']"
# driver=open_browser_with_url(url,ff_binary=binary,ff_driver_path=loc)
# print(select_item_from_drop_down(driver,drop_down_element_id=element_id,item_name=item))
# search_item_in_search_box(driver,search_box,'data_catalog','Enter',x)
# select_element_on_search_list_page(driver,0,item_list_x)

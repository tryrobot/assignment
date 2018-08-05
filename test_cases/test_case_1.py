__author__ = 'mranjan'

from selenium.common.exceptions import NoSuchElementException,TimeoutException
from utility.set_logging import logger
from utility.generate_report import generate_report
from utility.set_properties import get_properties
from reusable_methods.reusable_methods import search_item_in_search_box,select_element_on_search_list_page
from reusable_methods.reusable_methods import open_browser_with_url,select_item_from_drop_down,get_text_property
import re,os

properties = get_properties()
url = properties['URL']
ff_binary_location = properties['FF_BINARY_LOCATION']
ff_driver_location = properties['DRIVER_LOCATION']
generate_report('Test Case','Status','w')


"""
Verify that amazon.com is successfully opened.
"""
try:
    test_case_1='Verify that amazon.com is successfully opened.'

    driver = open_browser_with_url(url, ff_binary=ff_binary_location, ff_driver_path=ff_driver_location)

    if 'amazon' in str(driver.title).lower():          # checking the title of the page
        generate_report(test_case_1,'Success', 'a')
        logger.debug('Test case successful to open the amazon.com')
    else:
        generate_report(test_case_1,'Failed', 'a')
        logger.error('Failed to open amazon.com')

    """
    Verify that there is search drop-down list to select the different items in store.
    """
    test_case_2 = 'Verify that there is search drop-down list to select the different items in store.'

    drop_down_element_id = 'searchDropdownBox'

    drop_down_item_select = 'Books'

    list_of_items_in_drop_down = select_item_from_drop_down(driver, drop_down_element_id=drop_down_element_id, item_name=drop_down_item_select)

    if not list_of_items_in_drop_down:
        generate_report(test_case_2,'Failed','a')
    else:
        generate_report(test_case_2,'Success','a')
        logger.debug('Drop down for list of items found\n'+str(list_of_items_in_drop_down))

    """
    Verify that in the search drop-down list there is option called 'Books'.
    Verify that 'Books' option is successfully selected from the drop-down menu.
    """
    test_case_3 = 'Verify that in the search drop-down list there is option called \'Books\'.'

    test_case_4 = 'Verify that \'Books\' option is successfully selected from the drop-down menu.'

    if drop_down_item_select in list_of_items_in_drop_down:
        generate_report(test_case_3, 'Success', 'a')
        generate_report(test_case_4, 'Success', 'a')
    else:
        generate_report(test_case_3, 'Failed', 'a')
        generate_report(test_case_4, 'Failed', 'a')


    """
    Verify that there is search box to search the user's choice of item.
    """
    test_case_5 = "Verify that search text can be entered successfully in search box and pressing Enter, searches the item."

    search_box_id = 'twotabsearchtextbox'

    search_text='data_catalog'

    search_mode=['enter','submit','click']

    search_item_in_search_box(driver, search_box_id, search_text, search_mode[0], '')

    logger.debug('Searching for the text \'results for\' on the current page\n')

    if 'results for' in driver.find_element_by_id('s-result-count').text:
        generate_report(test_case_5, 'Success', 'a')
    else:
        generate_report(test_case_5, 'Failed', 'a')
    logger.debug('Going back to the previous page')
    driver.back()

    test_case_6 = "Verify that search text can be entered successfully in search box using Submit, searches the item."

    search_item_in_search_box(driver, search_box_id, search_text, search_mode[1], '')

    logger.debug('Searching for the text \'results for\' on the current page\n')

    if 'results for' in driver.find_element_by_id('s-result-count').text:
        generate_report(test_case_6, 'Success', 'a')
    else:
        generate_report(test_case_6, 'Failed', 'a')
    logger.debug('Going back to the previous page')
    driver.back()

    test_case_7 = "Verify that search text can be entered successfully in search box using Click, searches the item."

    xpath_for_click_button=x="//*[@id='nav-search']/form/div[2]/div/input"

    search_item_in_search_box(driver, search_box_id, search_text, search_mode[2], xpath_for_click_button)

    logger.debug('Searching for the text \'results for\' on the current page\n')

    if 'results for' in driver.find_element_by_id('s-result-count').text:
        generate_report(test_case_7, 'Success', 'a')
    else:
        generate_report(test_case_7, 'Failed', 'a')

    """
    Verify that first element on the search result page is viewed.
    """
    test_case_8 = "Verify that first item on the search result page is viewed successfully."

    element_no = 1    # Element number you want to view from 1 to 10 only

    xpath_for_all_search_results_element = "//ul[@id='s-results-list-atf']"                # selecting result set element
    '''Clicking on nth element'''
    select_element_on_search_list_page(driver, element_no, xpath_for_all_search_results_element)

    '''Using regex to verify that first item is selected by retrieving the url'''
    current_uri = str(driver.current_url)
    logger.debug('Current URL :'+current_uri)
    uri_ref = re.search(r'ref=\w+', current_uri.replace('/', ' ')).group()

    if int(uri_ref[-1:]) == element_no:
        generate_report(test_case_8, 'Success', 'a')
    else:
        generate_report(test_case_8, 'Failed', 'a')

    xpath_book_title = "//*[@id='productTitle']"
    xpath_kindle_cost= "//*[@id='mediaTab_heading_0']/a"
    xpath_paperback_cost = "//*[@id='mediaTab_heading_1']/a"
    xpath_product_details = "//*[@id='productDetailsTable']/tbody/tr/td/div/ul"
    product_details=driver.find_element_by_xpath(xpath_product_details)
    elements_product_details=product_details.find_elements_by_tag_name('li')  # element list of details about product

    '''Preparing the details about the book details in reports directory'''
    details_file_path = os.path.join(os.path.dirname(os.getcwd()), 'reports','book_details.txt')
    with open(details_file_path, 'w') as fp:
        fp.write('Details of the book are as follows ::\n')
        fp.write('Name = ')
        fp.write(get_text_property(driver, xpath_book_title))
        fp.write('\n')
        kindle_cost = get_text_property(driver, xpath_kindle_cost)
        fp.write(str(kindle_cost).replace('\n',' = '))
        fp.write('\n')
        paperback_cost=get_text_property(driver,xpath_paperback_cost)
        fp.write(str(paperback_cost).replace('\n',' = '))
        fp.write('\n')
        for detail in elements_product_details[:6]:
            fp.write(str(detail.text).replace(':',' = '))
            fp.write('\n')
        fp.write(str(elements_product_details[6].text).split('(')[0])
    logger.debug('Congratulations! Test Execution is Successful\n'+'Please check reports directory for detailed report.')
    driver.close()
except (NoSuchElementException, TimeoutException,  TypeError, AttributeError) as e:
    logger.error('Exception occurred while executing test cases:'+str(e))
    generate_report(' ', ' ', 'a')
    generate_report('Exception occurred for rest of test cases. Please check logs for more details', 'Failed', 'a')


# item_list_x="//ul[@id='s-results-list-atf']"
#x="//*[@id='nav-search']/form/div[2]/div/input"

# print()
# select_element_on_search_list_page(driver,0,item_list_x)
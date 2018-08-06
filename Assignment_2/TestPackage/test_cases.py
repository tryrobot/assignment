__author__ = 'mranjan'


from ConfigVar import envrionment_details
import unittest
from selenium import webdriver
from PageObjectFile.home_page import HomePage
from PageObjectFile.product_details_page import ProductDetailsPage
from PageObjectFile.search_result_page import SearchResultPage
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pytest
import os, re


class TestAssignment(unittest.TestCase):
    url = envrionment_details.URL
    ff_binary = envrionment_details.FF_BINARY_LOCATION
    driver_location = envrionment_details.DRIVER_LOCATION
    cap = DesiredCapabilities().FIREFOX
    # Setting up the browser marionette capability false to sync with ff version and selenium driver version
    cap["marionette"] = False
    # Setting up the location of firefox binary
    binary = FirefoxBinary(ff_binary) # Setting up the location of firefox binary
    driver = webdriver.Firefox(firefox_binary=binary, executable_path=driver_location)
    driver.get(url)
    driver.implicitly_wait(30)
    home_page_obj = HomePage(driver)
    product_details_obj = ProductDetailsPage(driver)
    search_result_obj = SearchResultPage(driver)

    '''Test case to select item from drop down '''
    @pytest.mark.run(order=1)
    def test01_select_item_from_drop_down(self):
        # list of drop down elements
        drop_down_list = self.home_page_obj.select_item_from_drop_down()
        item_list = []
        # items in the drop down
        for item in drop_down_list:
            item_list.append(item.text)
        title = self.home_page_obj.title_of_page()
        '''this assertion will ensure that we are able to open the current website as the title of the matches
        with amazon.com '''
        assert 'amazon' in str(title).lower()
        '''this assertion will ensure that we are able to able the same url as provided by the user'''
        assert self.url in str(self.driver.current_url)
        ''' checking if the item provided is there in the list of items in drop down. This will ensure that given category is
        present in the drop down.'''
        assert str(self.home_page_obj.select_item) in item_list

    '''Test case to put data into the search box and going to the search results page'''
    @pytest.mark.run(order=2)
    def test02_input_to_search_box(self):
        # putting data into the search box
        self.home_page_obj.put_data_into_search_box()
        # clicking on the search box click option
        self.home_page_obj.click_search_box()
        '''this assertion will ensure that search has been carried out for the text entered by the user '''
        assert str(self.home_page_obj.search_text)==str(self.search_result_obj.get_search_category_name()).replace("\"",'')
        '''This assertion will ensure that search has been carried out for correct category as entered by user'''
        assert str(self.home_page_obj.select_item)==str(self.search_result_obj.get_search_text())

    '''Opening the details of the nth item'''
    @pytest.mark.run(order=3)
    def test03_select_first_element(self):
        # list of elements on the search result page
        list_of_elements=self.search_result_obj.select_nth_item_on_result_set()
        # Selecting the first item on the search result page by changing the driver
        self.search_result_obj = SearchResultPage(list_of_elements[int(self.search_result_obj.item_no)-1])
        # Clicking on the first result item selected above
        self.search_result_obj.click_on_nth_item()
        self.search_result_obj = SearchResultPage(self.driver)
        # Getting current url
        current_uri = str(self.driver.current_url)
        # Parsing current uri to extract the element number.
        uri_ref = re.search(r'ref=\w+', current_uri.replace('/', ' ')).group()
        '''this assertion will check that only the nth element is viewed on the search
        results by parsing the url of the page which contains the item number in it'''
        self.assertEqual(uri_ref[-1:],str(self.search_result_obj.item_no))

    '''Storing the details of the item in the text file'''
    @pytest.mark.run(order=4)
    def test04_get_details(self):
        book_title,kindle_cost,paperback_cost=self.product_details_obj.get_title_cost_of_book()
        element = self.product_details_obj.get_product_details_element()
        self.product_details_obj = ProductDetailsPage(element)
        details = self.product_details_obj.get_product_details()
        details_file_path = os.path.join(os.path.dirname(os.getcwd()), 'Reports','book_details.txt')
        with open(details_file_path, 'w') as fp:
            fp.write('Details of the book are as follows ::\n')
            fp.write('Name = ')
            fp.write(book_title)
            fp.write('\n')
            fp.write(str(kindle_cost).replace('\n',' = '))
            fp.write('\n')
            fp.write(str(paperback_cost).replace('\n',' = '))
            fp.write('\n')
            for detail in details[:6]:
                fp.write(str(detail.text).replace(':',' = '))
                fp.write('\n')
            fp.write(str(details[6].text).split('(')[0])
        '''this assertion ensures that a file exists for the details or not'''
        assert os.path.exists(details_file_path)


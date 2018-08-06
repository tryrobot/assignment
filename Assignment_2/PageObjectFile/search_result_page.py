__author__ = 'mranjan'


from Utility.selenium_driver import SeleniumDriver

class SearchResultPage(SeleniumDriver):

    search_result_set="//ul[@id='s-results-list-atf']/li"
    item_no=1
    image_tag="img"
    search_category_xpath="//*[@id='bcKwText']"
    search_text_xpath="//*[@class='a-link-normal a-color-base a-text-bold a-text-normal']"

    def select_nth_item_on_result_set(self):
        list_items=self.getElements(self.search_result_set, locatorType='xpath')
        return list_items

    def click_on_nth_item(self):
        self.elementClick(self.image_tag, locatorType="tag")

    def get_search_category_name(self):
        return self.get_value_of_element(self.search_category_xpath, locatorType="xpath")

    def get_search_text(self):
        return self.get_value_of_element(self.search_text_xpath, locatorType="xpath")
from Utility.selenium_driver import SeleniumDriver



class ProductDetailsPage(SeleniumDriver):

    def __init__(self,driver):

        self.driver=driver

    book_title_id = "productTitle"
    kindle_cost_id = "mediaTab_heading_0"
    paperback_cost_id = "mediaTab_heading_1"
    product_details_xpath = "//*[@id='productDetailsTable']/tbody/tr/td/div/ul"
    details = "li"

    def get_title_cost_of_book(self):
        title=self.get_value_of_element(self.book_title_id, locatorType="id")
        kindle_cost = self.get_value_of_element(self.kindle_cost_id, locatorType= "id")
        paperback_cost=self.get_value_of_element(self.paperback_cost_id, locatorType="id")
        return title,kindle_cost,paperback_cost

    def get_product_details_element(self):
        details_element=self.getElement(self.product_details_xpath, locatorType="xpath")
        return details_element

    def get_product_details(self):
        details=self.getElements(self.details, locatorType="tag")
        return details

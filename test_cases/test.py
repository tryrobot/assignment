__author__ = 'mranjan'

from selenium import webdriver
import sys
import selenium
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# sys.path.append('D:\\Python\\Scripts\\geckodriver.exe')
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
binary=FirefoxBinary(r'D:\Mozilla/firefox.exe')
driver=webdriver.Firefox(firefox_binary=binary,executable_path=r'D:\Python\Scripts\geckodriver.exe')
driver.implicitly_wait(60)
driver.get('https://amazon.com')
a=driver.title
print(a)
if 'amazon' in str(a).lower():
    print(True)
else:
    print(False)
select=Select(driver.find_element_by_id('searchDropdownBox'))

print(len(select.options))
b=select.options
item_list=[]
for bb in b:
    a=(bb.text)
    item_list.append(a)
print(item_list)


driver.find_element_by_id('twotabsearchtextbox').send_keys('data catalog')
driver.find_element_by_id('twotabsearchtextbox').submit()
b=driver.find_element_by_id('s-result-count')
print(b.text)
print(b.get_attribute('span'))

# driver.find_element_by_xpath("//*[@id='bcKwText']/span").text
# driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()

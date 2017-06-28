#encoding=utf-8
from Action.login import login
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepository
import time

class HomePage(object):
    u"""首页"""
    def __init__(self, driver):
        self.driver = driver
        self.parsePOR = ParsePageObjectRepository()
        self.home_page_items = self.parsePOR.getItemsFromSection("126mail_homepage")

    def addressbook_link(self):
        # 通讯录
        return self.returnElement('homepage.addressbookbtn')

    def returnElement(self, option):
        locateType, locateExpression = self.home_page_items[option].split('>')
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="d:\\chromedriver")
    driver.get("http://mail.126.com")
    time.sleep(5)
    login(driver, 'sjjm0001', '11111q')
    time.sleep(5)
    home_page = HomePage(driver)
    print home_page.addressbook_link()



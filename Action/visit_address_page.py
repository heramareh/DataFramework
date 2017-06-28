#encoding=utf-8

from selenium import webdriver
from Action.login import login
from PageObject.home_page import HomePage
import time

def visit_address_page(driver):
    u"""访问通讯录页面"""
    home_page = HomePage(driver)
    home_page.addressbook_link().click()

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="d:\\chromedriver")
    driver.get("http://mail.126.com")
    time.sleep(5)
    login(driver, 'sjjm0001', '11111q')
    time.sleep(5)
    visit_address_page(driver)

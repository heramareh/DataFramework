#encoding=utf-8
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepository
import time

class LoginPage(object):
    u"""登录页"""
    def __init__(self, driver):
        self.driver = driver
        self.parsePOR = ParsePageObjectRepository()
        self.login_page_items = self.parsePOR.getItemsFromSection("126mail_login")

    def frame(self):
        return self.returnElement('loginpage.frame')

    def username(self):
        # 用户名
        return self.returnElement('loginpage.username')

    def password(self):
        # 密码
        return self.returnElement('loginpage.password')

    def login_btn(self):
        # 登录
        return self.returnElement('loginpage.loginbtn')

    def continuelogin_btn(self):
        # 继续登录
        return self.returnElement('loginpage.continuelogin')

    def returnElement(self, option):
        locateType, locateExpression = self.login_page_items[option].split('>')
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="d:\\chromedriver")
    driver.get("http://mail.126.com")
    time.sleep(5)
    login_page = LoginPage(driver)
    driver.switch_to.frame(login_page.frame())
    login_page.username().send_keys('sjjm0001')
    login_page.password().send_keys('11111q')
    login_page.login_btn().click()


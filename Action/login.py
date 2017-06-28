#encoding=utf-8

from selenium import webdriver
from PageObject.login_page import LoginPage
import time

def login(driver, username, password):
    u"""登录"""
    login_page = LoginPage(driver)
    driver.switch_to.frame(login_page.frame())
    # 用户名
    login_page.username().send_keys(username)
    # 密码
    login_page.password().send_keys(password)
    # 登录
    login_page.login_btn().click()
    # 继续登录
    login_page.continuelogin_btn().click()
    driver.switch_to.default_content()

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="d:\\chromedriver")
    driver.get("http://mail.126.com")
    time.sleep(5)
    login(driver, 'sjjm0001', '11111q')
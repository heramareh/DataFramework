#encoding=utf-8

from selenium import webdriver
from Action.login import login
from Action.visit_address_page import visit_address_page
from PageObject.addressbook_page import AdderssBookPage
import time

def addcontacts(driver, name, mail, mobile, comment, is_set_star):
    u"""新建联系人"""
    addressbook_page = AdderssBookPage(driver)
    # 点击新建联系人按钮
    addressbook_page.createcontacts_btn().click()
    # 姓名
    addressbook_page.contact_personname().send_keys(name)
    # 邮箱
    addressbook_page.contact_personemail().send_keys(mail)
    # 设为星标联系人
    if is_set_star == u'是':
        addressbook_page.starcontacts_cbox().click()
    # 手机号码
    addressbook_page.contact_personmobile().send_keys(mobile)
    # 备注
    if comment:
        addressbook_page.contact_personcomment().send_keys(comment)
    # 保存
    addressbook_page.savecontaceperson().click()

def cancleaddcontact():
    u"""取消新建"""
    addressbook_page = AdderssBookPage(driver)
    addressbook_page.canclecontaceperson().click()

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="d:\\chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://mail.126.com")
    # 登录
    login(driver, 'sjjm0001', '11111q')
    # 进入通讯录页签
    visit_address_page(driver)
    time.sleep(1)
    # 新建联系人
    addcontacts(driver, u'李旺', u'8926924@qq.com', u'18888888888', u'光荣之路自动化测试')
    time.sleep(2)
    # 断言
    assert u'李旺' in driver.page_source,u'新建联系人失败'
    print u'新建联系人成功'
    driver.quit()
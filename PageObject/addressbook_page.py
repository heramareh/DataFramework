#encoding=utf-8
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepository
import time

class AdderssBookPage(object):
    u"""通讯录页"""
    def __init__(self, driver):
        self.driver = driver
        self.parsePOR = ParsePageObjectRepository()
        self.addcontacts_page_items = self.parsePOR.getItemsFromSection("126mail_addcontactspage")

    def createcontacts_btn(self):
        # 新建联系人按钮
        return self.returnElement('addcontactspage.createcontactsbtn')

    def contact_personname(self):
        # 新建联系人-姓名
        return self.returnElement('addcontactspage.contactpersonname')

    def contact_personemail(self):
        # 新建联系人-邮箱
        return self.returnElement('addcontactspage.contactpersonemail')

    def starcontacts_cbox(self):
        # 新建联系人-设为星标联系人勾选框
        return self.returnElement('addcontactspage.starcontacts')

    def contact_personmobile(self):
        # 新建联系人-手机号码
        return self.returnElement('addcontactspage.contactpersonmobile')

    def contact_personcomment(self):
        # 新建联系人-备注
        return self.returnElement('addcontactspage.contactpersoncomment')

    def savecontaceperson(self):
        # 新建联系人-保存
        return self.returnElement('addcontactspage.savecontaceperson')

    def canclecontaceperson(self):
        # 新建联系人-取消
        return self.returnElement('addcontactspage.canclecontaceperson')

    def returnElement(self, option):
        locateType, locateExpression = self.addcontacts_page_items[option].split('>')
        # print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

if __name__ == '__main__':
    pass


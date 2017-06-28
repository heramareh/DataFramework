#encoding=utf-8

import time
import traceback

from selenium import webdriver
from Action.address_book import addcontacts
from Action.login import login
from Action.visit_address_page import visit_address_page
from ProjectVar import var
from Util.Excel import ParseExcel
from Util.Log import *

if __name__ == '__main__':
    pe = ParseExcel(var.test_data_excel_path)
    datas = pe.get_all_rows()
    for row_num in xrange(1, len(datas)):
        try:
            is_run = datas[row_num][4].value
            if is_run == 'y':
                username = datas[row_num][var.username_col_no].value
                password = datas[row_num][var.password_col_no].value
                driver = webdriver.Chrome(executable_path="d:\\chromedriver")
                driver.maximize_window()
                driver.implicitly_wait(10)
                driver.get("http://mail.126.com")
                # 登录
                login(driver, username, password)
                # 进入通讯录页签
                visit_address_page(driver)
                time.sleep(1)
                pe.get_sheet_by_name(u'联系人')
                datas_contact = pe.get_all_rows()
                for contact_row_num in xrange(1, len(datas_contact)):
                    try:
                        name, mail, is_set_star, mobile, comment, assert_key, is_add_contact = [x.value for x in datas_contact[contact_row_num]][1:8]
                        # print name, mail, is_set_star, mobile, comment, assert_key, is_add_contact
                        if is_add_contact == 'y':
                            # 新建联系人
                            addcontacts(driver, name, mail, mobile, comment, is_set_star)
                            time.sleep(2)
                            # 断言
                            assert assert_key in driver.page_source
                            info(u'新建联系人成功')
                            pe.write_cell_content(contact_row_num + 1, 10, u'成功')
                            pe.write_cell_current_time(contact_row_num + 1, 9)
                        else:
                            pe.write_cell_content(contact_row_num+1, 10, u'跳过')
                    except:
                        pe.write_cell_content(contact_row_num + 1, 10, u'失败')
                        pe.write_cell_current_time(contact_row_num + 1, 9)
                        error(str(traceback.format_exc()))
                pe.get_sheet_by_name(u'126账号')
                pe.write_cell_content(row_num+1, 6, u'成功')
                pe.write_cell_content(row_num+1, 7, u'')
            else:
                pe.get_sheet_by_name(u'126账号')
                pe.write_cell_content(row_num+1, 6, u'跳过')
                pe.write_cell_content(row_num+1, 7, u'')
        except:
            pe.get_sheet_by_name(u'126账号')
            pe.write_cell_content(row_num+1, 6, u'失败')
            pe.write_cell_content(row_num+1, 7, str(traceback.format_exc()))
            error(str(traceback.format_exc()))
        finally:
            driver.quit()

#encoding=utf-8
import os

#获取工程所在的目录的绝对路径
project_path = os.path.dirname(os.path.dirname(__file__))
page_object_repository_path = os.path.join(project_path, "Config", "PageObjectRepository.ini")
test_data_excel_path = os.path.join(project_path, "TestData", u"126邮箱联系人.xlsx")

username_col_no = 1
password_col_no = 2

if __name__ == '__main__':
    print project_path
    print page_object_repository_path
    print test_data_excel_path
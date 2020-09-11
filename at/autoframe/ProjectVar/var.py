# -*- coding:utf-8 -*-

import os

#获取工程所在目录的绝对路径
project_path = os.path.dirname(os.path.dirname(__file__))
#日志配置文件的绝对路径
log_config_file_path = project_path + "/Conf/logger.conf"
#测试数据excel文件的绝对路径
test_data_excel_path = project_path.encode('utf-8').decode("utf-8") + u"/TestData/联系人.xlsx"
#
page_object_repository_path = project_path.encode('utf-8').decode("utf-8") + "/Conf/PageProjectRepository.ini"

username_col_no=1
password_col_no=2
is_executed_col_no=4
test_result_col_no=6
exception_info_col_no=7
assert_keyword_col_no = 6
firefox_driver_path= 'D:\\geckodriver'

if __name__ == "__main__":
    print(os.path.dirname(__file__))
    print(os.path.dirname(os.path.dirname(__file__)))
    print(os.path.dirname(project_path+"/Conf/logger.conf")) #路径斜杠向左向右都可以
    print(log_config_file_path)
    print(test_data_excel_path)
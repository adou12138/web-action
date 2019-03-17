# coding: utf-8
# web-action 
# contans 
# shen 
# 2019/3/17 11:07 

import os
# 项目绝对路径地址
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

datas_dir = os.path.join(base_dir, "datas")
login_data = os.path.join(datas_dir, "login.py")

pages_dir = os.path.join(base_dir, "pages")
base_page = os.path.join(datas_dir, "base.py")
index_page = os.path.join(datas_dir, "index.py")
login_page = os.path.join(datas_dir, "login.py")
invest_page = os.path.join(datas_dir, "invest.py")

reports_dir = os.path.join(base_dir, "reports")
test_web_report = os.path.join(datas_dir, "test_web_report.py")
report_file = os.path.join(reports_dir, "luckytest.html")

testcase_dir = os.path.join(base_dir, "testcases")
test_login = os.path.join(datas_dir, "test_login.py")
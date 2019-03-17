# -*- coding: UTF-8 -*-
# 当前项目的名称: ui-action-po 
# 新文件名称：invest 
# 当前登录名：LuckyLu
# 创建日期：2019/3/15 16:39
# 文件IDE名称：PyCharm 

from selenium import webdriver

class Invest():
    '这个是测试投资的页面'

    def __init__(self, driver):
        self.driver = driver

    def invest(self):
        invest = self.driver.find_element_by_Xpath("//a[contains(@href,'loan/finance')]")


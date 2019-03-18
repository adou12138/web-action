# -*- coding: UTF-8 -*-
# 当前项目的名称: ui-action-po 
# 新文件名称：invest 
# 当前登录名：LuckyLu
# 创建日期：2019/3/15 16:39
# 文件IDE名称：PyCharm 

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage

class InvestPage(BasePage):
    '投资页面调用'
    bid_choose_button_locator = (By.XPATH, "//a[contains(@href, '5774') and @class='btn btn-special']")  # 抢投标

    bid_input_locator = (By.XPATH, "//input[@class='form-control invest-unit-investinput']")  # 投标输入
    bid_button_locator = (By.XPATH,"//button[@class ='btn btn-special height_style']")  # 投标按钮

    error_alert_locator = (By.XPATH, "//div[@class='text-center']")  # 错误弹出框
    #  //div[@class='layui-layer-content']
    error_alert_click_locator = (By.XPATH, "//a[@class='layui-layer-btn0']")  # 错误弹出框信息确认

    success_alert_locator = (By.XPATH, "//div[@id='layui-layer6']//div[@class='capital_font1 note'] ")  # 投标成功弹出框
    success_alert_click_locator = (By.XPATH, "//div[@id='layui-layer6']//button[contains(text(),'查看并激活')]")  # 成功弹出框信息确认

    # //button[contains(text(),'查看并激活')]

    # 年化收益://<div class="mt-5 bold red font_30 line_h40">12%</div>




    # def __init__(self, driver):
    #     self.driver = driver

    def invest(self):
        invest = self.driver.find_element_by_Xpath("//a[contains(@href,'loan/finance')]")

    def choose_bid_click_element(self):
        return self.get_visible_element(self.bid_choose_button_locator)


    def bid_input_element(self):
        return self.get_visible_element(self.bid_input_locator)

    def bid_button_element(self):
        return self.get_visible_element(self.bid_button_locator)

    # 错误alert
    def bid_error_alert_element(self):
        return self.get_invest_alert_element(self.error_alert_locator)

    def bid_error_alert_click_element(self):
        return self.get_invest_alert_element(self.error_alert_click_locator)

    # 成功alert
    def bid_success_alert_element(self):
        return self.get_invest_alert_element(self.success_alert_locator)

    def bid_success_alert_click_element(self):
        return self.get_invest_alert_element(self.success_alert_click_locator)


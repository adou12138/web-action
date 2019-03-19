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

class InvestPage(BasePage):  # 需要重新定义元素位置
    '投资页面调用'
    bid_choose_button_locator = (By.XPATH, "//a[contains(@href, '5774') and @class='btn btn-special']")  # 抢投标

    bid_input_locator = (By.XPATH, "//input[@class='form-control invest-unit-investinput']")  # 投标输入
    bid_button_locator = (By.XPATH, "//button[@class ='btn btn-special height_style']")  # 投标按钮
    # 空格用contains来定位
    # bid_error_alert_locator = (By.XPATH, "//div[@class='text-center']")  # 错误弹出框-文字提示
    bid_error_message_locator = (By.XPATH, "//div[@id='layui-layer1']")  # 错误弹出框
    bid_error_message_click_locator = (
        By.XPATH, "//div[@class='layui-layer layui-anim layui-layer-dialog ']//a[@class='layui-layer-ico layui-layer-close layui-layer-close1']")  # 错误弹出框信息确认

# 有空格用contains，需要改
    bid_success_message_locator = (
        By.XPATH, "//div[@class='layui-layer layui-anim layui-layer-page ']//div[@class='capital_ts']")  # 投标成功弹出框
    bid_success_message_click_locator = (By.XPATH, "//div[@id='layui-layer2']//img[@src='/Public/frontend/images/close_pop.png']")
    # X关闭
    # //div[@id='layui-layer6']//button[contains(text(),'查看并激活')]  # 提示文字

    # def __init__(self, driver):
    #     self.driver = driver
    """
    确认下要不要
    def invest(self):
        invest = self.driver.find_element_by_Xpath("//a[contains(@href,'loan/finance')]")

    def choose_bid_click_element(self):
        return self.get_visible_element(self.bid_choose_button_locator)
    """

    @property
    def bid_input_element(self):  # WebElement
        return self.get_visible_element(self.bid_input_locator)

    @property
    def bid_button_element(self):  # WebElement
        return self.get_visible_element(self.bid_button_locator)
# 添加.click事件
    def click_bid_button_element(self):
        return self.bid_button_element.click()

    # 成功message
    @property
    def bid_success_message_element(self):
        return self.get_visible_element(self.bid_success_message_locator)

    def bid_success_message_text_element(self):
        return self.bid_success_message_element.text

    # 比对投资前后的金额
    def data_amount(self):
        """

        :return:
        """
        return self.bid_input_element.get_attribute('data-amount')

    def bid_success_message_click_element(self):
        return self.get_visible_element(self.bid_success_message_click_locator)


    # 错误message
    def bid_error_message_element(self):
        return self.get_visible_element(self.bid_error_message_locator)

    def bid_error_message_click_element(self):
        return self.get_visible_element(self.bid_error_message_click_locator)


    def clear_bid_element(self):
        pass
    """
    alert
    def bid_error_alert_element(self):
        return self.get_invest_alert_element(self.error_alert_locator)

    def bid_error_alert_click_element(self):
        return self.get_invest_alert_element(self.error_alert_click_locator)

    def bid_success_alert_element(self):
        return self.get_invest_alert_element(self.success_alert_locator)

    def bid_success_alert_click_element(self):
        return self.get_invest_alert_element(self.success_alert_click_locator)
    """
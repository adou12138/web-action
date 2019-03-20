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
    # '投资页面调用'    空格用contains来定位
    # bid_choose_button_locator = (By.XPATH, "//a[contains(@href, '5774') and @class='btn btn-special']")  # 抢投标

    bid_input_locator = (By.XPATH, "//input[contains(@class,'form-control invest-unit-investinput')]")  # 投标输入
    bid_button_locator = (By.XPATH, "//button[contains(@class,'btn btn-special height_style')]")  # 投标按钮

    bid_error_pop_locator = (By.XPATH, "//div[@class='text-center']")  # 错误弹出框-文字提示
    bid_error_pop_button_locator = (
        By.XPATH, "//button[contains(@class,'btn btn-special height_style')]")  # 错误弹出框-文字提示

    bid_error_pop_close_locator = (
        By.XPATH, "//a[contains(@class,'layui-layer-ico layui-layer-close layui-layer-close1')]")  # 错误弹出框信息确认

    bid_success_pop_locator = (
        By.XPATH, "//div[@class='layui-layer-content']//div[contains(@class,'capital_font1 note')]")  # 投标成功弹出框
    bid_success_pop_close_locator = (
        By.XPATH, "//div[@id='layui-layer1']//img[contains(@src,'/Public/frontend/images/close_pop.png')]")

    # def __init__(self, driver):
    #     self.driver = driver
    """
    不要了，直接定义在index页面
    def invest(self):
        invest = self.driver.find_element_by_Xpath("//a[contains(@href,'loan/finance')]")

    def choose_bid_click_element(self):
        return self.get_visible_element(self.bid_choose_button_locator)
    """

    def bid(self, money):
        self.bid_input_element.send_keys(money)

    @property
    def bid_input_element(self):  # WebElement
        return self.get_visible_element(self.bid_input_locator)

    @property
    def bid_button_element(self):  # WebElement
        return self.get_visible_element(self.bid_button_locator)

    def click_bid_button_element(self):
        return self.bid_button_element.click()

    # 投标成功
    @property
    def bid_success_pop_element(self):
        return self.get_visible_element(self.bid_success_pop_locator)

    def bid_success_pop_text_element(self):
        return self.bid_success_pop_element.text

    @property
    def bid_success_pop_close_element(self):
        return self.get_visible_element(self.bid_success_pop_close_locator)

    def bid_success_pop_close_element_click(self):
        return self.bid_success_pop_close_element.click()

    # 比对投资前后的金额
    def data_amount(self):
        """

        :return: data-amount
        """
        return self.bid_input_element.get_attribute('data-amount')

    # 错误pop
    @property
    def bid_error_pop_element(self):
        return self.get_visible_element(self.bid_error_pop_locator)

    def bid_error_pop_text_element(self):
        return self.bid_error_pop_element.text

    def bid_error_pop_close_element(self):
        return self.get_visible_element(self.bid_error_pop_close_locator)

    @property
    def bid_error_pop_button_element(self):
        return self.get_visible_element(self.bid_error_pop_button_locator)

    def bid_error_pop_button_text_element(self):
        return self.bid_error_pop_button_element.text

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
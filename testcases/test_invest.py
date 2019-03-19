# -*- coding: UTF-8 -*-
# 当前项目的名称: web-action 
# 新文件名称：test_invest 
# 当前登录名：LuckyLu
# 创建日期：2019/3/18 13:25
# 文件IDE名称：PyCharm 

import unittest
from selenium import webdriver
from pages.login import LoginPage  # 导入登录页面操作
from pages.index import IndexPage  # 导入首页
from pages.invest import InvestPage  # 导入投资
# from libext.ddtNew import ddt, data
from ddt import ddt, data
from datas import login  # 导入登录的数据
from datas import invest

@ddt
class TestInvest(unittest.TestCase):
    '这是测试投资的用例'

    @classmethod
    def setUpClass(cls):
        pass
        # cls.driver = webdriver.Chrome()
        # cls.driver.get("http://120.78.128.25:8765/index/login.html")
        # cls.driver.implicitly_wait(30)
        # cls.login_page = LoginPage(cls.driver)
        # cls.invest_page = InvestPage(cls.driver)
        #
        # cls.login_page.send_phone_element(login.user_currect_info['phone'])
        # cls.login_page.send_password_element(login.user_currect_info['password'])
        # cls.login_page.submit_element()
        #
        # cls.invest_page.choose_bid_click_element().click()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://120.78.128.25:8765/index/login.html")
        self.driver.implicitly_wait(30)
        self.login_page = LoginPage(self.driver)
        self.invest_page = InvestPage(self.driver)

        self.login_page.send_phone_element(login.user_currect_info['phone'])
        self.login_page.send_password_element(login.user_currect_info['password'])
        self.login_page.submit_element()

        self.invest_page.choose_bid_click_element().click()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*invest.bid_success_message)
    def test_invest(self, data):
        # self.login_page.send_phone_element("18684720553")
        # self.login_page.send_password_element("python")
        # self.login_page.submit_element()
        #
        # self.invest_page.choose_bid_click_element().click()

        self.invest_page.bid_input_element().click()
        self.invest_page.bid_input_element().send_keys(data['amount'])
        self.invest_page.bid_button_element().click()

        if self.invest_page.bid_success_message_element():
            # print(self.invest_page.bid_success_message_element().text)
            self.assertTrue(data['expected'] in self.invest_page.bid_success_message_element().text)
            self.invest_page.bid_success_message_click_element().click()
        else:
            # print(self.invest_page.bid_error_message_element().text)
            self.assertTrue(data['expected'] in self.invest_page.bid_error_message_element().text)
            self.invest_page.bid_error_message_click_element().click()

        # 分开写
    def test_bid_success(self):
            # 首页点击投标
        IndexPage(self.driver).bid()

            # 投标页面输入投标

            # 需要验证投资的金额 投资后的金额判断

    def test_bid_failed1(self):
        pass

    def test_bid_failed2(self):
        pass
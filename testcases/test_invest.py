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
import time

@ddt
class TestInvest(unittest.TestCase):
    '这是测试投资的用例'

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://120.78.128.25:8765/index/login.html")
        cls.driver.implicitly_wait(30)
        cls.login_page = LoginPage(cls.driver)
        cls.invest_page = InvestPage(cls.driver)
        cls.index_page = IndexPage(cls.driver)

        cls.login_page.send_phone_element(invest.user_currect_info['phone'])
        cls.login_page.send_password_element(invest.user_currect_info['password'])
        cls.login_page.submit_element()

        IndexPage(cls.driver).bid()

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()
        # self.driver.get("http://120.78.128.25:8765/index/login.html")
        # self.driver.implicitly_wait(30)
        # self.login_page = LoginPage(self.driver)
        # self.invest_page = InvestPage(self.driver)
        # self.index_page = IndexPage(self.driver)
        #
        # self.login_page.send_phone_element(invest.user_currect_info['phone'])
        # self.login_page.send_password_element(invest.user_currect_info['password'])
        # self.login_page.submit_element()

    def tearDown(self):
        pass
        # self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    """
    @unittest.skip('skip')
    @data(*invest.bid_success_pop)
    def test_invest(self, data):
        # self.login_page.send_phone_element("18684720553")
        # self.login_page.send_password_element("python")
        # self.login_page.submit_element()
        #
        # self.invest_page.choose_bid_click_element().click()

        self.invest_page.bid_input_element().click()
        self.invest_page.bid_input_element().send_keys(data['amount'])
        self.invest_page.bid_button_element().click()

        if self.invest_page.bid_success_pop_element():
            # print(self.invest_page.bid_success_message_element().text)
            self.assertTrue(data['expected'] in self.invest_page.bid_success_pop_element().text)
            self.invest_page.bid_success_pop_close_element().click()
        else:
            # print(self.invest_page.bid_error_message_element().text)
            self.assertTrue(data['expected'] in self.invest_page.bid_error_pop_element().text)
            self.invest_page.bid_error_pop_click_element().click()
    """
    # @unittest.skip('skip')
    @data(*invest.bid_success_pop)
    def test_bid_success(self, data):
        # 首页点击投标
        # IndexPage(self.driver).bid()
        # 投标页面输入投标
        before_amount = round(float(self.invest_page.data_amount()))
        # print(before_amount)

        self.invest_page.bid(data['amount'])
        self.invest_page.click_bid_button_element()

        # print(self.invest_page.bid_success_pop_text_element())
        # 断言
        try:
            self.assertTrue(data['expected'] in self.invest_page.bid_success_pop_text_element())
            print('Test Pass!')
        except AssertionError as e:
            print('Test Failed!!! AssertionError：{}'.format(e))
            raise e
        finally:
            self.driver.refresh()

        self.driver.refresh()
        # 需要验证投资的金额 投资后的金额判断
        after_amount = round(float(self.invest_page.data_amount()))
        # print(after_amount)
        try:
            self.assertTrue(before_amount - after_amount == int(data['amount']))
            print('Test Pass!')
        except AssertionError as e:
            print('Test Failed!!! AssertionError：{}'.format(e))
            raise e

    # @unittest.skip('skip')
    @data(*invest.bid_error_pop)
    def test_bid_failed1(self, data):
        # IndexPage(self.driver).bid()

        self.invest_page.bid(data['amount'])
        self.invest_page.click_bid_button_element()

        try:
            self.assertTrue(data['expected'] in self.invest_page.bid_error_pop_text_element())
            print('Test Pass!')
        except AssertionError as e:
            print('Test Failed!!! AssertionError：{}'.format(e))
            raise e
        finally:
            # self.invest_page.bid_error_pop_close_element()
            self.driver.refresh()

    # @unittest.skip('skip')
    @data(*invest.bid_error_pop_button)
    def test_bid_failed2(self, data):
        # IndexPage(self.driver).bid()

        self.invest_page.bid(data['amount'])
        # self.invest_page.click_bid_button_element()
        # print(self.invest_page.bid_error_pop_button_text_element())

        try:
            self.assertTrue(data['expected'] in self.invest_page.bid_error_pop_button_text_element())
            print('Test Pass!')
        except AssertionError as e:
            print('Test Failed!!! AssertionError：{}'.format(e))
            raise e
        finally:
            self.driver.refresh()
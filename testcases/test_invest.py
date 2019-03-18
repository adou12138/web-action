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


class TestInvest(unittest.TestCase):
    '这是测试投资的用例'

    @classmethod
    def setUpClass(cls):
        cls.url = "http://120.79.176.157:8012/index/login.html"
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.url)
        cls.driver.implicitly_wait(30)
        cls.login_page = LoginPage(cls.driver)
        cls.invest_page = InvestPage(cls.driver)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @unittest.skip("忽略")
    def test_invest_0_failed(self):
        self.login_page.send_phone_element("18684720553")
        self.login_page.send_password_element("python")
        self.login_page.submit_element()

        self.invest_page.choose_bid_click_element().click()

        self.invest_page.bid_input_element().click()
        self.invest_page.bid_input_element().send_keys("10")
        self.invest_page.bid_button_element().click()

        self.assertTrue("投标金额必须为100的倍数" in self.invest_page.bid_error_alert_element().text)

    # alert = driver.switch_to.alert  # 通过变量来接收alert，是全局的，只有一次，不需要定位





    @unittest.skip("忽略")
    def test_invest_1_success(self):
        self.login_page.send_phone_element("18684720553")
        self.login_page.send_password_element("python")
        self.login_page.submit_element()

        self.invest_page.choose_bid_click_element().click()

        self.invest_page.bid_input_element().click()
        self.invest_page.bid_input_element().send_keys("100")
        self.invest_page.bid_button_element().click()

        success = self.invest_page.bid_success_alert_element()
        print(success, type(success))

        # self.assertTrue("投标成功" in self.invest_page.bid_success_alert_element().text)
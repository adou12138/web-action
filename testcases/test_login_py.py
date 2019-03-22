# coding: utf-8
# ui-action-po 
# index 
# shen 
# 2019/3/16 12:20

import sys
sys.path.append("../")

import unittest
from selenium import webdriver
from pages.login import LoginPage  # 导入登录页面操作
from pages.index import IndexPage  # 导入首页
# from libext.ddtNew import ddt, data
# from ddt import ddt, data
from datas import login  # 导入登录的数据

from common import logger
my_logger = logger.get_logger(logger_name="login")
import pytest


@pytest.mark.all
@pytest.mark.usefixtures('my_class_login')
class TestLogin:
    '这个是一个测试登录的类'
    @classmethod  # 类方法，实例方法，静态方法 cls
    def setUpClass(cls):
        pass
        # cls.url = "http://120.78.128.25:8765/Index/login.html"
        # cls.driver = webdriver.Chrome()
        # cls.driver.get(cls.url)
        # cls.driver.implicitly_wait(30)
        # cls.login_page = LoginPage(cls.driver)

    def setUp(self):
        pass
        # print('Test Start')
        # self.login_page.clear_phone()
        # self.login_page.clear_password()

    def tearDown(self):
        pass
        # print('Test End')

        # self.login_page.clear_phone()
        # self.login_page.clear_password()

    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.close()  # 加了会拖慢加载速度
        # cls.driver.quit()

    @pytest.mark.smoke
    @pytest.mark.usefixtures('init_driver')
    @pytest.mark.parametrize('data', login.user_error_info)
    def test_login_0_failed(self, data, my_class_login):
        driver, login_page = my_class_login
        # 字典，列表+ddt，来保存登录的用例
        # print("phone: ", data['phone'])
        # print("password: ", data['password'])

        # self.login_page.submit_userinfo(data['phone'], data['password'])
        login_page.send_phone_element(data['phone'])
        login_page.send_password_element(data['password'])
        login_page.submit_element()

        try:
            # self.assertTrue(data['expected'] == self.login_page.alert_info().text)
            assert data['expected'] == login_page.alert_info().text
            print('Test Pass!')
        except AssertionError as e:
            print('Test Failed!!! AssertionError：{}'.format(e))
            raise e

    @pytest.mark.test
    @pytest.mark.usefixtures('init_driver')
    @pytest.mark.parametrize('data', login.user_error_js_info)
    def test_login_1_unauthorizon(self, data, my_class_login):
        # print("phone: ", data['phone'])
        # print("password: ", data['password'])
        # self.login_page.submit_userinfo(data['phone'], data['password'])

        driver, login_page = my_class_login
        login_page.send_phone_element(data['phone'])
        login_page.send_password_element(data['password'])
        login_page.submit_element()

        try:
            # self.assertTrue(data['expected'] == login_page.unauthorizon_info().text)
            assert data['expected'] == login_page.unauthorizon_info().text
            print('Test Pass!')
        except AssertionError as e:
            print('Test Failed!!! AssertionError：{}'.format(e))
            raise e

    @pytest.mark.success
    @pytest.mark.usefixtures('init_driver')
    @pytest.mark.parametrize('data', login.user_currect_info)
    def test_login_2_success(self, data, my_class_login):
        driver, login_page = my_class_login
        # self.login_page.submit_userinfo("18684720553", "python")

        login_page.send_phone_element(data['phone'])
        login_page.send_password_element(data['password'])
        login_page.submit_element()

        try:
            # self.assertTrue("小小蜜蜂" in user_ele.text)
            # self.assertTrue(data['expected'] in IndexPage(self.driver).get_user().text)
            assert data['expected'] in IndexPage(driver).get_user().text
            print('Test Pass!')
        except AssertionError as e:
            print('Test Failed!!! AssertionError：{}'.format(e))
            raise e
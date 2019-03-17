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
from ddt import ddt, data
from datas import login  # 导入登录的数据

# import logging
# logging.basicConfig(filename="test.log", level="INFO")
# my_log = logging.getLogger()

@ddt
class TestLogin(unittest.TestCase):
    '这个是一个测试登录的类'
    @classmethod  # 类方法，实例方法，静态方法 cls
    def setUpClass(cls):
        cls.url = "http://120.79.176.157:8012/index/login.html"
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.url)
        cls.driver.implicitly_wait(30)
        cls.login_page = LoginPage(cls.driver)

    def setUp(self):
        pass

    def tearDown(self):
        self.login_page.clear_phone()
        self.login_page.clear_password()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()  # 加了会拖慢加载速度
        cls.driver.quit()

    @unittest.skip("忽略")
    def test_login_2_success(self):
        """
        phone: 18819340103
        pwd: 123456
        :return:
        """

        # phone = WebDriverWait(self.driver, 20).until(ec.element_located_to_be_selected(By.XPATH,"//input[@name='phone']"))
        # pwd = WebDriverWait(self.driver, 20).until(ec.element_located_to_be_selected(By.XPATH,"//input[@name='password']"))

        # phone_ele = self.driver.find_element_by_xpath("//input[@name='phone']")
        # pwd_ele = self.driver.find_element_by_xpath("//input[@name='password']")

        # phone_ele.send_keys("18684720553")
        # pwd_ele.send_keys("python")
        # pwd_ele.submit()

        # 断言
        # 账户的元素
        # user_ele = WebDriverWait(self.driver, 20).until(
        #     ec.visibility_of_element_located((By.XPATH, "//img[@class='mr-5']//..")))
        # user_ele = self.driver.find_element_by_xpath("//img[@class='mr-5']//..")

        self.login_page.submit_userinfo("18684720553", "python")
        # user_ele = WebDriverWait(self.driver, 20).until(
        #     ec.visibility_of_element_located((By.XPATH, "//img[@class='mr-5']//..")))
        # self.assertTrue("小小蜜蜂" == user_ele.text)

        user_ele = IndexPage(self.driver).get_user()
        self.assertTrue("小小蜜蜂" in user_ele.text)

    @data(*login.user_error_info)
    def test_login_0_failed(self, data):
        # 字典，列表+ddt，来保存登录的用例
        # print("phone: ", data['phone'])
        # print("password: ", data['password'])

        self.login_page.submit_userinfo(data['phone'], data['password'])
        self.assertTrue(data['expected'] == self.login_page.alert_info().text)

    # @unittest.skip("忽略此用例")
    @data(*login.user_error_js_info)
    def test_login_1_unauthorizon(self, data):
        # print("phone: ", data['phone'])
        # print("password: ", data['password'])

        self.login_page.submit_userinfo(data['phone'], data['password'])
        self.assertTrue(data['expected'] == self.login_page.unauthorizon_info().text)
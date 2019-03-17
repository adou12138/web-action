# coding: utf-8
# ui-action-po 
# index 
# shen 
# 2019/3/16 12:20 

import unittest

from class7_19_03_14.pages.login import Login
from ddt import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@ddt
class TestLogin(unittest.TestCase):
    '这个是一个测试登录的类'

    @classmethod
    def setUpClass(cls):
        cls.url = "http://120.79.176.157:8012/index/login.html"
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.url)
        cls.driver.implicitly_wait(30)
        cls.login_page = Login(cls.driver)

    def setUp(self):
        pass

    def tearDown(self):
        pass
        # self.driver.clear()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_login1_success(self):
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
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, "//img[@class='mr-5']//..")))
        self.assertTrue("小小蜜蜂" == user_ele.text)

    def test_login1_failed(self):
        self.login_page.submit_userinfo("", "")
        phone_msg = self.driver.find_element_by_xpath("//div[@class='form-error-info']")

        self.assertTrue("请输入手机号" == phone_msg.text)

    @unittest.skip("忽略此用例")
    def test_login2_noauthorizon(self):
        self.login_page.submit_userinfo("", "")

        flash_msg_ele = self.driver.find_element_by_xpath("//div[@class='layui-layer-content']")

        self.assertTrue("请输入手机号" == flash_msg_ele.text)


if __name__ == '__main__':
    pass


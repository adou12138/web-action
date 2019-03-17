# -*- coding: UTF-8 -*-
# 当前项目的名称: ui-action-po 
# 新文件名称：loginpage 
# 当前登录名：LuckyLu
# 创建日期：2019/3/15 14:12
# 文件IDE名称：PyCharm 

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage

class LoginPage(BasePage):
    '登录页面调用'

    # 用户的元素定位器
    phone_user_locator = (By.NAME, "phone")
    password_user_locator = (By.NAME, "password")
    unauthorizon_info_locator = (By.XPATH, "//div[@class='layui-layer-content']")

    # 继承 ==> BasePage

    # def __init__(self, driver):
    #     self.driver = driver

    # 颗粒度太大，需要简化
    def submit_userinfo(self, phone, password):
        phone_ele = self.driver.find_element_by_name("phone")
        pwd_ele = self.driver.find_element_by_name("password")

        # 需要等待
        # phone_ele = BasePage.get_visible_element(self.phone_user_locator)
        # pwd_ele = BasePage.get_visible_element(self.password_user_locator)

        # 输入内容
        phone_ele.send_keys(phone)
        pwd_ele.send_keys(password)

        # 提交信息
        phone_ele.submit()

        # time.sleep(5)  # 不要使用强制等待

    # 接受定义的复杂，不能接受调用的复杂（简化函数的调用，使用函数时只会使用函数名，而不会使用函数的内容）
    def get_phone_element(self):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((
            By.NAME, "phone")))

    def get_password_element(self):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((
            By.NAME, "password")))

    def alert_info(self):

        return self.driver.find_element_by_xpath("//div[@class='form-error-info']")

    def unauthorizon_info(self):
        return self.get_visible_element(self.unauthorizon_info_locator)
        # return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((
        #     By.XPATH, "//div[@class='layui-layer-content']")))

    def clear_phone(self):
        return self.get_phone_element().clear()

    def clear_password(self):
        return self.get_password_element().clear()

    def click_remember(self):
        pass


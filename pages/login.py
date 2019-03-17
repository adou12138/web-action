# -*- coding: UTF-8 -*-
# 当前项目的名称: ui-action-po 
# 新文件名称：loginpage 
# 当前登录名：LuckyLu
# 创建日期：2019/3/15 14:12
# 文件IDE名称：PyCharm 

import time

class Login:
    '登录页面调用'

    def __init__(self, driver):
        self.driver = driver

    def submit_userinfo(self, phone, password):
        phone_ele = self.driver.find_element_by_name("phone")
        pwd_ele = self.driver.find_element_by_name("password")

        # 输入内容
        phone_ele.send_keys(phone)
        pwd_ele.send_keys(password)

        # 提交信息
        phone_ele.submit()

        # time.sleep(5)

    def phone_submit(self, phone):
        return self.driver.find_element_by_name("phone")

    def password_submit(self, phone):
        return self.driver.find_element_by_name("password")

    def alert_info(self):
        return self.driver.find_element_by_xpath("//div[@class='form-error-info']")

    def js_error(self):
        return self.driver.find_element_by_xpath("//div[@class='layui-layer-content']")

    def clear_phone(self):
        return self.driver.find_element_by_name("phone").clear()

    def clear_password(self):
        return self.driver.find_element_by_name("password").clear()

    def click_remember(self):
        pass


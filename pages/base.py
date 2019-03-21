# coding: utf-8
# ui-action-po 
# base 
# shen 
# 2019/3/16 12:20

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome
import time

from common import contants

from common import logger
my_logger = logger.get_logger(logger_name="BasePage")

# import logging
# logging.basicConfig(filename="test.log", level="INFO")
# my_log = logging.getLogger()

class BasePage:
    '所有页面的父类'

    def __init__(self, driver: Chrome):  # 表示返回值
        self.driver = driver

    # 可以接受定义的复杂
    def get_visible_element(self, locator, eqc=20) -> WebElement:
        try:
            return WebDriverWait(self.driver, eqc).until(
                ec.visibility_of_element_located(locator))
        except Exception as e:
            my_logger.error("No this element{}!!!".format(e))
            self.driver.save_screenshot(contants.pictures_file+"{}.png".format(time.time()))

    # def get_visible_elements
    def switch_windows(self, name=None, fqc=20):  # 查看窗口跳转源代码
        # 等待
        if name is None:
            current_handle = self.driver.current_window_handle
            WebDriverWait(self.driver, fqc).until(ec.new_window_is_opened(current_handle))
            handles = self.driver.window_handles
            return self.driver.switch_to.window(handles[-1])
        self.driver.switch_to.window()

    def get_invest_alert_element(self, locator, eqc=20):
        try:
            return WebDriverWait(self.driver, eqc).until(
                ec.alert_is_present(locator))
        except Exception as e:
            my_logger.error("No this alert{}!!!".format(e))
            self.driver.save_screenshot(contants.pictures_file+"{}.png".format(time.time()))
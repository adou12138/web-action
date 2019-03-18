# coding: utf-8
# ui-action-po 
# base 
# shen 
# 2019/3/16 12:20

from webbrowser import Chrome

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
            # my_logger.info("test")
            return WebDriverWait(self.driver, eqc).until(
                ec.visibility_of_element_located(locator))
        except Exception as e:
            my_logger.error("No this element{}!!!".format(e))
            # self.driver.save_screenshot("test.jpg".format(time.time()))
            # self.driver.save_screenshot("log_dir/{}.jpg".format(time.time()))
            self.driver.save_screenshot(contants.pictures_file+"{}.jpg".format(time.time()))

    def get_invest_alert_element(self, locator, eqc=20):
        try:
            return WebDriverWait(self.driver, eqc).until(
                ec.alert_is_present(locator))
        except Exception as e:
            my_logger.error("No this alert{}!!!".format(e))
            self.driver.save_screenshot(contants.pictures_file+"{}.jpg".format(time.time()))
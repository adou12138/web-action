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
import logging

logging.basicConfig(filename="test.log", level="INFO")
my_log = logging.getLogger()

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
            my_log.error("No this element{}!!!".format(e))
            self.driver.save_screenshot("log_dir/{}.jpg".format(time.time()))

# coding: utf-8
# ui-action-po 
# base 
# shen 
# 2019/3/16 12:20
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging

# my_log = logging.log()

class BasePage:
    '所有页面的父类'

    def __init__(self, driver):
        self.driver = driver

    # 可以接受定义的复杂
    def get_visible_element(self, locator, eqc=20):
        try:
            WebDriverWait(self.driver, eqc).until(ec.visibility_of_element_located(locator))
        except Exception as e:
            print("No this element{}!!!".format(e))
        return WebDriverWait(self.driver, eqc).until(ec.visibility_of_element_located(locator))
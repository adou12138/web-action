# coding: utf-8
# ui-action-po 
# index 
# shen 
# 2019/3/16 22:51 

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage

class IndexPage(BasePage):
    'index page'
    index_locator = (By.XPATH, "//img[@class='mr-5']//..")
    bid_ele_locator = (By.XPATH, "//a[contains(@class,'btn btn-special') and contains(@href,'13090')]")

    # def __init__(self, driver):
    #     self.driver = driver

    def get_user(self):
        # return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((
        #     By.XPATH, "//img[@class='mr-5']//.."
        # )))
        return self.get_visible_element(self.index_locator)

    def bid(self):
        # 元素
        return self.get_bid_button().click()

    def get_bid_button(self):
        return self.get_visible_element(self.bid_ele_locator)
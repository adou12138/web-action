# coding: utf-8
# ui-action-po 
# base 
# shen 
# 2019/3/16 12:20
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging

my_log = logging.log()

class BasePage:
    '这个是所有页面的父类'

    def __init__(self, driver):
        self.driver = driver

    def wait(self, local):
        try:
            WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, locals())))
        except Exception as e:
            print("No this element{}!!!".format(e))
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, locals())))



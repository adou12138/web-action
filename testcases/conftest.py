# coding: utf-8
# web-action 
# conftest.py 
# shen 
# 2019/3/21 23:17 

# 配置初始化函数和参数
# pytest http://www.cnblogs.com/cnhkzyy/p/9270830.html

import pytest
from selenium import webdriver
from pages.login import LoginPage

@pytest.fixture
def init_driver():
    print("Begin driver")
    # print('Test Start')

    # url = "http://120.78.128.25:8765/Index/login.html"
    # driver = webdriver.Chrome()
    # driver.get(url)
    # driver.implicitly_wait(30)
    # login_page = LoginPage(driver)
    #
    # login_page.clear_phone()
    # login_page.clear_password()


    my_class().login_page.clear_phone()
    my_class().login_page.clear_password()

    # 功课 面试之前，生成器
    yield

    print("Quit driver")
    # print('Test End')

@pytest.fixture(scope='class')  # 在不同用例上面加载，也只会执行一次
def my_class():
    print('Start Test')
    url = "http://120.78.128.25:8765/Index/login.html"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(30)

    login_page = LoginPage(driver)

    yield (driver, login_page)

    print('End Test')

@pytest.fixture(scope='session', autouse=True)  # 执行所有的用例，不需要再装饰
def my_class_session():
    print('Start Test')

    yield

    print('End Test')
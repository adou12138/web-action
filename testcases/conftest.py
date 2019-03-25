# -*- coding: UTF-8 -*-
# 当前项目的名称: web-action 
# 新文件名称：test11 
# 当前登录名：LuckyLu
# 创建日期：2019/3/25 11:02
# 文件IDE名称：PyCharm 


# 配置初始化函数和参数
# pytest http://www.cnblogs.com/cnhkzyy/p/9270830.html

import pytest
from selenium import webdriver
from pages.login import LoginPage
from pages.invest import InvestPage
from pages.index import IndexPage
from datas import invest


login_page =None

@pytest.fixture(scope='class')  # 在不同用例上面加载，也只会执行一次
def my_class_login():
    print('Start Test Only Once')
    url = "http://120.78.128.25:8765/Index/login.html"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(30)

    global login_page
    login_page = LoginPage(driver)
    print(login_page, type(login_page))

    yield (driver, login_page)

    print('End Test Only Once ')
    driver.quit()

@pytest.fixture
def init_driver():
    print("Every Time Start")
    # print('Test Start')

    if login_page is not None:
        login_page.clear_phone()
        login_page.clear_password()

    # 功课 面试之前，生成器
    yield

    print("Every Time End")
    # print('Test End')


@pytest.fixture(scope='class')  # 在不同用例上面加载，也只会执行一次
def my_class_invest():
    print('Start Test Only Once')
    url = "http://120.78.128.25:8765/Index/login.html"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(30)

    login_page = LoginPage(driver)
    invest_page = InvestPage(driver)
    index_page = IndexPage(driver)

    login_page.send_phone_element(invest.user_currect_info['phone'])
    login_page.send_password_element(invest.user_currect_info['password'])
    login_page.submit_element()
    index_page.bid()

    yield (driver, login_page, invest_page)

    print('End Test Only Once ')
    driver.quit()


@pytest.fixture(scope='session', autouse=True)  # 执行所有的用例，不需要再装饰
def my_class_session():
    print('Start Test')



    yield

    print('End Test')
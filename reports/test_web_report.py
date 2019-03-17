# -*- coding: UTF-8 -*-
# 当前项目的名称: python_13
# 新文件名称：test_math_suite 
# 当前登录名：LuckyLu
# 创建日期：2019/1/11 16:29
# 文件IDE名称：PyCharm

import sys
sys.path.append('../')

import unittest
from libext import HTMLTestRunnerNew
from common import contans


from testcases.test_login import TestLogin  # 导入登录
# from test_cases import test_api_regitser  # 模块方式导入注册

suite = unittest.TestSuite()  # 创建对象
loader = unittest.TestLoader()

# suite.addTest(loader.loadTestsFromTestCase(TestLogin))  # 执行注册
# suite.addTest(loader.loadTestsFromModule(test_api_regitser))  # 模块方式执行注册


# 自动查找testcase目录下，以test开头的.py文件里面的测试类
discover = unittest.defaultTestLoader.discover(contans.testcase_dir, pattern='test_*.py')
# 有多层目录就要添加top_level_dir

# import time
# now = time.strftime('%Y-%m-%d-%H-%M-%S')  # 获取当前系统的时间，生成字符串
# path = contants.report_file+now+'.html'
#
# with open(path, 'wb+') as file:
#     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
#                                             verbosity=2,
#                                             title='API TEST',
#                                             description='THIS IS A API TEST REPORT  ',
#                                             tester='lucky')
#     runner.run(suite)


# 执行jenkins，不能添加时间戳，不然只会显示最久的
with open(contans.report_file, 'wb+') as file:  # 引用common中的report地址 与时间戳互换
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='WEB TEST',
                                            description='THIS IS A WEB TEST REPORT',
                                            tester='lucky')
    runner.run(discover)  # 执行测试集里面的用例  F代表失败 .代表成功 e代表代码错误


# 2: 文本输出测试结果
# with open('../log/case.log', 'w', encoding='utf-8') as file:
#     runner=unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)  # 执行用例的类
#     runner.run(discover)  # 执行测试集里面的用例  F代表失败 .代表成功 e代表代码错误
# steam：输出用例执行结果位置
# descriptions：用例描述
# verbosity：
# 0 显示失败的用例
# 1 用'.'显示成功的用例 失败详细内容
# 2 所有的的用例
# coding: utf-8
# web-action 
# main.py 
# shen 
# 2019/3/21 23:17 

# 配置用例执行顺序

import pytest


if __name__ == '__main__':
    pytest.main([
                 '-m smoke',
                 # '-m success',
                 # '-m investsuccess',
                 # '-m investfailed',
                 # '-m all',
                 # '--capture=no'
                 # '--result-log=reports/result.log ',
                 # '--junit-xml=reports/result.xml',
                 # '--html=reports/result.html',
                 # '--alluredir = allure',
                '--alluredir=../allure-server-report'

                 ])


"""
pytest --alluredir=allure 
'--capture=no'
关闭Captured stdout call输出信息（失败或成功都不显示输出结果）,但是会显示在test session starts部分

　效果等同于 --capture=no， 不捕获
"""
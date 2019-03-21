# -*- coding: UTF-8 -*-
# 当前项目的名称: web-action 
# 新文件名称：invest 
# 当前登录名：LuckyLu
# 创建日期：2019/3/18 15:21
# 文件IDE名称：PyCharm 

user_currect_info = {"phone": "18684720553", "password": "python"}

bid_success_pop = [
                  {"amount": "100", "expected": "投标成功"},
                  {"amount": "1000", "expected": "投标成功"},
                  ]

bid_error_pop = [
                {"amount": "10", "expected": "投标金额必须为100的倍数"},
                {"amount": "010", "expected": "投标金额必须为100的倍数"},
                {"amount": "0", "expected": "请正确填写投标金额"},
                {"amount": "-10", "expected": "请正确填写投标金额"}
                ]

bid_error_pop_button = [
                       {"amount": "##%#$#$", "expected": "请输入10的整数倍"},
                       {"amount": "1", "expected": "请输入10的整数倍"},
                       {"amount": "jhgjghj", "expected": "请输入10的整数倍"}
                       ]
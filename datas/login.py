# coding: utf-8
# ui-action-po 
# login 
# shen 
# 2019/3/16 12:27

# 帐号1：18684720553 密码: python
# 帐号2：13760246701 密码：python
# {"phone": "18684720553", "password": "python"}
user_currect_info = [{"phone": "18684720553", "password": "python"}]

user_error_info = [{"phone": "", "password": "", "expected": "请输入手机号"},
                   {"phone": "", "password": "python", "expected": "请输入手机号"},

                   {"phone": "186847205533", "password": "python", "expected": "请输入正确的手机号"},
                   {"phone": "123", "password": "python", "expected": "请输入正确的手机号"},
                   {"phone": "18684720551", "password": "", "expected": "请输入密码"}

                   # {"phone": "123", "password": "python", "expected": ""},
                   # {"phone": "123", "password": "python", "expected": ""},
                   ]

# //div[@class='layui-layer-content']
user_error_js_info = [{"phone": "18684720552", "password": "python", "expected": "此账号没有经过授权，请联系管理员!"}
                      # {"phone": "18684720553", "password": "python3", "expected": "帐号或密码错误!"}, # 需要调试

                      ]
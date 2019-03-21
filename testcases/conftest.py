# coding: utf-8
# web-action 
# conftest.py 
# shen 
# 2019/3/21 23:17 

import pytest

@pytest.fixture
def init_driver():
    print("Begin driver")


    # 功课 面试之前，生成器
    yield

    print("Quit driver")

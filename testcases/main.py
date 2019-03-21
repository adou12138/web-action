# coding: utf-8
# web-action 
# main.py 
# shen 
# 2019/3/21 23:17 

import pytest

if __name__ == '__main__':
    pytest.main(['-m smoke',
                 '--result-log=reports/result.log ',
                 '--junit-xml=reports/result.xml',
                 '--html=reports/result.html'

                 ])



# coding: utf-8
# web-action 
# config 
# shen 
# 2019/3/17 20:08 

from configparser import ConfigParser
from common import contants

class ReadConfig:
    '这个是一个读取配置的类'

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(contants.web1_conf_file, encoding="utf-8")

    def get_value(self, section, option):
        return self.config.get(section, option)

    def get_int(self, section, option):
        return self.config.getint(section, option)

    def get_float(self, section, option):
        return self.config.getfloat(section, option)

    def get_blean(self, section, option):
        return self.config.getboolean(section, option)

if __name__ == '__main__':
    res = ReadConfig()
    print(res.config.get("LogNew", "in_level"))

    in_level = eval(res.get_value('LogNew', 'in_level'))
    print(in_level, type(in_level))
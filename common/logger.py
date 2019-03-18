# coding: utf-8
# web-action 
# logger 
# shen 
# 2019/3/17 19:59 

import logging
import logging.handlers
from common import contants
from common.config import ReadConfig

config = ReadConfig()
in_level = eval(config.get_value('LogNew', 'in_level'))
out_level = eval(config.get_value('LogNew', 'out_level'))
file_out_level = eval(config.get_value('LogNew', 'file_out_level'))
data_formatter = config.get_value('LogNew', 'fmt')

def get_logger(logger_name):
    """
    :param logger_name: 定义日志输出的名称
    :return:
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(in_level)

    fmt = data_formatter
    formate = logging.Formatter(fmt)

    file_name = contants.log_file
    file_handler = logging.handlers.RotatingFileHandler(
        file_name, maxBytes=20*1024*1024, backupCount=10, encoding="utf-8")
    file_handler.setLevel(file_out_level)
    file_handler.setFormatter(formate)

    # 输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(out_level)
    ch.setFormatter(formate)  # 格式化输出
    
    logger.addHandler(ch)
    logger.addHandler(file_handler)

    return logger

if __name__ == '__main__':
    logger = get_logger(logger_name="login")
    logger.error(" thi is test!!!")
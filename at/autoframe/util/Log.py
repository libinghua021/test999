# -*- coding:utf-8 -*-

import logging
import logging.config
from ProjectVar.var import *

#读取日志的配置文件
logging.config.fileConfig(log_config_file_path)
#选择一个日志格式
logger = logging.getLogger("example02")


def info(message):
    #打印info级别的信息
    logging.info(message)

def error(message):
    #打印error级别的信息
    logging.error(message)

def warning(message):
    #打印warning级别的信息
    logging.warning(message)

if __name__ == "__main__":
    error("---ERROR---")
    info("===Test===")
    warning("````Wang`````")

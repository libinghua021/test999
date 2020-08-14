# -*- coding:utf-8 -*-

import time

#返回中文的年月日时分秒
def data_time_chinese():
    return time.strftime("%Y年%m月%d日 %H时%M分%S秒",time.localtime())

#返回中文的时分秒
def time_chinese():
    return time.strftime("%H时%M分%S秒", time.localtime())

# 返回英文的年月日时分秒
def data_time_english():
    return time.strftime("%Y-%m-%d %H:%M:%S秒", time.localtime())

# 返回英文的时分秒
def time_english():
    return time.strftime("%H:%M:%S秒", time.localtime())

if __name__ == "__main__":
    print data_time_chinese()
    print time_chinese()
    print data_time_english()
    print time_english()
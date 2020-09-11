# -*- coding:utf-8 -*-

import time

#返回中文的年月日时分秒
def data_time_chinese():
    return time.strftime("%Y{}%m{}%d{} %H{}%M{}%S{}").format('年', '月', '日', '时', '分', '秒'), time.localtime()

#返回中文的时分秒
def time_chinese():
    return time.strftime("%H{}%M{}%S{}").format('时', '分', '秒'), time.localtime()

# 返回英文的年月日时分秒
def data_time_english():
    return time.strftime("%Y{0}%m{0}%d %H{1}%M{1}%S").format('-', ':'), time.localtime()

# 返回英文的时分秒
def time_english():
    return time.strftime("%H{0}%M{0}%S").format(':'), time.localtime()

if __name__ == "__main__":
    print(data_time_chinese())
    print(time_chinese())
    print(data_time_english())
    print(time_english())
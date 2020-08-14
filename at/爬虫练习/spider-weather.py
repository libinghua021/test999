import requests
from bs4 import BeautifulSoup
import lxml
import os
from urllib import request
import pymysql
import time

DB_CONN = {
    "host": '192.168.1.26',
    "user": 'root',
    "password": 'Test123',
    "name": 'tianqi'
}

def get_content(url:str):
    header = {
        'user-agent': "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like  Gecko) Chrome / 83.0.4103.61Safari / 537.36"
    }
    response = requests.get(url, headers=header)
    response_text = response.content.decode("utf-8")
    return response_text



def get_citys(url:str):
    content = get_content(url)
    soup = BeautifulSoup(content, 'html.parser')
    course_citys = []
    filter = soup.find_all('div', class_='citybox')

    t = filter[0].find('h2').attrs[value]
    print(t)
    """获取省份"""
    # num = str(filter).count('<h2>')
    # filter_province = []
    # for i in range(0, num):
    #     temp_province = str(filter[{}].find('h2')).format(i)
    #     filter_province.append(temp_province)
    #     print(filter_province)

    # for one in filter_province:
        # print(one)
        # temp_dict = {}
        # province = str(one).split(">")[-3].split("<")[0]
        # temp_dict['province'] = province

    """获取城市"""
    # filter_city = filter.find_all('span')

if __name__ == "__main__":
    url = 'https://www.tianqi.com/chinacity.html'
    get_citys(url)
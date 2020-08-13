import requests
from bs4 import BeautifulSoup
import lxml
import os
from urllib import request
import pymysql
import time
import threading
from queue import Queue

class SpiderThread：
    def __init__(self):
        self.base_url = 'https://www.doutula.com/photo/list/?page={}'
        self.base_url_detial = 'https://www.doutula.com/photo/{}'
        self.pages = 68
        self.header = {'user-agent': "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like  Gecko) Chrome / 83.0.4103.61Safari / 537.36"}
        self.page_number = 10
        self.url_queue = Queue()
        self.html_queue = Queue()

    def get_url_list(self):
        """获取url列表"""
        for i in range(1, self.page_number + 1):
            self.url_queue.put(self.base_url.format(i))

    def parse_url(self):
        """获取页面"""
        while True:
            url =self.url_queue.get()
            response = requests.get(url, headers=self.header)
            self.html_queue.put(response.content.decode("utf-8"))
            self.url_queue.task_done()

    def get_content_list(self):
        """筛选数据"""
        content = parse_url(self)
        soup = BeautifulSoup(content, 'html.parser')
        filter = soup.find_all('a', class_='col-xs-6')
        course_infos = []
        # imgi = 1
        for one in filter:
            temp_dict = {}
            title = one.find('img').attrs['alt']
            temp_dict['title'] = title
            img = one.find('img').attrs['data-backup']
            temp_dict['img'] = img
            # save_img(img)
            # print("已保存第{}张图片...".format(imgi))
            # imgi += 1
            course_infos.append(temp_dict)
        return course_infos

    def save_content_list(self):
        """保存数据"""
        pass

import requests
from bs4 import BeautifulSoup
import lxml
import os
from urllib import request
import pymysql
import time
# import threading

DB_CONN = {
    "host": '192.168.1.26',
    "user": 'root',
    "password": 'Test123',
    "name": 'spider'
}

def get_content(url:str):
    header = {
        'user-agent': "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like  Gecko) Chrome / 83.0.4103.61Safari / 537.36"
    }
    response = requests.get(url, headers=header)
    response_text = response.content.decode("utf-8")
    return response_text

def save_img(url:list):
    filename = url.split("/")[-1]
    path = os.path.join("images", filename)
    request.urlretrieve(url, path)

def get_course_info(url:str):
    content = get_content(url)
    soup = BeautifulSoup(content, 'html.parser')
    filter = soup.find_all('a', class_='col-xs-6')
    course_infos = []
    imgi = 1
    for one in filter:
        temp_dict = {}
        title = one.find('img').attrs['alt']
        temp_dict['title'] = title
        img = one.find('img').attrs['data-backup']
        temp_dict['img'] = img
        save_img(img)
        print("已保存第{}张图片...".format(imgi))
        imgi += 1
        course_infos.append(temp_dict)
    return course_infos

def save_to_mysql(courses:list):
    mysql_conn = pymysql.connect(DB_CONN['host'], DB_CONN['user'], DB_CONN['password'], DB_CONN['name'])
    cursor = mysql_conn.cursor()
    try:
        for course in courses:
            sql = "INSERT INTO doutu (imgname, imgurl) VALUES('%s','%s')" % (course['title'], course['img'])
            cursor.execute(sql)
            mysql_conn.commit()
        print("数据已保存至数据库")
    except Exception as e:
        mysql_conn.rollback()
        print("写入失败，具体原因："+str(e))
    finally:
        mysql_conn.close()

if __name__ == "__main__":
    while True:
        pagetime = input("您将从斗图网爬取图片，一页爬取68张图片，请输入要爬取的页数：")
        if pagetime.isdigit() and int(pagetime) > 0:
            break
        else:
            continue
    start_time = time.time()
    for p in range(1, int(pagetime)+1):
        url = 'https://www.doutula.com/photo/list/?page={}'.format(p)
        print('开始爬取第{}页'.format(p))
        save_to_mysql(get_course_info(url))
        # 多线程
        # th = threading.Thread(target=save_to_mysql(get_course_info(url)), args=[p])
        # th.start()
        print('已爬取第{}页'.format(p))
        print('-'*30)
    end_time = time.time()
    print("任务完成*_*")
    print("保存所需时间为：{:.4f}秒".format(end_time - start_time))
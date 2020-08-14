#__author:'lbh'
#date: 2020/6/17
import requests
from bs4 import BeautifulSoup
for i in range(0,10):
    url = 'http://maoyan.com/board/4?offset={}'.format(i)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}   #因为猫眼对爬虫或许有反爬措施，所以这里进行简单的处理，将我们的爬虫伪装成是人访问
    response = requests.get(url,headers = headers)     #对网页进行请求并返回值
    html = response.text      #将网页内容以html返回
    soup = BeautifulSoup(html,'lxml')      #解析网页的一种方法
    name = soup.find_all('p',class_="name")    #对电影名字的定位
    score = soup.find_all('p',class_="score")   #对电影评分的定位
    time = soup.find_all('p',class_="releasetime")  #对电影上映时间的定位
    artist = soup.find_all('p',class_="star")       #对主演的定位
    dic = {}    #创建一个字典，用来储存
    for n in range(len(name)) :         #对于每一部电影进行同样的内容处理
        # print(name[n].text)   #实现提取电影名字
        # print(artist[n].text.strip()[3:])   #获取主演名字
        # print(time[n].text[5:])    #上映时间
        # print(score[n].text)   #评分
        dic['name'] = name[n].text
        dic['star'] = artist[n].text.strip()[3:]
        dic['showtime'] = time[n].text[5:]
        dic['score'] = score[n].text
        print(dic)  #输出字典

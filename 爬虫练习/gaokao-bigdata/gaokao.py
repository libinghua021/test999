import requests
from bs4 import BeautifulSoup
import lxml



def get_conn(url):
    header = {
     'user-agent': "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like  Gecko) Chrome / 84.0.4147.105Safari / 537.36"
    }

    response = requests.get(url, headers=header)
    response_text = response.content.decode("utf-8")
    return response_text

def get_info(url):
    content = get_conn(url)
    soup = BeautifulSoup(content, 'html.parser')
    first = soup.find_all('div', class_='list-content__5b048e89')
    for item in first:
         print(item)


if __name__ == '__main__':
    url = 'https://voice.baidu.com/activity/gaokao?page=collegeExam&tabname=trendList&subtabname=collegeRank'
    get_info(url)
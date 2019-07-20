# Author 洪胜兵
# Date 2019/7/20
# version 1.0
import re

from requests.exceptions import RequestException
import requests
from bs4 import BeautifulSoup


# 获取网页内容
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/75.0.3770.142 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def write_to_file(content):
    with open('result_music.txt', 'a', encoding='utf-8') as f:
        f.write(content + "\n")


def main():
    url = 'https://www.kugou.com/yy/html/rank.html'
    html = get_one_page(url)
    soup = BeautifulSoup(html, 'lxml')
    for item in soup.find_all("a", {'class': 'pc_temp_songname'}):
        print(re.sub('\\s', '', str(list(item.parent)[5].string)), item.string,
              re.sub("\\s", '', list(item.parent)[11].span.string))
        write_to_file(re.sub('\\s', '', str(list(item.parent)[5].string)) + item.string +
                      re.sub("\\s", '', list(item.parent)[11].span.string))


if __name__ == '__main__':
    main()

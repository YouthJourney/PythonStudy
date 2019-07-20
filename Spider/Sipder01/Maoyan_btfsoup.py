# @Author 洪胜兵
# @Date 2019/7/19 20:06
# @Version 1.0
import time
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
import re


# 获取网页内容
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def write_to_file(content):
    with open('result_soup.txt', 'a', encoding='utf-8') as f:
        f.write(content + "\n")


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # print(html)
    soup = BeautifulSoup(html, 'lxml')

    """做测试用"""
    # lst = list()
    # for k in soup.find_all("p", {'class': 'name'}):
    #     lst.append(["片名:" + re.sub('\\s', '', k.string), re.sub('\\s', '', list(k.next_siblings)[1].string),
    #                 re.sub('\\s', '', list(k.next_siblings)[3].string)])
    #     print(lst[len(lst) - 1])
    #     write_to_file(",\t".join(lst[len(lst) - 1]))

    # for n in soup.find_all("p", {'class': 'score'}):
    #     print("评分:" + list(n.descendants)[1] + list(n.descendants)[3])
    # for n in lst:
    #     print(n)

    # for brother in soup.find("p", {'class': 'name'}).next_siblings:
    #     print(re.sub('\\s', '', brother.string))
    # for n in soup.find_all(attrs={'class': 'releasetime'}):
    #     print(re.sub('\\s', '', n.string))
    # for l in soup.find_all(attrs=):
    #     pass

    """最终代码"""
    lst = list()
    for m in soup.find_all("div", {'class': 'movie-item-info'}):
        lst.append(
            ["片名:" + list(m.descendants)[3], re.sub('\\s', '', list(m.descendants)[6]),
             list(m.descendants)[9], "评分:" + list(list(m.next_siblings)[1].p.descendants)[1] +
             list(list(m.next_siblings)[1].p.descendants)[3]])
        print(lst[len(lst) - 1])
        write_to_file(",\t".join(lst[len(lst) - 1]))


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        # print(i)
        time.sleep(1)

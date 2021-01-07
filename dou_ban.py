# -*- coding: utf-8 -*-
# @Date    : 2021-01-06 11:45:54
# @Author  : ningshengit
# @知乎    : https://www.zhihu.com/people/kuanye
# @微信    : 
# @funtion : 豆瓣影评
# @Version : $Id$

import os
import random
import time
import requests
from bs4 import BeautifulSoup
import re
import json
import csv
import pickle

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    ]

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/explore',
    }
cookie = '从浏览器复制cookie到这里'

def local_cookie(string):
    """
    从浏览器赋值cookie进行处理
    放到session中
    :return:
    """
    if string:
        s_list = string.split(';')
        cookie_d = {}
        for item in s_list:
            i = item.split('=')
            cookie_d[i[0]] = i[1]
        return cookie_d

cookies = local_cookie(cookie)
session = requests.session()
session.headers = headers
session.cookies.update(cookies)


def get_page(movie_id, page):

    headers['User-Agent'] = random.choice(USER_AGENTS)
    url = 'https://movie.douban.com/subject/{}/reviews?start={}'.format(movie_id, page*20)    
    print("正在爬的页码：%s"%page)
    res = session.get(url=url, headers=headers, allow_redirects=False)
    print(res.status_code)
    if res.status_code == 200:
        #每一页有20条影评，就有20个关于内容，时间，评分的main
        soup = BeautifulSoup(res.text, 'lxml')
        title = re.findall('(?<= )(.*?)(?=的影评)', soup.title.get_text())[0].replace(" ", '')
        yp_list = soup.find_all('div', attrs={'class':'main review-item'})
        for page_tag in yp_list:
            name = get_yp_name(page_tag).get_text()
            star = str(get_yp_star(page_tag))
            dtime = get_yp_time(page_tag).get_text()
            ying_ping = get_detial_yp(page_tag)
            time.sleep(random.randint(1,2))
            save_to_csv([title, name, star, dtime, ying_ping])
            save_to_txt([title, name, star, dtime, ying_ping])

def get_yp_name(page_tag):
    '''影评作者'''
    return page_tag.find(attrs={'class':'name'})

def get_yp_star(page_tag):
    '''获取星级'''
    pattern = re.findall('class="allstar(\d+) main-title-rating"',str(page_tag))
    if pattern:
        star = pattern[0]
    else:
        star = 0
    return star

def get_yp_time(page_tag):
    '''影评时间'''
    return page_tag.find(attrs={'class':'main-meta'})

def get_detial_yp(page_tag):
    '''解析影评全内容'''
    headers['User-Agent'] = random.choice(USER_AGENTS)
    content_id = re.findall('id="review_(\d+)_full"', str(page_tag))[0]
    content_h1 = page_tag.select('h2>a')[0].get_text()
    url = 'https://movie.douban.com/j/review/{}/full'.format(content_id)
    print("爬取id%s--"%content_id)
    res = session.get(url=url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = json.loads(res.text)
        if data['html']:
            yp = re.findall('[\u4e00-\u9fa5|，、“”‘’：！~@#￥【】*（）——+。；？]+', data['html'])
            return content_h1+"\n"+",".join(yp)
        else:
            return content_h1+""

def save_to_csv(data):
    if data:
        with open('muyuzhiwang.csv', 'a',  newline='', encoding='utf-8-sig') as fp:
            csv_w = csv.writer(fp)
            csv_w.writerow(data)
        print("写入文件")          

def save_to_txt(data):
    if data:
        with open('muyuzhiwang.txt', 'a', encoding='utf-8-sig') as f:
            f.write("--------------------------------\n")
            f.write("|".join(data)+'\n')
            f.writelines('\n')
        print("写入文件")                    




if __name__ == '__main__':
    move_id = 34894753
    for page in range(0,10):
        get_page(move_id, page)

                
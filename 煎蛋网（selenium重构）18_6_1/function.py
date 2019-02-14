#!/usr/bin/env python3
# -*- coding: utf-8 -*

def parse_html(html):
    #获取的页面源码中解析出每个图片的URL

    from bs4 import BeautifulSoup
    import re

    url_list = []
    soup = BeautifulSoup(html, 'lxml').find('ol', class_='commentlist')
    # print(str(soup))
    sole_item = soup.find_all('p')
    for i in sole_item:
        #print(i)
        pattern = re.compile(r'<img src="(.*?)" style',re.S)
        result = re.findall(pattern,str(i))
        print(result)
        url_list+=result
    print('--------------------------')
    for i in url_list:
        print(i,'   ',str(len(i)))

    return url_list


def pdf(html):
    #
    print(html)

def receive_img(url_list,num):
    #下载图片
    import requests
    import random
    from UA import user_agent

    ua = user_agent()#获取随机UA

    s_num = 1#s_num每页图片个数

    headers = {
        'Host':'wx3.sinaimg.cn',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer':'http://jandan.net/ooxx/page-'+str(random.randint(1, 80)),
        'User-Agent':ua
    }

    for url in url_list:
        name ='C:\\Users\L1308\Desktop\Python Demo\project\meiztu\\'+str(num)+'-'+str(s_num)+'.jpg'
        img = requests.get(url, headers=headers)
        f = open(name, 'ab')  ##写入多媒体文件必须要 b 这个参数！！必须要！！
        f.write(img.content)  ##多媒体文件要是用conctent哦！
        f.close()
        s_num+=1



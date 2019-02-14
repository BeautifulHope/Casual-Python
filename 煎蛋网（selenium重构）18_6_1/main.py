#!/usr/bin/env python3
# -*- coding: utf-8 -*

from selenium import webdriver
from function import *
import requests
from bs4 import BeautifulSoup
import time
import re
import random

def browse(page):

    num = page
    browse = webdriver.Firefox()
    #browse.get('http://jandan.net/')
    #url = 'http://jandan.net/ooxx/page-'+str(page)+'#comments'
    url = 'http://jandan.net/ooxx'

    browse.get(url)
    while(1):
        time.sleep(random.randint(3,12))#随机延时函数
        print(browse.title +'    第'+str(num)+'页    ')


        html = browse.page_source#获取页面源码

        url_list = parse_html(html)
        receive_img(url_list,num)#分析页面，获取图片
        num += 1

        browse.find_element_by_class_name('previous-comment-page').click()#点击下一页


    browse.close()



if  __name__ == '__main__':
    page = 1
    browse(page)
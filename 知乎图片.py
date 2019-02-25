# 作者：匿名用户
# 链接：https://www.zhihu.com/question/21395276/answer/509105044
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
##
#HBAD-215

import re
import json
import requests
import os
import time

class Pics:
    def __init__(self):
        self.header = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36',
            'Upgrade-Insecure-Requests':'1',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        }
        # 获取问题的json链接
        ##self.url = 'https://www.zhihu.com/api/v4/questions/58498720/answers?include=content&limit=20&offset=0&sort_by=default'
        self.url = 'https://www.zhihu.com/api/v4/questions/302127448/answers?include=content&limit=20&offset=0&sort_by=default'
        # 存放根目录路径
        self.base_dir = 'I:\AALLTEST\\test'#'D:/pics/'
        #问题链接
        ##self.index_url = 'https://www.zhihu.com/question/58498720'
        self.index_url = 'https://www.zhihu.com/question/302127448'
        self.page = ''
        self.makeNewSession()

    def makeNewSession(self):
        requests.get(self.index_url, headers=self.header)
        self.session = requests.session()

    def getContent(self):
        print('正在扒%s'%self.url)
        json_str = self.session.get(self.url, headers=self.header)
        json_obj = json.loads(json_str.content.decode())

        data = json_obj.get('data')
        if data:
            self.url = json_obj.get('paging').get('next')
        else:
            self.url = ''

        for i in data:
            self.formatPic(i.get('content'))

    def formatPic(self,content):
        result = list(set(re.findall(r'data-original="(.+?)"', content))) #正则获取图片 然后去重
        for i in result:
            path,authority = self.makePicName(i)

            pic = self.session.get(i,headers=self.header)
            if pic.status_code != 200:
                print('图片：'+i+'获取失败')
                print('状态码：'+pic.status_code)
                time.sleep(3)
            self.savePic(pic,path)

    def savePic(self,pic,name):
        with open(self.page+name,'wb') as f:
            f.write(pic.content)
            print('保存图片'+self.page+name)

    def makePicName(self,link):
        rindex = link.rfind('/')
        index = link.find('pic')
        return link[rindex:],link[index:rindex]

    def mkdir(self,path):
        print('创建'+path)
        path = self.base_dir + path
        is_exists = os.path.exists(path)
        if not is_exists:
            os.mkdir(path)
        self.page = path

    def run(self):
        index = 1
        is_exists = os.path.exists(self.base_dir)
        if not is_exists:
            os.mkdir(self.base_dir)
        while True:
            if self.url == '':
                break

            page = '第{}页'.format(index)
            self.mkdir(page)
            self.getContent()
            index += 1

        print('图片扒取完毕')

if __name__ == '__main__':
    pic = Pics()
    pic.run()
#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pdfkit#txt转化为pdf
import time
import matplotlib.pyplot as plt

def converser():
    filename = '图片转txt.txt'

    time_1 = time.time()
    print(time_1)
    with open(filename) as f:
        options = {
            'page-size': 'A4',#Letter
            'margin-top': '0.1in',
            'margin-right': '0.1in',
            'margin-bottom': '0.1in',
            'margin-left': '0.1in',
            'encoding': "ascii",
            'no-outline': None
        }
        pdfkit.from_file(f, '图片转txt.pdf',options=options)
    time_2 = time.time()
    print("用时：",str(time_2-time_1)[0:5]+'s')

file_name='图片转txt.txt'

start_time = time.time()#计时开始

show_height = 600#60,120
show_width = 800#80,160
#这两个数字是调出来的

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#生成一个ascii字符列表
char_len = len(ascii_char)
print('char_len:'+str(char_len))

pic = plt.imread("2.jpg")
#使用plt.imread方法来读取图像，对于彩图，返回size = height*width*3的图像
#matplotlib 中色彩排列是R G B
#opencv的cv2中色彩排列是B G R

pic_height ,pic_width,_ = pic.shape
#获取图像的高、宽

gray = 0.2126 * pic[:,:,0] + 0.7152 * pic[:,:,1] + 0.0722 * pic[:,:,2]
#RGB转灰度图的公式 gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

#思路就是根据灰度值，映射到相应的ascii_char

# with open(file_name, 'w') as file:
#     for frame in output_list:
#         file.write(frame + "\n");

with open(file_name,'w') as object:
    for i in range(show_height):
        #根据比例映射到对应的像素
        y = int(i * pic_height / show_height )
        text = ""
        for j in range(show_width):
            x = int(j * pic_width / show_width)
            text += ascii_char[int(gray[y][x] / 256 * char_len)]
        print(text)
        object.write(text + "\n")

converser()
end_time = time.time()
print("用时：",str(end_time-start_time)[0:5]+'s')

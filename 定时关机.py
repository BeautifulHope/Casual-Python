#!/usr/bin/env python3
# -*- coding: utf-8 -*

import os
import time
from datetime import datetime

def kill_computer():
    shutdown = int(input('请选择功能:(0：定时关机；1：取消自动关机；2：立即关机):'))

    if shutdown==1:

        os.system('shutdown -a')
        os._exit(0)

        s = input('按回车健结束。')

    elif shutdown==2:

        print('5秒后关机。')
        os.system('shutdown -s -t 5')
        os._exit(0)

        s = input('按回车健结束。')

    else:

        t = input('请输入关机时间(格式： 时：分：秒)：')
        try:
            time_now = t.split(':')
        except:
            time_now = t.split('：')
        # print(str(time))

        h, m, s = time_now
        h = min(int(h), 24)  # 防止小时超过24
        m = min(int(m), 59)  #
        s = min(int(s), 59)  #

        # print(str(h),str(m),str(s))

        now = datetime.now()  # 获取当前时间
        now_h, now_m, now_s = now.hour, now.minute, now.second
        # print(str(now_h),str(now_m),str(now_s))

        encounter = (h - now_h) * 3600 + (m - now_m) * 60 + (s - now_s)
        if (encounter > 0):
            print('电脑将在' + str(encounter) + '秒后自动关机')
            os.system('shutdown -s -t {}'.format(str(encounter)))
            os._exit(0)
        else:
            print('仅支持当天自动关机')

        s = input('按回车健结束。')

if __name__=='__main__':
    kill_computer()



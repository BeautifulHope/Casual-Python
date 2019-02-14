#!/usr/bin/env python3
# -*- coding: utf-8 -*

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱地址
smtpserver = 'smtp.163.com'
#邮箱账号，密码
user = '13080349916@163.com'
password = 'ljz123'
#发送邮箱
send = '13080349916@163.com'
#接受邮箱
receive = '1148368634@qq.com'
#发送邮件主题
subject = 'Python email test'
#邮件正文
msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'Tim<13080349916@163.com>'
msg['To'] = "1148368634@qq.com"

#发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(send,receive,msg.as_string())
smtp.quit()
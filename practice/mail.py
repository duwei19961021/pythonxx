#coding: utf-8

# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = "duwei19961021@163.com"
# password = "duwei1996"
# receiver = "1035374290@qq.com"
# subject = "test" #邮件标题
# words = "test" #邮件正文
# smtpserver = 'smtp.163.com'
#
# msg = MIMEText(words, 'plain', 'utf-8')#中文需参数‘utf-8'，单字节字符不需要
# msg['Subject'] = Header(subject, 'utf-8') #邮件标题
# msg['from'] = sender #发信人地址
# msg['to'] = receiver #收信人地址
#
# smtp = smtplib.SMTP('smtp.163.com',25)
# smtp.connect('smtp.163.com')
# smtp.login(sender, password)
# smtp.sendmail(sender, receiver, msg.as_string()) #这行代码解决的下方554的错误
# smtp.quit()
# print("邮件发送成功!")
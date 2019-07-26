# -*- coding: utf-8 -*-
# import xlwt
# import pymysql
# connection = pymysql.connect(host='139.196.120.52',
#                              port=3306,
#                              user='duwei',
#                              password='duwei',
#                              db='mytest',
#                              charset='utf8')
# cursor = connection.cursor()
# sql1 = 'select  v1.`TrueName`,v1.`Mobile` from mytest.xb_mem_info  v1 join (select  * from     mytest.`xb_loans_applylist`   where LoanStatus =2 )v2 on v1.ID=v2.userID'
# cursor.execute(sql1)
# result = cursor.fetchall()
# d = {}
# Name = []   #姓名
# Mobile = [] #手机号
# for i in result:
#     d[i[0]] = i[1]
# for k,v in d.items():
#     Name.append(k),Mobile.append(v)
# for num in range(len(Mobile)):
#     workbook = xlwt.Workbook(encoding = 'ascii')
#     worksheet = workbook.add_sheet('data')
#     worksheet.write(num,0,label = '{}'.format(Name[num]))
#     # worksheet.write(num,1,label = '{}'.format(Mobile[num]))
#     print(num,Name[num],Mobile[num])
#     workbook.save('Excel_Workbook.xls')

# from openpyxl import Workbook
# import openpyxl
import os
import xlwt
import pymysql
dbname = ("51yqb",
"alqd",
"anxundai",
"bahaoqianzhuang",
"bsjk",
"btqb",
"chaond",
"cht",
"csqb",
"daidd",
"dainih",
'daiqianjin',
'daishux',
'dayunh',
'ddb',
'ddyd',
'emd',
'fenmyd',
'guirenbang',
'haolaimi',
'haoqd',
'hbh',
'hcjr',
'hlh',
'hlqb',
'hsqb',
'hyh',
'jbd',
'jdj',
'jfqb',
'jiahejinrong',
'jialejf',
'jiebaod',
'jiedb',
'jiejie',
'jijiubao',
'jinbak',
'jinmadai',
'jinmjf',
'jintongmiaojie',
'jishuqianbao',
'jiuzcm',
'jiyongbao',
'jjh',
'jpt',
'jucaib',
'jwy',
'jzd',
'jzqb',
'kuaidaiwang',
'kuailehua',
'lanjing',
'lijiyou',
'longfyj',
'lqb',
'luban7',
'mangguosudai',
'mdd',
'miaojiedao',
'micheng',
'midai',
'mjd',
'mlhh',
'msyj',
'niwoyidai',
'paipaiqiandai',
'pgy',
'pinganfu',
'ppqd',
'puhuiqb',
'qianduoduo',
'qianjin',
'quancd',
'rongyihua',
'ruyidai',
'sdgj',
'sqh',
'stqb',
'sudai',
'suinidai',
'sujiebao',
'susudai',
'sxb',
'sxqb',
'syd',
'taoxianj',
'tbg02',
'wantqb',
'wcqb',
'weilibao',
'wht',
'wjd',
'wljf',
'wuyimiaodian',
'xbd',
'xdb',
'xhb',
'xiangjiuyong',
'xinshidai',
'xinyongqianbao',
'xinzefu',
'xjd',
'xjingui',
'xsqb',
'xxhua',
'ydb',
'ydj',
'yifanqb',
'yimiaod',
'yimijinfu',
'yinghc',
'yinuoqb',
'yirongrd',
'yixiangh',
'yizhihua',
'yjqb',
'ymftest',
'ymqb',
'ymwd',
'yonghqb',
'youmihua',
'youpyj',
'youxinhua',
'yqh',
'yrd',
'ysh',
'yudaibao',
'zhimaxiaodai',
'zlb',
'zzqb')
for db_name in dbname:
    print(db_name)
    connection = pymysql.connect(host='rm-bp12wrwc74l886dl6so.mysql.rds.aliyuncs.com',
                                 port=3306,
                                 user='duwei',
                                 password='Dbde181d04b2d',
                                 db=db_name)
                                 # charset='utf-8')
    cursor = connection.cursor()
    sql1 = 'select  v1.`TrueName`,v1.`Mobile` from xb_mem_info  v1 join (select  * from  `xb_loans_applylist`   where LoanStatus !=2 )v2 on v1.ID=v2.userID'
    cursor.execute(sql1)
    result = cursor.fetchall()
    for i in result:
        with open(r"C:\Users\x1c\Desktop\sj\data_no.txt",'a+') as f:
            f.write("{},{}".format(i[0],i[1])+'\n')
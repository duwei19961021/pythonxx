# -*- coding: utf-8 -*-
import xlwt
import pymysql
connection = pymysql.connect(host='139.196.120.52',
                             port=3306,
                             user='duwei',
                             password='duwei',
                             db='mytest',
                             charset='utf8')
cursor = connection.cursor()
sql1 = 'select  v1.`TrueName`,v1.`Mobile` from mytest.xb_mem_info  v1 join (select  * from     mytest.`xb_loans_applylist`   where LoanStatus =2 )v2 on v1.ID=v2.userID'
cursor.execute(sql1)
result = cursor.fetchall()
for i in result:
    print(i)
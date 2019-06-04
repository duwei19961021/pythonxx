import  pymysql
def chushihua():
    connection = pymysql.connect(host='139.196.120.52',
                                 port=3306,
                                 user='python',
                                 password='123456',
                                 charset='utf8')
    cursor = connection.cursor()
    sql1 = "create database shop;"
    sql2 = "create table shop.users(ID  int(11) primary key not null auto_increment,User_name VARCHAR (32) unique not null, Password varchar(30) not NULL,Wage int(11) not null);"
    cursor.execute(sql1)
    cursor.execute(sql2)
chushihua()
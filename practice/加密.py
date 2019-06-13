import hashlib
import pymysql
def MD5(a): #密码加密
    m = hashlib.md5()
    m.update(a.encode("utf8"))
    a_md5 = m.hexdigest()
    return a_md5
def execsql(sql): #执行sql
    db = pymysql.connect("139.196.120.52", "python", "123456", "shop")
    cursur = db.cursor()
    cursur.execute(sql)
    ret = cursur.fetchone()
    db.commit()
    db.close()
    return ret
def checkuser(username): #检查用户是否存在
    sql2 = "select user_name from shop.users where user_name='{}';".format(username)
    execsql(sql2)
def modifypwd(): #修改密码
    username = input("input your username:")
    mobile = input("input your mobile:")
    sql = "select mobile from shop.users where user_name='{}';".format(username)
    if execsql(sql)[0] == mobile:
        newpassword = input("mobile check successfuly and input your newpassword that you want:")
        sql2 = "update shop.users set password='{}' where user_name = '{}'".format(MD5(newpassword), username)
        execsql(sql2)
        print("修改成功")
    else:
        print("mobile checking faied")
class user: #注册
    def __init__(self,username,password,mobile):
        self.username = username
        self.password = password
        self.mobile = mobile
    def registered(self):
        sql1 = "insert into shop.users (user_name,Password,mobile) values ('{}','{}',{});".format(self.username, self.password,self.mobile)
        execsql(sql1)



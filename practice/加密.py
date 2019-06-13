import hashlib
import pymysql
def MD5(a):
    m = hashlib.md5()
    m.update(a.encode("utf8"))
    a_md5 = m.hexdigest()
    return a_md5
def execsql(sql):
    db = pymysql.connect("139.196.120.52", "python", "123456", "shop")
    cursur = db.cursor()
    cursur.execute(sql)
    ret = cursur.fetchone()
    db.commit()
    db.close()
    print(ret)
def checkuser(username):
    sql2 = "select user_name from shop.users where user_name='{}';".format(username)
    execsql(sql2)
class user:
    def __init__(self,username,password,mobile):
        self.username = username
        self.password = password
        self.mobile = mobile
    def registered(self):
        sql1 = "insert into shop.users (User_name,Password,mobile) values ('{}','{}',{});".format(self.username, self.password,self.mobile)
        execsql(sql1)
    # def modifypwd(self):
ss = checkuser("duwei")
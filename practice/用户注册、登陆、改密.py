import hashlib
import pymysql
# def MD5(a): #密码加密
#     m = hashlib.md5()
#     m.update(a.encode("utf8"))
#     a_md5 = m.hexdigest()
#     return a_md5
# def execsql(sql): #执行sql
#     db = pymysql.connect("139.196.120.52", "python", "123456", "shop")
#     cursur = db.cursor()
#     cursur.execute(sql)
#     ret = cursur.fetchall()
#     db.commit()
#     db.close()
#     return ret
# def checkuser(username): #检查用户是否存在
#     sql2 = "select user_name from shop.users where user_name='{}';".format(username)
#     execsql(sql2)
# def modifypwd(): #修改密码
#     username = input("input your username:")
#     mobile = input("input your mobile:")
#     sql = "select mobile from shop.users where user_name='{}';".format(username)
#     if execsql(sql)[0] == mobile:
#         newpassword = input("mobile check successfuly and input your newpassword that you want:")
#         sql2 = "update shop.users set password='{}' where user_name = '{}'".format(MD5(newpassword), username)
#         execsql(sql2)
#         print("modify password successfuly!")
#     else:
#         print("mobile checking faied")



class user: #用户类
    def __init__(self,username,password,mobile):
        self.username = username
        self.password = password
        self.mobile = mobile

    @staticmethod
    def md5(password):  # password加密,静态方法，无需使用对象中封装的值
        m = hashlib.md5()
        m.update(password.encode("utf8"))
        a_md5 = m.hexdigest()
        return a_md5

    @staticmethod
    def execsql(sql):  # 执行sql,静态方法，无需使用对象中封装的值
        db = pymysql.connect("139.196.120.52", "python", "123456", "shop")
        cursur = db.cursor()
        cursur.execute(sql)
        ret = cursur.fetchall()
        db.commit()
        db.close()
        return ret

    def checkuser(self):  # 检查用户是否存在
        sql2 = "select user_name from shop.users where user_name='{}';".format(self.username)
        if user.execsql(sql2) == ():
            return 0
        else:
            return 1

    def registered(self): #注册
        if self.checkuser() == 1:
            print("user had exist!")
        else:
            sql1 = "insert into shop.users (user_name,Password,mobile) values ('{}','{}',{});".format(self.username, user.md5(self.password),self.mobile)
            user.execsql(sql1)
            print("register successfuly")


    def modifypwd(self):  # 修改密码
        if self.checkuser() == 1:
            sql = "select mobile from shop.users where user_name='{}';".format(self.username)
            if eval(user.execsql(sql)[0][0]) == self.mobile:
                newpassword = input("mobile check successfuly and input your newpassword that you want:")
                sql2 = "update shop.users set password='{}' where user_name = '{}'".format(self.md5(newpassword), self.username)
                user.execsql(sql2)
                print("modify password successfuly!")
            else:
                print("mobile checking faied")
        else:
            print("user not exist")

    def login(self):
        sql = "select password from shop.users where user_name='{}'".format(self.username)
        if self.checkuser() == 1 and user.execsql(sql)[0][0] == self.md5(self.password):
            print("login successfuly")
        else:
            print("your username or password error!")
print("1、注册 2、登录 3、修改密码")
choice = int(input("input your chice:"))
if choice == 1:
    obj1 = user("duwei3",'123456',13487459076)
    obj1.registered()
elif choice == 2:
    obj2 = user("duwei",'duwei',13487459076)
    obj2.login()
elif choice == 3:
    obj3 = user("duwei","duwei",13487459076)
    obj3.modifypwd()
# dd

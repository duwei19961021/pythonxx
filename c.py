import pymysql
connection = pymysql.connect(host='139.196.120.52',
                             port=3306,
                             user='python',
                             password='123456',
                             charset='utf8')
cursor = connection.cursor()
def registered():
        while 1:
            username = input("username:")
            password = input("password:")
            if username == '' or password == '':
                print("用户名或者密码不能为空")
                continue
            wage = input("wage:")
            SelectSql = "select ID from shop.users where User_name='%s'"%(username)
            InsertSql = """insert into shop.users (User_name,Password,Wage) values ("%s","%s","%s");"""%(username, password, wage)
            if cursor.execute(SelectSql) == 1:
                print("用户已存在，请重新输入！！！")
                continue
            else:
                cursor.execute(InsertSql)
                print("注册成功")
            connection.commit()
            cursor.close()
            connection.close()
            break

def longin():
    num = 0
    while num < 3:
        username = input("your username:")
        password = input("your password:")
        if username == '' or password == '':
            print("用户名或者密码不能为空")
            continue
        Sql1 = "select ID from shop.users where User_name='%s'"%(username)
        Sql2 = "select Password from shop.users where User_name='%s'"%(username)
        if cursor.execute(Sql1) == 1:
            cursor.execute(Sql2)
            a = cursor.fetchone()
            if  a[0] == password:
                print("登陆成功！！！")
                break
            else:
                print("密码错误,请重新输入！！！")
                num += 1
                continue
        else:
            print("用户不存在！！！")
    cursor.close()
    connection.close()
# Selection = input("welcome,1=登陆，2=注册,3=退出:")
# if eval(Selection) == 1:
#     longin()
# elif eval(Selection) == 2:
#     registered()
# elif eval(Selection) == 3:
#     exit()
# else:
#     pass
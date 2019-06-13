# class LiShuai:
#     def __init__(self,name,age): #构造方法
#         # 实例变量（字段）
#         self.name1 = name
#         self.age1 = age
#     # 类变量（静态字段）
#     contry = 100
#     def name(self):
#         print(self.name1,self.age1)
#     def age(self):
#         print(self.name1,self.age1)
# obj = LiShuai("lishuai",28)
# obj2 = LiShuai("lishuai",28)
# print(obj.contry)
# obj2.name()
# obj.age()
# print(LiShuai.contry)
# LiShuai.contry = 300
# print(obj2.contry)

# 准则：
# 实例变量（字段）访问时，使用对象访问，即obj1.name
# 类变量（静态字段）访问时，使用类方法，即LiShuai.country(实在不方便才使用对象)



##################################################
# class duwei:
#     __contry = "中国" #私有类变量
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age #私有实例变量（私有字段），只能由类的内部访问
#     def func3(self):
#         print(self.__age)
#     def func4(self):
#         print(self.__contry)
# obj3 = duwei("duwei",18)
# print(obj3.name)
# # print(obj3.__age)
# obj3.func3()

######################################################
# class father:
#     __secret = "A"
# class son(father):
#     def func(self):
#         print(self.__secret)
#         print(father.__secret)
# obj = son()
# obj.func()
######################################################
# class father:
#     __secret = "A"
#     def func(self):
#         print(self.__secret)
#         print(father.__secret)
# class son(father):
#     pass
# obj = son()
# obj.func()
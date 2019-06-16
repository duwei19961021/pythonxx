# 1、类或对象是否能做字典的key、value
# 2、对象中有什么？
# class foo(object):
#     def __init__(self,age):
#         self.age = age
#     def display(self):
#         print(self.age)
# data_list = [foo(8),foo(9)]
# for item in data_list:
#     print(item.age,item.display())
# class test(object):
#     def __init__(self,num):
#         self.num = num
#     def display(self):
#         print(self.num)
# # data = [test(8),test(9)]
# # for item in data:
# #     print(item.num,item.display())
# obj = test(9)
# print(obj.dis play())

# class Base(object):
#     def f1(self):
#         print("5")
#
# class Foo(object):
#     def f1(self):
#         print("3")
#         Base.f1(self) #主动调用
#
# # obj = Foo()
# # obj.f1() #调用时现在自己的类中找，没有则去父类中寻找。
# obj = Foo()
# obj.f1()
# class Base(object):
#     def f1(self):
#         print("base.f1")
# class Foo(object):
#     def f1(self):
#         print("Foo.f1")
#         super().f1()
# class Bar(Base,Foo): #Base和Foo的顺序不一样，结果不一样
#     pass
# obj = Bar()
# obj.f1()
# class Foo(object):
#     def __init__(self,a):
#         self.a = a
#
#     def __call__(self, *args, **kwargs):
#         print(args,kwargs)
#
#     def  __getitem__(self, item):
#         print(item)
#
#     def __setitem__(self, key, value):
#         print(key,value)
#
#     def __delitem__(self, key):
#         print(key)
#
#     def __add__(self, other):
#         pass
# # 类名() 自动执行 __init__
# obj = Foo(1)
# # 对象() 自动执行 __call__
# obj(1,2,3,k=4)
# # 对象[] 自动执行 __getitem__
# obj[1]
# # 对象['xx'] = 11 自动执行 __setitem__
# obj["k1"]
# # del 对象[xx] 自动执行__delitem__
# del  obj['uuu']
# # 对象+对象 自动执行__add__
# obj1 = Foo(1)
# obj2 = Foo(2)
# ret = obj1 + obj2
# class foo(object):
#     def __init__(self,age):
#         self.age = age
# obj = foo(100)
# print(obj.age)
# print(foo(100).age)


# 4、123
# 5、1 666 666
# 6、none 2 3
# 7、2 999 - 3 999
# 8 none 999   * 666 none
# 9、
# 11 1 11
# 12
# 13 345


# class Foo(object):
# #     def __init__(self,a,b):
# #         print(1)
# #         self.a = a
# #         self.b = b
# #     def __new__(cls, *args, **kwargs):
# #         print(2)
# #         return object.__new__(cls) #Python每部创建一个当前类的对象（初始为空）
# # Foo(1,2)
# class Base(object):
#     def f1(self):
#         print("Base.f1",3,sep=":")
# class Foo(Base):
#     def f1(self):
#         print("Foo.f1",5,sep=":")
#         Base.f1(self)
# obj = Foo()
# obj.f1()
# class Foo(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def func(self):
#         pass
#     def __iter__(self):
#         return iter([1,2,3,4,5,6])
#     """
#     如果想要把一个不可迭代对象->可迭代对象:
#     1、在类中定义__iter__方法
#     2、iter内部返回一个迭代器(生成器也是一种特殊的迭代器)
#     """
# obj1 = Foo("duwei",18)
# for i in obj1:
#     print(i)
# class foo(object):
#     list_display = []
#     def get_list_display(self):
#         self.list_display.insert(0,33)
#         print(self.list_display)
#         return self.list_display
# s1 = foo()
# re1 = s1.get_list_display()
# print(re1)
# re2 = s1.get_list_display()
# print(re2)

# class foo(object):
#     list_display = []
#     def get_list_display(self):
#         self.list_display.insert(0,33)
#         return self.list_display
# class base(object):
#     list_display = [11,22]
# s1 = foo()
# s2 = foo()
# re1 = s1.get_list_display()
# print(re1)
# re2 = s2.get_list_display()
# print(re2)

# class foo(object):
#     list_display = []
#     def get_list_display(self):
#         self.list_display.insert(0,33)
#         return self.list_display
# class base(foo):
#     list_display = [11,22]
# s1 = foo()
# s2 = base()
# re1 = s1.get_list_display()
# print(re1)
# re2 = s2.get_list_display()
# print(re2)

# class foo(object):
#     list_display = []
#     def get_list_display(self):
#         self.list_display.insert(0,33)
#         return self.list_display
# class base(foo):
#     list_display = [11,22]
# s1 = base()
# s2 = base()
# re1 = s1.get_list_display()
# print(re1)
# re2 = s2.get_list_display()
# print(re2)
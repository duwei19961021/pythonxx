# def Sum(**kwargs):
#     print(type(kwargs))
# Sum()
# def Max(*kwargs):
#     return max(*kwargs)
# print(dir(dict))
# a = '100'
# for i in a:
#     print(i)

# a = "asdfsdf"
# for i in enumerate(a):
#     print(i)
# -*- coding: utf8 -*-
# s = "A"
# print(format(s,">20"))

#
# def func1():
#     yield 1 #和return一样都能返回数据，yedld返回的是内存地址
# print(func1())

# lis = "asdfsdf"
# for i in lis:
#     print(i)

# List = [j for j in lis]
# print(List)
# List1 = []
# List = [["duweis", "lisisi", "zhanga", "wanger"], ["tomss", "jim", "hahass"]]
# for i in List:
#     for name in i:
#         if name.count("s") == 2:
#             List1.append(name)
# print(List1)

# Lis2 = [name for A in List for B in A if B.count("s") == 2]
# print(Lis2)

# Dict1 = {}
# Dict = {"a":"A", "b":"B", "c":"C"}
# for k,v in Dict.items():
#     Dict1[v]=k
# print(Dict1)
# Dict2 = {A:B for B,A in Dict.items()}
# print(Dict2)
# print(help(sum))
# print(ord("a")) #产看阿斯卡码
# print(ord("中"))
# print(chr(20013))
# print("a\\\c")
# import urllib
# urllib.urlopen("www.baidu.com")
# a = input("dd:")
# print(a)
from os import listdir
# def listdir():
#     print("self")
# listdir()
# from import过程中
# from mymodule import *
# 在mymodule中写__all__ = ['a','b']
# 限制import导入
# import testmodule
# 模块之间不能循环应用，例如：a-b-c-a

# 模块路径搜索
# import sys
# path = r'H:\'
# sys.path.append(path)
# import ...
#
# 包
# 文件夹中有一个__init__.py文件
# 是几个模块的集合
# from glance.api import testmodule
# 直接导入包
# 导入一个包不意味着包下面的所有内容都可以被使用的
import glance
glance.api.testapi.get()
glance.db.testdb.func2()
C:\Users\x1c\PycharmProjects\untitled3\day21-模块导入\glance\api
# -*- coding: utf-8 -*-
# @Time    : 2019/6/16 15:49
# @Author  : duwei
# @FileName: issubclass-type-isinstance.py
# @Software: PyCharm
# @Blog    ：https://github.com/duwei19961021/pythonxx

# class base(object):
#     pass
# class foo(base):
#     pass
# class bar(foo):
#     pass
# print(issubclass(foo,base)) #检查第一个参数是否是第二个参数的子类（foo 是否是 base 的子类）
# print(issubclass(base,foo))

# class foo(object):
#     pass
# obj = foo()
# print(obj,type(obj),sep="\n")

class Foo(object):
    pass
class base(Foo):
    pass
obj = Foo()
print(isinstance(obj,Foo)) # 检查第一个参数（对象）是否是第二个参数（类）的实例
print(isinstance(obj,Foo))
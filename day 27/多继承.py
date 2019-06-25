# -*- coding: utf-8 -*-
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    pass
obj = C()
# 新式类，如果自己或者自己的前辈只要有人继承object，那么就是新式类
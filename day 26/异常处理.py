# -*- coding: utf-8 -*-
class nameerror(Exception):
    def __init__(self,code,msg):
        self.code = code
        self.msg = msg
a = 123
try:
    isinstance(a,int)
    raise nameerror(1000,"nameerror")
except nameerror as e:
    print(e)


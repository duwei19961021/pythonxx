# -*- coding: utf-8 -*-
import  hashlib
# 方法1
# res = hashlib.md5()
# with open("server.py","r") as f:
#     res.update(f.read().encode("gbk"))
# print(res.hexdigest())

# 方法2
# with open("server.py","r") as f:
#     for line in f.read():
#         res.update(line.encode("gbk"))
#     print(res.hexdigest())

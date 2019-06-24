# -*- coding: utf-8 -*-
import hashlib
obj = hashlib.md5()
obj.update("123456".encode('utf-8'))
v = obj.hexdigest()
print(v)
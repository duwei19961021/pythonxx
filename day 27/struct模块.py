# -*- coding: utf-8 -*-
import struct
res = struct.pack("i",1202140)
print(res,len(res))

obj = struct.unpack("i",res)
print(obj[0],type(obj[0]))
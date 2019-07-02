import json
# Dic = {'key1':'value1','key2':'value2'}
# ret = json.dumps(Dic)
# print(type(ret))
# ret1 = json.loads(ret)
# print(ret1,type(ret1),sep='\n')

# a = ' dfdf dfdf '
# print(a.strip(" "))

Dic = {'word':'你好'}
print(json.dumps(Dic,ensure_ascii=False))
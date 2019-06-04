import  re

#findall 查找 匹配符合正则表达式的字符
# ret = re.findall('\d+','1223sadfas3sdfasd3sdf232') #正则表达式，字符串，flag
# print(ret)

#search 只匹配第一个，得到的不是直接的结果，通过group方法获取结果
# ret = re.search('\d+','1223sadfas3sdfasd3sdf232') #正则表达式，字符串，flag
# print(ret) #内存地址
# print(ret.group()) #获取值
#<_sre.SRE_Match object; span=(0, 4), match='1223'> span 为索引，match为结果

# ret = re.search('\d','asdfasdfg')
# print(ret) #找不到时返回none
# print(ret.group()) #找不到时会报错
# if ret:
#     print(ret.group()) #规范写法

#match
# ret = re.match('\d','a345dfg')
# ret = re.search('^\d','a345dfg') #等同于match
# if ret:
#     print(ret.group())

#split
# s = 'asd34uio90'
# ret = re.split('\d+',s)
# print(ret)

#sub
# s = 'asds45sdf090dsf'
# ret = re.sub('\d+','H',s,1) # 旧  新   对象 替换次数
# print(ret)

#subn 替换结果and次数
# s = 'asds45sdf090dsf'
# ret = re.subn('\d+','H',s,1) # 旧  新   对象 替换次数
# print(ret)

#compile 节省时间
# ret = re.compile('\d+')
# print(ret)
# res = ret.findall('adsf45df233445g')
# print(res)
#finditer 节省空间
# ret = re.finditer('\d','23sdf44fd')
# for i in ret:
#     print(i.group())
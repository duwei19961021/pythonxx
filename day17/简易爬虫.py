from urllib import request
import re,os,requests
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1559698399790_R&pv=&ic=undefined&nc=1&z=0&hd=undefined&latest=undefined&copyright=undefined&se=1&showtab=0&fb=0&width=undefined&height=undefined&face=0&istype=2&ie=utf-8&hs=2&sid=&word=%E7%BE%8E%E5%A5%B3'
ret = request.urlopen(url)
ret2 = ret.read().decode('utf-8')
ret3 = re.findall('https://\w+\.\w+\.\w{3}/\w+/\w\w/\w=\d+,\d+&\w\w=\d\d&\w\w=\d\.jpg',ret2)
# ret3 = re.findall('https://ss3.*jpg',ret2)
ret3 = list(set(ret3))
for url in ret3:
    root = r'D:\photo'
    path = root + url.split('/')[-1]
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")

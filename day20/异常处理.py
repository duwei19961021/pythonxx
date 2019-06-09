# try:
#     name = a
# except NameError:
#     print(1)

# 多行报错的原因：在嵌套调用过程中，内部的代码出了问题，外部所有调用的地方都成为报错信息的一部分(自下往上找)

# 多分支异常处理
# try:
#     ...
#     ...
# except ...:
#     ...
# except ...:
#     ...

# 多分支合并
# try:
#     ...
# except(...,...):
#     ...

# 万能异常
# try:
#     ...
# except Exception as f:
#     print(f)
# else: #万能分支，tyr中的代码不发生异常的时候走else分支，比如说
#     ...
# finally: #无论如何都会执行，优先执行，例如打开一个文件之后关闭文件,常用来回收一些系统资源：数据库连接、网络连接、打开的文件句柄
#     ...

# with open("a.txt",'w') as f:
#     f.write("aaa")
# f.close()
import random
List = []
hongbao = []
a, b = 100, 10
for i in range(b-1):
    ret = random.randint(0,a)
    List.append(ret)
List = sorted(List)
for i in range(b):
    if i == 0:
        hongbao.append(List[i]-0)
    elif 0 < i <= b-2:
        hongbao.append(List[i]-List[i-1])
    else:
        hongbao.append(a-List[-1])
print(List)
print(hongbao)
print(len(hongbao))
print(sum(hongbao))

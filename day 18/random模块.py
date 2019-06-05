import random
# print(random.random())
# print(random.uniform(1,2))
# print(random.randint(-1,2))
# print(random.randrange(1,10,3))
# List = [1,3,4,[5,6],7,8,9,10]
# while 1:
    # print(random.choice(List))
# print(random.sample(List,2))
# print(random.shuffle(List))
# List = [0,1,2,3,4,5,6,7,8,9]
# print(random.sample(List,4))
# def Verification():
#     List1 = ['1','2','3','4','5','6','7','8','9']
#     List2 = random.sample(List1,6)
#     str1 = "".join(List2)
#     print(str1)
# def Verification():
#     List1 = ['1','2','3','4','5','6','7','8','9']
#     List2 = random.sample(List1,6)
#     str1 = "".join(List2)
#     return str1
# print(Verification())

def code(n=6): #数字验证码
    s = ''
    for i in range(n):
        str1 = random.randint(0,9)
        s += str(str1)
    return s
print(code())
# res=lambda a,b:a+b
# print(res(3,4))
#
#
# lsit=[(1,2),(2,3),(3,4),(4,5),(5,6)]
# lsit.sort(key=lambda x:x[1],reverse=True)
# print(lsit)
# print(lsit)
# 1. 使用lambda表达式，随机传入任意多个数据，并计算累加和， 使用两种方式调用（*args）
from importlib.metadata import files

# re= lambda *args: sum(args)
# print(re(1,2,3,4))
#
# re1=(lambda *args: sum(args))
# print((lambda *args: sum(args))(1,3,6))

# 2. 使用lambda表达式，计算a 和 b 中的较大值，并返回（选做）
# re=lambda a,b:a if a>b else b
# print(re(10,20))

# 3. 使用lambda进行排序, 排序规则是按照元素除以4的余数大小进行排序
# list1=[3,4,5]
# list1.sort(key=lambda x:x%4)
# print(list1)
# 斐波那契数列
# def match(n):
#     if n in (1,2):
#         return 1
#     else:
#         return match(n - 1) + match(n-2)
# re = match(6)
# print(re)
files=open('C:/Users/98501/Desktop/123.txt','r',encoding='utf-8')
print(files.readlines())
files.close()

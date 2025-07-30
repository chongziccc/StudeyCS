dict1={'name':'zhangsan','age':18}
# print(dict1['name'])
# dict1.update({'ce':'fe'})
# dict1['d']=56
# print(dict1)
# b=dict1.pop('ce')
# print(b)
# dict1.popitem()
# print(dict1)
# dict1.clear()
# print(dict1)

print(dict1['name'])
print(dict1.get('nam'))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(type(dict1.values()))
for k,v in dict1.items():
    print(k,v,sep=':')

list1=dict1.keys()
print(list1)
ls=list(list1)
print(ls[0])
# * 乘法运算符
# 2. 容器类型相加,就是将容器赋值n份并相加
# str
print('123' * 3)  # 123123123
# list
print([1, 2, 3] * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# tuple
tuple3 = (1, 2, 3)
print(max(tuple3))
print(min(tuple3))
del(tuple3)
print(tuple3)
# 乘法运算不会修改容器的原有数据,而是产生了一个新的数据容器
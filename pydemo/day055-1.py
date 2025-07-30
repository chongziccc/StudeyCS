lsit=['a','b','c','d','e','f']
str='x'
b=str.join(lsit)
print(b)
lsit.append(['a','2'])
lsit.extend(['b','3'])
print(lsit)
print(lsit.count('a'))
list_num = [1, 2, 3, 3, 2, 1]
for num in list_num:
    if num==3:
        list_num.remove(3)
print(list_num)

list_num.pop(2)
print(list_num)

list_num.clear()
print(list_num)

for num in range(list_num.count(3)):#统计数列中的3的个数，循环次数
    list_num.remove(3)
    print(list_num)

for num in list_num[:]:#复制数组，然后在复制的数组内进行匹配
    if num==3:
     list_num.remove(3)
print(list_num)
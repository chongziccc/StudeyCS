# 需求1:创建一个列表,内部是从0-9的数字
# for
list1=[i for i in range(10) ]
print(list1)

#添加偶数加入数列
list2=[]
for i in range(10):
    if i % 2 == 0:
        list2.append(i)
print(list2)

list3=[i for i in range(10) if i % 2 == 0]
print(list3)

list5=[]
for i in range(1,11):
    list5.append(f'cceshi{i}')
print(list5)

list6=[f'ceshi{i}.jpg' for i in range(1,12) ]
print(list6)

#创建元组的时候需要加逗号，不然就成了默认的类型数据
tuple=(3)
print(type(tuple))
tuple1=(3,)
print(type(tuple1))

#创建元组的时候可以不加外层括号，系统会自己补上
tuple2=4,
tuple5=1,2,3,9,8,7
print(type(tuple5))
#元组可以分割，产生新对象
print(tuple5[2:4])
list1 = ['Tom', 'Jack', 'Rose', 'Dave']
#修改数据内容
index=list1.index('Tom')
list1[index]='cuihua'
list1.append('ce')
list1.extend('fes')
print(list1)

#列表的内容反转
list1 = [1, 5, 6, 3, 4, 8, 2]
list1.reverse()#没有返回值，返回值就是none，只能先反转然后再进行输出
print(list1)

b=list1[-1:-5:-1]#产生新的列表
print(b)

list3 = [1, 5, 6, 3, 4, 8, 2]

list3.sort()
list3.reverse()
print(list3)

list3.sort(reverse=True)
print(list3)

school_names = [['北京大学', '清华大学'], ['南开大学', '天津大学'], ['复旦大学', '河北大学']]
for names in school_names:
    for name in names:
        print(name)

# 题目 1: 给定列表 list1 = [10, 20, 30, 40, 50]，请完成以下操作：
#
# 使用 remove 删除元素 30。
#
# 使用 pop 删除索引为 2 的元素，并输出被删除的元素。
#
# 清空该列表并输出列表内容。

#
#方法一
'''
for item in range(list1.count(30)):
    list1.remove(30)
    print(list1)

#方法二
#list1 = [10, 20, 30, 30,40,30, 50]
list1 = [10, 30, 30, 40]

de=list1.pop(2)
print(de)

list1=[item for item in list1 if item!=30]
print(list1)
print()

for item in list1[::]:
    if item==30:
       list1.remove(item)
print(list1)
list1.clear()
print(list1)


#**题目 2**: 给定列表 `list2 = [1, 2, 3, 4, 5, 6]`，逆转该列表并输出结果。

list2 = [1, 2, 3, 4, 5, 6]
list2.reverse()
print(list2)
# list2.sort(reverse=True)
# print(list2)
'''
#**题目 4**: 创建一个包含 5 个元素的元组 `tuple1 = (1, 2, 3, 4, 5)
# 1. 使用切片操作提取倒数第二个到最后一个元素。
# 2. 尝试修改元组中的元素，观察会发生什么。
# 3. 尝试删除元组中的元素，观察会发生什么。
#
# tuple1=(1,2,3,4,5)
# print(tuple1[-2:-1])

### 3. **集合操作**

# - **题目 6**: 给定集合 `set1 = {1, 2, 3, 4, 5}`，请完成以下操作：
#   1. 添加元素 `6` 到集合中。
#   2. 删除元素 `3`。
#   3. 判断 `2` 是否存在于该集合中。
#   4. 创建一个新的集合 `set2 = {4, 5, 6, 7, 8}`，并求出 `set1` 和 `set2` 的交集与并集。

# ste1={1,2,3,4,5}
#
# set2 = {4, 5, 6, 7, 8}
#
# ste4=ste1.intersection(set2)
# print(ste4)
# - **题目 7**: 创建字典 `dict1 = {'name': 'Alice', 'age': 25, 'city': 'New York'}`，完成以下操作：
#   1. 修改 `age` 键的值为 `30`。
#   2. 添加新的键值对 `'job': 'Engineer'`。
#   3. 删除 `city` 键并输出删除的值。
# - **题目 8**: 创建字典 `dict2 = {'name': 'Bob', 'age': 20, 'city': 'London'}`，使用 `get` 方法获取 `city` 的值，并设置默认值 `Unknown`。
# - **题目 9**: 给定字典 `dict3 = {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}`，遍历字典并输出每个键值对。
#
# dict2={'name':'zhangsan','age':25,'city':'New York'}
# dict2['age']=30
# dict2.update([('key','ceshi')])
# dict2['kei']='jiushi'
# print(dict2)
#
# dict3 = {'name': 'Bob', 'age': 20, 'city': 'London'}
# dict3.setdefault('age','11')
# print(dict3)
# print(dict3.get('city'))


# dict3 = {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
# for item in dict3.items():
#     print(item)

# - **题目 10**: 给定列表 `list4 = [1, 2, 3, 4, 5, 6, 7]`，通过列表推导式生成一个新列表，包含所有偶数的平方值。
# - **题目 11**: 给定数字列表 `list5 = [12, 15, 20, 25, 30]`，使用列表推导式生成一个新列表，其中包含大于 20 的元素，并将它们乘以 2。
# list4 = [1, 2, 3, 4, 5, 6, 7]
# list4=[ite*ite for ite in list4 if ite%2==0 ]
# print(list4)
### 7. **删除操作**
#
# - **题目 15**: 给定字典 `dict5 = {'name': 'Alice', 'age': 25, 'city': 'New York'}`，使用 `pop` 方法删除 `age` 键并打印删除的值。
# - **题目 16**: 给定列表 `list7 = [1, 2, 3, 4, 5]`，使用 `del` 删除索引为 `2` 的元素，并打印删除后的列表。
# dict5 = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# re=dict5.pop('age')
# print(re)
# list7 = [1, 2, 3, 4, 5]
# del list7[2]
# print(list7)
### 综合应用：

# - **题目 17**: 给定列表 `list8 = [1, 2, 3, 4, 5, 6, 7]`，请完成以下操作：
#   1. 使用列表推导式生成一个新列表，包含所有奇数的平方值。
#   2. 使用 `remove` 删除所有 `4`，并打印删除后的列表。
# - **题目 18**: 给定字典 `dict6 = {'name': 'Eve', 'age': 28, 'city': 'Boston'}`，完成以下操作：
#   1. 使用 `get` 方法获取 `name` 对应的值。
#   2. 使用 `popitem` 删除最后一个键值对，并打印结果。


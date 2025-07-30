# 一 题
# def greet(name):
#     print(f"{name}爱你呀大王")
# greet('我')

# def sumcla(a,b):
#     return a+b
# sum1=sumcla(3,2)
# print(sum1)
#
# def tringecla(base,height):
#     return base*height/2
# sum2=tringecla(3,2)
# print(sum2)

# def greets(name,greeting='hello'):
#     print(f'{name}你好{greeting}')
#
# greets('san','working')
# greets('cen')

#
# def calculates(a,b):
#     sum1=a+b
#     ser=a/b
#     ca=a*b
#     return sum1,ser,ca
# re=calculates(3,6)
# for i in re:
#     print(i)
# print(re[0],re[1],re[2])

#定义一个函数 `sum_of_numbers(*args)`，使用不定长参数接收任意数量的数字，并返回它们的总和。调用该函数并计算 `1, 2, 3, 4, 5` 的和。

# def sum_of_numbers(*args):
#     num1=0
#     for num in args:
#         num1+=num
#     return num1
# print(sum_of_numbers(1,2,3,4,5))

# 编写一个函数 `person_info(name, age, city)`，接受 `name`、`age` 和 `city`
# 作为参数，并打印一条包含这些信息的字符串。然后使用关键字参数调用该函数，传入这三项信息。

# def person_info(name,age,city):
#     print(f'name:{name},age:{age},city:{city}')
#
# person_info(name='san',age=18,city='New York')
#
 #定义一个全局变量 `num = 10`，然后定义一个函数 `modify_num()`，该函数修改 `num` 的值为 `20`。调用该函数并打印修改后的 `num`。
#
# num=10
# def modify_num():
#     global num
#     num=20
#     print(num)
# modify_num()
#
# 定义一个全局变量 `counter = 0`，然后定义一个函数 `increment_counter()`，该函数使用 `global`
# 关键字使得全局变量 `counter` 自增 1。调用该函数并输出自增后的 `counter` 值。

# counter1=0
# def increment_counter():
#     global counter1
#     counter1+=1
#     print(counter1)
# increment_counter()
# 定义一个外部函数 `outer()`，它调用内部函数 `inner()`，并且 `inner()` 打印
# "Inside inner function!"。调用 `outer()`，并观察嵌套函数如何被调用。
# def inner():
#     print("inner function")
#
# def outer():
#     inner()
# outer()

# 创建两个列表 `list1` 和 `list2`，使得 `list2` 引用 `list1`，然后修改 `list1` 的内容，
# # 打印 `list2` 的内容，观察它们是否发生了变化。同时使用 `id()` 查看两个列表的内存地址，分析它们为什么相同。
# list1=[1,2,3]
# print(list1)
# lsit2=list1
# print(id(lsit2))
# print(id(list1))


#创建一个字符串 `str1 = "Hello"`，尝试通过修改字符串的某个字符来改变它的内容，观察是否会报错并分析原因。
# str1='hello world'
# str1[2]='c'
# print(str1)
# 编写一个函数 `show_info(name, age=18)`，如果调用时没有提供 `age`，则默认为 `18`。
# 调用该函数时分别传入和不传入 `age`，观察返回结果。
# def show_info(name,age=18):
#     print(name,age)
#
# show_info('san')
# # show_info('san',age=24)
# 编写一个函数 `average(*args)`，使用不定长参数接收多个数字，并返回这些数字的平均值。
# 调用该函数并传入 `2, 4, 6, 8, 10`，打印平均值。

# def average(*args):
#     return sum(args)/len(args)
#
# 定义一个函数 `student_info(**kwargs)`，接受任意数量的关键字参数，打印传入的信息。
# 调用该函数时传入不同数量的参数，如 `name="Alice", age=25, city="New York"`。
#
# 这些题目将帮助你深入理解和掌握函数的定义、参数传递、
def student_info(**kwargs):
    print(kwargs)

student_info(name='san',age=12,city='shanghai')
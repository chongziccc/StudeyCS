# def prt(n):#输入一个数打印横线
#     for i in range(n):
#       print('-'*30)
# prt(10)
# num1=0
# def func3():
#     # 如果想要自增需要先声明num1为全局变量
#     global num1
#     # UnboundLocalError: local variable 'num1' referenced before assignment
#     # 因为num1 += 1 等价于 num1 = num1 + 1 此时我们num1= 被检索到,系统认为其有局部变量,优先使用局部变量,但是+1时局部变量还没有赋值,所以报错
#     num1 += 1
#     print(num1)
#
# func3()
#
# print(num1)
# def function1(a,b,c,d):
#     print(a,b,c,d)
# function1(b=1,c=2,d=3,a=8)
#计算多个数的平均值
def avgcla(*args):
 um1=sum(args)/len(args)

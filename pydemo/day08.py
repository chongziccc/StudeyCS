#编写一个程序，要求用户输入一个整数并计算其平方根。如果输入的不是正整数或负数，程序应捕获异常并提示用户输入有效数字。
# import math
#
# person_str=input('输入一个数字')
# try:
#
#         nums=math.sqrt(int(person_str))
#         print(nums)
# except Exception as e:
#     print(e)
#编写一个程序，读取一个名为 data.txt 的文本文件，统计文件中每行的字数，并输出每一行的字数总和。
# with open('output.txt','r') as f:
#     files_contenr=f.readlines()
#     i = 1
#     for itm in files_contenr:
#         number=len(itm.split())
#         print(f'第{i}行有{number}个字符')
#
#         i+=1
import demos
from demos import *
num=demos.demo_fuc.add(3,5)
mun=demos.sub(3,5)
print(num)
print(mun)

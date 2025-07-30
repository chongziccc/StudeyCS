import random
'''
sorce=float(input('请输入小明的成绩'))
if sorce>90:
    print('A')
elif sorce>80 and sorce<90:
    print('B')
else:
    print('C')
    random.randint(1,3)
    '''

i,j=0,0
while i<=100:
    if i%2==0:
     j=i+j
    i=i+1
print(f'所有偶数的和是{j}')
print('-'*20)
print('1.添加学员信息')
print('2.修改学员信息')
print('3.删除学员信息')
print('4.查询学员信息')
print('5.输出所有学员信息')
print('6.退出学员系统')
print('-'*20)
sel=int(input('输入你的选择'))
lists=[]
list1={'name':'sab','age':15,'StudentNo':124}
lists.append(list1)
def addStudents():
    print("输入学员信息")
    name=input('输入学员名字')
    age=input('输入学员的年龄')
    StudentsNo=input('请输入学号')
    list={'name':name,'age':age,'StudentNo':StudentsNo}

    lists.append(list)


def modifyStudents():
    Nos=input('输入你要修改同学信息的学号')
    persons=selStudents()

    pass

def delStudents():


    pass
def selStudents():
    nos=int(input('输入你要修改同学信息的学号'))
    for item in lists:
        if item['StudentNo']==nos:
            item['name']=input('请输入你要修改的学生姓名')
            item['age']=input('请输入年龄信息')
        else:
            print('没有该学生的信息，无法修改')

def exitStudents():
    print('退出系通')
    exit()
def displayStudents():
    pass

while True:
      if sel==1:
         addStudents()
      elif sel==2:
           modifyStudents()
      elif sel==3:
           delStudents()
      elif sel==4:
           selStudents()
      elif sel==5:
           displayStudents()
      elif sel==6:
           exitStudents()
      else:
          exitStudents()
      sel=int(input('输入编号'))

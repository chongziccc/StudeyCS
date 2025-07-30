# person_info=input('输入您要备份的文件')
# files_name=open(f'{person_info}.txt','r',encoding='utf-8')
# liststr=files_name.readlines()
# files_backup=open(f'{person_info}beifen.txt','w',encoding='utf-8')
# files_backup.writelines(liststr)
# files_name.close()
# files_backup.close()
# filesdis=open(f'{person_info}.txt','r',encoding='utf-8')
# lists=filesdis.readlines()
# print(lists)
# filesdis.close()
#
# with open('output.txt', 'r',encoding='utf-8') as f:
#     content=f.read(102)
#     while content:
#          content = f.read(102)
#          print(content)
# if content=='':
# #     print('内容已经读取完毕')
# import os
#
# s=os.getcwd()
# booo=os.path.dirname(f'{s}ceshi')
# if booo:
#      print('文件已经存在')
# else:
#     s.mkdir(f'{s}ceshi')
#
# with open(f'{s}ceshi/file.txt', 'w') as f:
#        f.write('hello')
#
# print(os.listdir())

#编写一个程序，将一个 UTF-8 编码的文件的内容转换为 GBK 编码，并保存为新的文件。

# def switch():
#     with  open('output.txt','r',encoding='utf-8') as f:
#           lists=f.read()
#           if lists:
#               with open('output1.txt','w',encoding='GBK') as s:
#                   s.write(lists)
#     with open('output1.txt','r') as f:
#         ss=f.read()
#     print(f'{ss}')
# 编写一个程序，打开一个文件并尝试读取它。如果文件不存在，程序应该提示用户输入正确的文件路径，
# 然后重新打开文件并读取内容。使用 `try-except` 来捕获文件打开时的异常。
# try:
#     files=open('output22.txt', mode='r',encoding='utf-8')
# except OSError:print('文件不存在')

# 编写一个程序，用户输入一个图片文件（如 `.jpg` 文件）的路径，程序应将该文件的字节内容备份到另一个文件。
# 使用 `rb` 和 `wb` 模式处理字节型文件。

file_path=input('输入文件名')
with open(file_path, 'rb') as f:
    strs=f.read()
    print(strs)
    
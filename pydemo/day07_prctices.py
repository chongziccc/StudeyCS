#编写一个程序，创建一个名为 `sample.txt` 的文件，并在其中写入以下内容：
# res=open('sample.txt','w',encoding='utf-8')
# lists=['hello world\n','inwejfds\n']
# res.writelines(lists)
# res.close()
# re=open('sample.txt','r',encoding='utf-8')
# print(re.read())
# re.close()
### 2. **文件写入和覆盖**

# 创建一个名为 `output.txt` 的新文件，写入以下内容：
#
# ```
# Line 1: Python
# Line 2: Java
# Line 3: C++
# ```
#
# 然后，使用 `w` 模式打开该文件，并覆盖文件内容为：
#
# ```
# Python is fun.
# Java is powerful.
# C++ is fast.
# ```

### 3. **文件追加操作**
creates=open('output.txt', 'w', encoding='utf-8')
strs=['python is fun\n','java is powerful\n','c++ is fast']
creates.writelines(strs)
creates.close()

displays=open('output.txt', 'r', encoding='utf-8')
print(displays.read())
displays.close()

adds=open('output.txt', 'a', encoding='utf-8')
str1=['hello\n','words\n']
adds.writelines(str1)
adds.close()

ad=open('output.txt', 'r', encoding='utf-8')
print(ad.read())
ad.close()
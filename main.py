# fo = open("1234.txt", "w+")
# fo.write("123455")
# # str = fo.read(10)
# # print ("读取的字符串是 : ", str)
# # 关闭打开的文件
# fo.close()
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 打开一个文件
with open('python小课堂/1234.txt', encoding='utf-8') as f:
    fo = f.read()
str_new = fo.split()
new = open("new.txt","w")
new.write(fo)
print(str_new)


# 关闭打开的文件
fo.close()
new.close
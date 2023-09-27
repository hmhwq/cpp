# fo = open("1234.txt", "w+")
# fo.write("123455")
# # str = fo.read(10)
# # print ("读取的字符串是 : ", str)
# # 关闭打开的文件
# fo.close()
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 打开一个文件
# with open('python小课堂/1234.txt', encoding='utf-8') as f:
#     fo = f.read()
# str_new = fo.split()
# new = open("new.txt","w")
# new.write(fo)
# print(str_new)


# # 关闭打开的文件
# fo.close()
# new.close

'''
# --按行读取TXT文件列表-返回txt文本数组
def get_txt_lines():
    # --可以是相对路径-也可以是绝对路径
    file = open(r"check.txt", encoding='utf8')
    data = file.readlines()
    for line in data:  # --打印每行数据
        print(line)
    file.close()  # --关闭文件-释放资源
    return data
 
 
# 1.--调用例子--
list_txt = get_txt_lines()
 
# # 2.--取出第一行数据-下标从0开始-
# row_one = list_txt[0]
 
# # 3.--循环遍历--
# for txt_item in list_txt:
#     print(txt_item)
 
# # 4.--按逗号(,)分割字符串-分割出来是数组形势
# split_list = row_one.split(',')
 
# # --取出分割的第一个字符串-下标从0开始-
# split_one = split_list[0]
 
# # 5.--number类型转字符串类型--
# number_test = 100
# str_number = str(number_test)


# # 1.--写入txt文件，原有数据清空--
# def set_txt_one():
#     f = open('test.txt', 'w')
#     f.write('set_txt_one!')
#     f.close()

# set_txt_one()
'''


fo = open()

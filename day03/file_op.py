#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#data = open("yesterday",encoding="utf-8").read()
   #Windows系统中是gbk的编码，该IDE中是utf-8进行编码，因此打开此文件需要进行转码

#文件打开后需要赋给一个变量，方便对文件进行操作

'''
f = open("yesterday",'w',encoding="utf-8")  #文件句柄，包括文件名，字符集，大小，在硬盘的起始位置
                                            #第二个参数文件操作模式
f.write("我爱北京门")         #覆盖写入，将之前的内容覆盖
f.close()  #文件关闭
f2 = open("yesterday2",'a',encoding="utf-8")  #模式'a'是追加模式
f2.write("我爱北京门....\n")   #追加到最后的位置
f2.write("天门太阳向上升...")
f2.close()
'''

f = open("yesterday",'r',encoding="utf-8")  #文件句柄，包括文件名，字符集，大小，在硬盘的起始位置
print(f.readline())   #读出一行数据
for i in range(5):
    print(f.readline())   #读取前五行的数据

#读取全部文件内容
for index,line in enumerate(f.readline()):    #readline()将每行数据设置为一个列表，读取所有内容及遍历列表,适合读小文件
                                             #enumerate列出数据和数据下标,index是取数据的下标
    if index == 9:
        print("-----")       #将第十行有分割线代替
        continue
    print(line.strip())  # 在此文件中每行都有隔行符，strip()去掉隔行符和空格


#更有效率的读取文件
count = 0
for line in f:    #此时的数据不是上面的列表，此时的f是一个迭代器
    if count == 9:
        print("-----")
        continue
    count += 1
    print(line)   #一行读取存入内存，然后读取另一行，将上一行内容换出，存入内存，效率高，不占用内存

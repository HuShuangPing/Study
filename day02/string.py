#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#字符串
#对字符串不可以修改
name = "my name is {name} and age is {age}"
print(name.capitalize())    #首字母大写
print(name.count("a"))      #统计字母"a"有多少个
print(name.center(50,"-"))  #打印50个字符，空白处用"-"
print(name.endswith("ex"))  #判断一段字符串以什么结尾，返回布尔值
print(name.find("y"))       #返回查找字母的位置（从0开始）
print(name[name.find("name"):8])
print(name.format(name="alex",age="18"))
print(name.format_map({'name':'alex','year':12}))   #字典
print("ab".isalpha())      #是否是纯英文字母
print("ab".isdecimal())    #是否是十进制
print("ab".isdigit())      #是否是整数
print("ab".isidentifier()) #判断是不是一个合法的变量名

print("ab".islower())     #判断是不是一个小写
print("ab".isnumeric())   #只有数字存在
print("ab".isspace())     #是不是个空格

print("al ex lil".split("l"))   #以l当分隔符对序列进行分割


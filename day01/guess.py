#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#elif

age = 56
count =0
while count<3:
    guess_age = int(input("输入猜的的年龄"))  # input默认输入的是字符串
    if guess_age == age:
        print("yes,you got it")
    elif guess_age> age:
        print("think smaller")
    else:
        print("thin bigger")
    count+=1
else:
    print("You have tried too many...fuck off")
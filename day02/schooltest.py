#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


func_str ='''
 #include "stdio.h"
 void test(){      //测试方法  
  "printf("in the test")  /*打印一个值
                           并且没有返回值*/ 
     } 
main()
{ 
  int a=1,b=2;    // 定义两个变量
  test()          //调用方法1
} '''
index=-1
while True:
    index =func_str.find('//',index+1)
    index2 = func_str.find("\n",index)
    func_str=func_str.replace(func_str[index:index2],"")
    if index==-1:
        break
index3=-1
index4=-1
while True:
    index3 = func_str.find("/*",index3+1)
    index4 = func_str.find("*/",index3)+2
    func_str=func_str.replace(func_str[index3:index4],"")
    if index3==-1:
        break
print(func_str)


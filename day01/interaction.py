#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#输入与输出
 #格式化输出
name = input("name:");
age =int( input("age:"))    #从键盘中输入的信息都是字符串
salary = input("salary:")

inf = '''
------ Info of %s  ------
Name:%s
Age:%d
salary:%s
''' % (name,name,age,salary)
#第二种输出形式
inf2 = '''
------ Info of %s {_name} ------
Name:{_name}
Age:{_age}
salary:{_salary}
'''.format(__name=name,_name=name,_age=age,_salary=salary)
#第三种输出形式
inf3 = '''
------ Info of %s {0}------
Name: {0}
Age:{1}
salary:{2}
'''.format(name,age,salary)
print(inf3)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import configparser


config = configparser.ConfigParser()
config.read("example.ini")

print(config.sections())   #输出
# print(config["bitbucket.org"]["user"])  #读出

#修改
sec = config.remove_section("bitbucket.org")
config.write(open("example.ini"))   #覆盖原文件


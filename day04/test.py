#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing
'''
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width)//2

print()
print(' '*left_margin + '+' + '-'*(box_width-2)+'+')
print(' '*left_margin + '|' + ' '*text_width    +'|')
print(' '*left_margin + '|' + sentence   +'|')
print(' '*left_margin + '|' + ' '*text_width    +'|')
print(' '*left_margin + '+' + '- '*(box_width-2)    +'+')
print()
'''
'''
for i in range(2):
    print("+ - - - - + - - - - +")
    for i in range(4):
        print("|         |         |")
        print()
print("+ - - - - + - - - - +")
'''
from tqdm import tqdm
from time import sleep
for i in tqdm(range(1,100)):
    sleep(0.01)
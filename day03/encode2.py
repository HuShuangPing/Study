#!/usr/bin/env python
# -*- coding:gbk -*-
# Author:HuShuangPing

import sys
print(sys.getdefaultencoding())
_author_="Alex"

s = "���"   #��Ȼ�ļ��ı�����gbk����Python���õĻ���Unicode����
             #��ʱs����Unicode����
print(s.encode("gbk"))  #��ʱ���ַ�������Unicodeת����gbk����
                        #��ӡ����bytes������gbk�ı�����ʽ
print(s.encode("utf-8")) #������gbkԭ����ͬ
print(s.encode("utf-8").decode("utf-8").encode("gb2312"))
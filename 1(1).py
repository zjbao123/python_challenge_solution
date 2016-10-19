#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
def findLetter(s):
    sum =''
    for i in s:

        if 120>=ord(i)>=97:
             sum +=chr(ord(i)+2)
        elif 122>=ord(i)>=121:
            sum += chr(ord(i)-24)
        else:
            sum += i
    return sum
l = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
print findLetter(l)
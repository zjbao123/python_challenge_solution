#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'

import urllib2, re

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
response = urllib2.urlopen(url)
content = response.read().decode('utf-8')
pattern = re.compile('<!--(.*?)-->', re.S)
match = pattern.findall(content)

str = []
for i in match[1]:
    if i in str:
        pass
    else:
        str.append(i)
        print i + ' ', match[1].count(i)

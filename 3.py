#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'

import urllib2, re

response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
content = response.read()
pattern = re.compile('<!--(.*?)-->', re.S)
match = pattern.findall(content)
with open('e.txt', 'w') as f:
    f.write(match[0])

pattern = re.compile('(?<=[^A-Z][A-Z]{3})[a-z](?=[A-Z]{3}[^A-Z])')
content =''.join((line.strip() for line in open('e.txt','r')))
match = pattern.findall(content)
print ''.join(i for i in match)

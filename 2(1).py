#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'

import urllib2, re

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
response = urllib2.urlopen(url)
content = response.read().decode('utf-8')
pattern = re.compile('-->(.*?)-->', re.S)
match = pattern.search(content)
result = match.group()
pattern2 = re.compile('\n')
result = pattern2.sub('', result)
pattern2 = re.compile('[a-zA-Z0-9]')
str = ('').join(pattern2.findall(result))

print str

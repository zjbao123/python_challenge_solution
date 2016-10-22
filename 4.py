#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
import urllib2, re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
tail = '37278'
while True:
    result = urllib2.urlopen(url + tail)
    str = result.read()
    pattern = re.compile("\d+")
    tail = pattern.search(str).group()
    print tail
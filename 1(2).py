#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

__author__ = 'zjbao123'
intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'
trantab = string.maketrans(intab, outtab)

l = "map"
print l.translate(trantab)
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:11:15 2018

@author: gatesk
"""

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print ('fizzbuzz')
    elif i % 3 == 0:
        print ('fizz')
    elif i % 5 == 0:
        print ('buzz')
    else:
        print (i)
    
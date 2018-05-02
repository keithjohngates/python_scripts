# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:13:08 2018

@author: gatesk
"""
import os

path = r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\GOLD_SGC\fixed_up'

with open('files_to_fix.txt','w') as fout:
    for root, dirs, f in os.walk(path):
        for file in f:
            print (file)
            fout.write(file+'\n')

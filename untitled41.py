# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:31:06 2018

@author: gatesk
"""

import shelve
import matplotlib.pyplot as plt

db =  shelve.open(r"G:\Transit\kgates\DDZ_ASSAY_DH_DRILL_UNIQUE_RINS.db")

rin = input()

df = db[rin]
dfau = df.loc[df['ELEMENT'] == 'Au']
print (dfau[['ELEMENT', 'RESULT', 'UNITS', 'CONV_ELEMENT', 'CONV_RESULT', 'CONV_UNITS', 'HEADING']].describe())
print (dfau['CONV_UNITS'].describe())
dfau['CONV_RESULT'].plot.hist()
plt.show()


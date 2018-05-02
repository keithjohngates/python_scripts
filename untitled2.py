# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:06:24 2018

@author: gatesk
"""

import os
import csv

rins = ['R00030758',
'R00030786',
'R00030863',
'R00030964',
'R00036036',
'R00041701',
'R00054275',
'R00079208',
'R00079594',
'RE0000404',
'RE0000697',
'RE0000704',
'RE0000901',
'RE0002384',
'RE0002571',
'RE0002791',
'RE0003971',
'RE0004030',
'RE0005048',
'RE0005542',
'RE0005962',
'RE0007293',
'RE0007611',
'RE0007685',
'RE0009588']

rindict = {}

for rin in rins:
    print (rin)
    rindict[rin] = []
    

def get_file_delimiters(filepath):
    with open(filepath, 'r') as fin:
        line = fin.readline()
        try:
            dialect = csv.Sniffer().sniff(line, delimiters = '\t,')
            if dialect.delimiter == '\t':
                delimiter = '\t'
            elif dialect.delimiter == ',':
                delimiter = ','
            else:
                delimiter = 'unk'
        except:
            delimiter = 'unk'
    return delimiter

def count_D(fin):
    Dcount = 0
    with open(fin,'r') as fin:
        for line in fin:
            if line.startswith('D'):
                Dcount = Dcount + 1
    return Dcount

for a,b,c in os.walk(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO_RENAMED_FIXED'):
    for file in c:
        filepath =  os.path.join(a,file)
        rin = file.split('_')[0]
        print (rin)
        rindict[rin].append(count_D(filepath))
        


for key,value in rindict.items():
    tot = 0
    for i in value:
#        print (i)
        tot = tot + i
    print (tot)
#    rindict[rin] = [rindict[rin],tot]
    
print (rindict)
    
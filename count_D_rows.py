# -*- coding: utf-8 -*-
"""
Created on Tue May  1 07:25:17 2018

@author: gatesk
"""

import os
import csv

def get_file_delimiters(f):
    with open(f, 'r') as fin:
        line = fin.readline()
        dialect = csv.Sniffer().sniff(line, delimiters = '\t,')
        if dialect.delimiter == '\t':
            delimiter = '\t'
        elif dialect.delimiter == ',':
            delimiter = ','
        else:
            delimiter = 'unk'
    return delimiter



def D_rows(filein,rin):
    drows = 0
    with open(filein,'r') as fin:
        reader = csv.reader(fin,delimiter=delimiter)
        for row in reader:
            try:
                if row[0] == 'D':
                    drows = drows + 1
            except:
                pass
    return drows


rin_D_file_count = {}

for root,dirs,files in os.walk(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO_RENAMED_FIXED'):
    for f in files:
        rin = f.split('_')[0]  
        rin_D_file_count[rin] = []
        

for root,dirs,files in os.walk(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO_RENAMED_FIXED'):
    for f in files:
        fpath = os.path.join(root,f)
        delimiter = get_file_delimiters(fpath)
        rin = f.split('_')[0]        
        d_rows = D_rows(fpath,rin)
        print (f,rin)
        rin_D_file_count[rin].append(d_rows)
        
for key,value in rin_D_file_count.items():
    print (key,sum(value))
        
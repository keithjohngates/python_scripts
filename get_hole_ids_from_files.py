# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:18:04 2018

@author: gatesk
"""

import os
import csv
holeidset = set()


def get_file_delimiters(fin):
    with open(fin, 'r') as fin:
        line = fin.readline()
        dialect = csv.Sniffer().sniff(line, delimiters = '\t,')
        if dialect.delimiter == '\t':
            delimiter = '\t'
        elif dialect.delimiter == ',':
            delimiter = ','
        else:
            delimiter = 'unk'
    return delimiter

def getholeids(fin,delimiter):
    reader = csv.reader(open(fin,'r'),delimiter=delimiter)
    for row in reader:
        if row[0] == 'H1000':
            holeids = ['hole_id','hole id']
            if any((True for x in row if x.lower() in holeids)):
                pass
                return fin
            else:
                print (fin)

def getrin_and_holeids(fin,delimiter):
    reader = csv.reader(open(fin,'r'),delimiter=delimiter)
    hidx = None
    for row in reader:
        if row[0] == 'H1000':
            for idx, header in enumerate(row):
                if 'hole' in header.lower():
                    hidx = idx
    return hidx

def getrin_holes(fin,delimiter,idx,holeidset):
    reader = csv.reader(open(fin,'r'),delimiter=delimiter)
    rin = os.path.split(fin)[1].split('_')[0]
    try:
        for row in reader:
            if row[0] == 'D':
               holeid = row[hidx]
               holeidset.add((rin,holeid))
        return holeidset
    except Exception as e:
        print (fin,e)
        pass
    return holeidset
           
for root, dirs, files in os.walk(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO_RENAMED_FIXED'):
    for f in files:
        fpath = os.path.join(root,f)
        delimiter = get_file_delimiters(fpath)
        fin = getholeids(fpath, delimiter)
        if fin != None:
            hidx = getrin_and_holeids(fin,delimiter)
            hset = getrin_holes(fin,delimiter,hidx,holeidset)
        else:
            print (fin)
        
rins = ['R00079208',
'R00079594',
'RE0002571',
'RE0003971',
'RE0007611']

with open(r"C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO_RIN_HOLE_IDS_OVER_FROM_FILES.csv",'w') as fout:
    for item in hset:
        if item[0] in rins:
            fout.write(f"{item[0]},{item[1]}\n")
            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            
    
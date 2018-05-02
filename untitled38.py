# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 12:55:51 2018

@author: gatesk
"""
import os
import csv
from gather_db_data_dgc import GatherDatabaseData
from itertools import islice

dbconnection_string = r'DSN=GEODWH;UID=gatesk;PWD=Oldsp00n'
DGFILES = []


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

def create_new_filename(delimiter, rin):
    get_new_filename = GatherDatabaseData(dbconnection_string, rin, delimiter).get_new_filename()
    return get_new_filename

def do_work(root,file):
    path = os.path.join(root,file)
    
    with open(path) as fin:
        head = list(islice(fin, 50))
        for line in head:
            dialect = None
            if line.startswith('H0202'):
                try:
                    dialect = csv.Sniffer().sniff(line, delimiters = '\t,')
                    if dialect.delimiter == '\t':
                        delimiter = '\t'
                    elif dialect.delimiter == ',':
                        delimiter = ','
                    else:
                        delimiter = None
                except:
                    pass
                
                try:
                    if line.split(delimiter)[2][:2] == 'DG':
                        DGFILES.append((path, line.split(delimiter)[2]))
                        print (line.split(delimiter)[2])
                        
                except:
                    print ('No line found')




for a,b,c in os.walk(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO'):
    for file in c:
        print (a)
        print (file)
#        do_work(a, file)
        

for file in DGFILES:
    print (file)

        
        
        
        
        
        
        
        
        
        
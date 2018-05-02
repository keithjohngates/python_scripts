# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:09:18 2018

@author: gatesk
"""
import csv
import os
from gather_db_data_dgc import GatherDatabaseData

dbconnection_string = r'DSN=GEODWH;UID=gatesk;PWD=Oldsp00n'

def create_new_filename(delimiter, rin):
    get_new_filename = GatherDatabaseData(dbconnection_string, rin, delimiter).get_new_filename()
    return get_new_filename

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


for a,b,c in os.walk(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO_RENAMED'):
    for file in c:
        fpath =  os.path.join(a,file)
        delimiter = get_file_delimiters(fpath)
        rin = file.split('_')[0]
        print (rin)
        print (delimiter)
        new_fname = create_new_filename(delimiter,rin)
        print (new_fname)
        
        
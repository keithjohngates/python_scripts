# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 11:00:51 2018

@author: gatesk
"""

import sqlite3
import pandas as pd
import os 
import shutil

destroot = r'G:\Geosurvey\Shared\CogentII\DATA\DIGS_2018_ORIGINAL_DBSOURCE_FILES\LITHOLOGY_FILES_EXTRACT'
conn = sqlite3.connect(r'G:\Geosurvey\Shared\CogentII\DATA\DIGS_2018_ORIGINAL_DBSOURCE_FILES\RINS_v2_dictdb.db')
cur = conn.cursor()
df = pd.read_sql_query("SELECT * from MASTER WHERE geol_guess = 'GEOLOGY'", conn)

outfile = open('headers.txt','w')

def pull_H1000(filepath,rin,delimiter,length,dcount,H1000):
    with open(filepath) as fin:
        if ('H1000') in fin.read():
            print ('H1000',filepath,rin,delimiter)
            for i in str(H1000).split(delimiter):
                
                
                #I am here !!
                #outfile.write(i.strip('\n')+'\n')
            
            if dcount == 'None' or length == 'None' or dcount == '' or length == '':
                print ('H1000 D: invalid')
            elif int(dcount) == int(length):
                print ('H1000 D: valid')
            elif int(dcount) != int(length):
                print ('H1000 D: invalid')
        else:
            print ('non_H1000')

for row in df.itertuples(index=True):
    filepath = getattr(row,'path')
    rin =  getattr(row,'rin')
    
    delimiter = getattr(row,'delim')
    
    if delimiter == 'tab':
        delimiter = '\t'
    elif delimiter == 'csv':
        delimiter = ','
    else:
        delimiter = 'unk'
        
    length = getattr(row,'len')
    dcount =  getattr(row,'D_count')
    H1000 = getattr(row,'H1000')
    
    filepath = filepath.replace('RINS_v2','RINS')
    filename = os.path.split(getattr(row,'path'))[1]
    
    newfilepath = (rin+'_'+filename)
    destpath = os.path.join(destroot,filename)
    
#    shutil.copyfile(filepath,destpath)
    pull_H1000(filepath,rin,delimiter,length,dcount,H1000)
    
outfile.close()
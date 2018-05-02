# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 08:39:42 2018

@author: gatesk
"""

import sqlite3
import pandas as pd


destroot = r'G:\Geosurvey\Shared\CogentII\DATA\DIGS_2018_ORIGINAL_DBSOURCE_FILES\LITHOLOGY_FILES_EXTRACT'
conn = sqlite3.connect(r'G:\Geosurvey\Shared\CogentII\DATA\DIGS_2018_ORIGINAL_DBSOURCE_FILES\RINS_v2_dictdb.db')
cur = conn.cursor()
df = pd.read_sql_query("SELECT * from MASTER WHERE geol_guess = 'GEOLOGY'", conn)

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
    print ((rin,filepath,delimiter),(length,dcount),H1000.split(delimiter))
    
    #print (filepath,rin,delimiter,length,dcount,H1000)
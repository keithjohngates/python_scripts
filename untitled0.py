# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:27:09 2018

@author: gatesk
"""

import pandas as pd
import shelve

df = pd.read_csv(r"C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\DDZ_ASSAY_SURFSAMP_PCT_ERRORS.csv")
dfgb = df.groupby(['RIN','ELEMENT'])

with shelve.open('SURF_ASSAY_PCT_ERRORS.shelve') as db:
    for name, data in dfgb:
        name = f"{name[0]}_{name[1]}"
        print (name)
        db[name] = pd.DataFrame(data)
        
db = shelve.open('SURF_ASSAY_PCT_ERRORS.shelve')
        
with open(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\DDZ_ASSAY_SURF_PCT_ERRORS_DESCRIBE.txt','w') as outf:
    for name, data in db.items():
    #    print (type(data))
        describe = data['CONV_RESULT'].describe()[['min','max']].reset_index()
        describe.pivot(columns='index', values='CONV_RESULT')
        outf.write(name+',')
#        print (describe._slice(slice(0, 2)))
        for index, row in describe.iterrows():
            print (row['CONV_RESULT'])
            outf.write(str(row['CONV_RESULT'])+',')
        outf.write('\n')
            
        print (describe.unstack(0))
#        outf.write(name+',')
        
#outf.write(str(describe.iloc[[0]])+','+str(describe.iloc[[1]])+'\n')


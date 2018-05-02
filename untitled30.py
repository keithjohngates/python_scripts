# -*- coding: utf-8 -*-
"""
Created on Wed May  2 13:06:33 2018

@author: gatesk
"""
import sqlite3
conn = sqlite3.connect(r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT.db")

res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")

with open(r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_DB.txt",'w') as fout:
    for name in res:
        counts = conn.execute(f"SELECT Count() FROM {name[0]}")
        numberOfRows = counts.fetchone()[0]
        print ((name[0]),numberOfRows)
        fout.write(str(name[0])+'|'+str(numberOfRows)+'\t')
        
        columns = conn.execute(f"PRAGMA table_info({name[0]});")
        colist = []
        for col in columns:
            colist.append(col[1])
        for item in colist:
            fout.write(str(item)+'\t')
        fout.write('\n')
    #        dist = conn.execute(f"SELECT distinct ({col[1]}) FROM ({name[0]}) LIMIT 10;")
    #        distincts = dist.fetchall()
    #        for i in distincts:
    #            print (i)
            





#rowsQuery = "SELECT Count() FROM %s" % table
#cursor.execute(rowsQuery)
#numberOfRows = cursor.fetchone()[0]
        
#SELECT distinct REPORT_NO FROM NT_DrillholeSamplesOpen LIMIT 1000
#
#
#distincts = conn.execute(f"SELECT DISTINCT index FROM PETROLEUMWELLS LIMIT 10;")
#distincts.fetchall()
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:38:17 2018

@author: gatesk
"""

fin = open(r"C:\Users\gatesk\Documents\___aaa___PERSONAL\ALL_DOJOS.txt",'r',encoding="utf8")
fout = open(r"C:\Users\gatesk\Documents\___aaa___PERSONAL\ALL_DOJOS_tidy.txt",'w')

keep = ['Address',
'Country',
'Instructors',
'Phone',
'Schedule',
'E-mail',
'Website']

idx = 0

for line in fin:
    print (line)
    if line.startswith('Address'):
        idx = idx + 1
    if line.split(':')[0] in keep:
        fout.write(str(idx)+'|'+str(line.split(':')[0].strip()+'|'+str(line.split(':')[1].strip()+'\n')))
        
fout.close()

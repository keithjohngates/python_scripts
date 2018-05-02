# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:56:21 2017

@author: gatesk
"""

#fin = open("G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DiGS_GBjoin_KG_SIMPLEv2.csv",'r')



f = open("G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DiGS_GBjoin_KG_SIMPLEv2.csv",'r')
contents = f.read()
f.close()
new_contents = contents.replace('\n', ' ')
f = open("G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DiGS_GBjoin_KG_SIMPLEv3.csv",'w')
f.write(new_contents)
f.close()


f = open("G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DiGS_GBjoin_KG_SIMPLEv3.csv",'r')
contents = f.read()
f.close()
new_contents = contents.replace('newline', '\n')
f = open("G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DiGS_GBjoin_KG_SIMPLEv4.csv",'w')
f.write(new_contents)
f.close()

fin = open("G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DiGS_GBjoin_KG_SIMPLEv4.csv",'r')
RINS = set()
DINS = set()
count = 0

foutRINS = open("G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\RINS.csv",'w')
foutDINS = open("G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DINS.csv",'w')

for line in fin:
    count = count+1
    line = line.replace(',','').replace('"','').replace('(','').replace(')','').replace('#','').replace(';','').replace(':','')
    item = line.split('|')
    w = item[1].split(' ')
    print (w)
    
    for i in w:
        RINS.add(i)

    w = item[2].split(' ')
    for i in w:
        DINS.add(i)

for i in RINS:
    foutRINS.write(i+'\n')
for i in DINS:
    foutDINS.write(i+'\n')
    
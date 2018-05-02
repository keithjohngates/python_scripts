# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:31:49 2017

@author: gatesk
"""

'''
OBJECTID,
ORDER_,
FILE_ID,
RPT_ID,
HOLEID,
First__DEP,
First__DIP,
First__AZI,
FILE_ID_1,
PROJECT,
SITE_ID,
TOTDEPTH,
DRILLCODE,
DIP,
AZIMUTH,
ELEVATION,
DATE_DRILL,
UPDATED,
COLOUR,
DIP_USE,
AZI_USE,
SURVEY_COR,
SURVEY_FIE,
Field23,
Field24,
ZONE,
COORDSYS,
SYSTEM,
SYSTEM_1,
ORIG_E,
ORIG_N,
ORIG_epsg,
MGA94_E,
MGA_94_N,
MGA_epsg,
LAT94_OLD,
LNG94_OLD,
LAT94_NEW,
LNG94_NEW,
RASTERVALU
'''

colutmin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_LOC_DATA_INTERNAL_v2_utm_surveys_RL__v2_20171108.csv",'r')
coldict = dict()

for line in colutmin:
    #print (line)
    items = line.split('|')
    HOLEID = (items[4].rstrip())
    E = (items[32].rstrip())
    N = (items[33].rstrip())
    RL =(items[39].rstrip())
    DIP = (items[19].rstrip())
    AZI = (items[20].rstrip())
    #print (HOLEID,E,N,RL,DIP,AZI)
    coldict[HOLEID] = (E,N,RL,DIP,AZI)
    
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\sdfas.csv",'r')
intout = open(r"C:\Users\gatesk\Documents\sdfas_desurveyed.csv",'w')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)
        azi = coldict[HOLEID_ASS][4]
        azi = float(azi)
        phi = azi * 2.0 * pi / 360.0
        dip = coldict[HOLEID_ASS][3]
        dip = float(dip)
        theta = (90.0 - dip) * 2.0 * pi / 360.0
        x = r*cos(phi)*sin(theta)
        y = r*sin(phi)*sin(theta)
        z = r*cos(theta)
        #print (x,y,z)
        xs = float(coldict[HOLEID_ASS][0])
        ys = float(coldict[HOLEID_ASS][1])
        zs = float(coldict[HOLEID_ASS][2])
        xn = xs - x
        yn = ys - y
        zn = zs - z
        #print (xs,ys,zs)
        #print (x,y,z)
        #print (xn,yn,zn)
        #print ('\n')
        intout.write(items[3]+'|'+items[8].rstrip()+'|'+str(xn)+'|'+str(yn)+'|'+str(zn)+'\n')
        #input()
    except Exception as e:
        #print (e)
        intout.write(line)
        #print ('\n')
        pass
intout.close()
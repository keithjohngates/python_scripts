# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:50:06 2017

@author: gatesk
"""

colutmin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_LOC_DATA_INTERNAL_v2_utm.csv",'r')
coldict = dict()

for line in colutmin:
    items = line.split('|')
    HOLEID = (items[1].rstrip())
    E = (items[-1].rstrip())
    N = (items[-2].rstrip())
    RL =(items[13].rstrip())
    DIP = (items[11].rstrip())
    AZI = (items[12].rstrip())
    #print (HOLEID,E,N,RL,DIP,AZI)
    coldict[HOLEID] = (E,N,RL,DIP,AZI)
    
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

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
        print (xs,ys,zs)
        print (x,y,z)
        print (xn,yn,zn)
        print ('\n')
    except Exception as e:
        print (e)
        print ('\n')
        pass
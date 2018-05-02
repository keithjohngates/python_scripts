# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Wed Nov  1 13:33:16 2017)---
import pandas
import pandas as pod
import pandas as pd
df = pd.read_csv("C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DDZ_ASSAY_DH_DRILL_ASSAY.csv",sep='|')
df = pd.read_csv(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DDZ_ASSAY_DH_DRILL_ASSAY.csv",sep='|')
len(df)
df
df.pivot(index='SAMPLEID', columns='HEADING', values='CONV_RESULT')
list(df)
df.pivot(index=('SAMPLEID','TOPP','BASE'), columns='HEADING', values='CONV_RESULT')
list(df)
df.pivot(columns=('DRILLCODE','RPT_ID','ASSAY_FILE_ID','HOLEID','SAMPLEID','SAMPCODE','TOPP','BASE'), values='CONV_RESULT')
df.pivot(columns='DRILLCODE','RPT_ID','ASSAY_FILE_ID','HOLEID','SAMPLEID','SAMPCODE','TOPP','BASE', values='CONV_RESULT')
df.pivot(columns=['DRILLCODE','RPT_ID','ASSAY_FILE_ID','HOLEID','SAMPLEID','SAMPCODE','TOPP','BASE'], values='CONV_RESULT')

## ---(Thu Nov  2 09:07:04 2017)---
import pandas as pd
pd.read_csv("C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_ALL.csv")
df = pd.read_csv(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_ALL.csv")

## ---(Thu Nov  2 10:36:16 2017)---
runfile('C:/Users/gatesk/.spyder-py3/temp.py', wdir='C:/Users/gatesk/.spyder-py3')
x
runfile('C:/Users/gatesk/.spyder-py3/temp.py', wdir='C:/Users/gatesk/.spyder-py3')
import pyproj
import pandas as pd
coldf = pd.read_csv(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_LOC_DATA.csv")
coldf
list(coldf)
import pyproj
coldf
collardf
coldf
import pandas as pd
import pyproj
coldf = pd.read_csv(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_LOC_DATA.csv")
coldf
list(coldf)
from pyproj import Proj, transform
inProj = Proj(init='epsg:4326')
runfile('C:/Users/gatesk/.spyder-py3/temp.py', wdir='C:/Users/gatesk/.spyder-py3')
colout.close()]
colout.close()
runfile('C:/Users/gatesk/.spyder-py3/temp.py', wdir='C:/Users/gatesk/.spyder-py3')
colout.close()
runfile('C:/Users/gatesk/.spyder-py3/temp.py', wdir='C:/Users/gatesk/.spyder-py3')
list(coldf)
runfile('C:/Users/gatesk/.spyder-py3/temp.py', wdir='C:/Users/gatesk/.spyder-py3')
list(coldf)
coldf = pd.read_csv(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_LOC_DATA_utm.csv")
list(coldf)
import numpy as np
colutmin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_LOC_DATA_utm.csv",'r')

for line in colutmin:
    items = line.split(',')
    E = (items[-1].rstrip())
    N = (items[-2].rstrip())
    RL =(items[13].rstrip())
    DIP = (items[11].rstrip())
    AZI = (items[12].rstrip())
    print (E,N,RL,DIP,AZI)
coldict = dict{}
coldict = dict()
colutmin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_LOC_DATA_utm.csv",'r')
coldict = dict()

for line in colutmin:
    items = line.split(',')
    HOLEID = (items[2].rstrip())
    E = (items[-1].rstrip())
    N = (items[-2].rstrip())
    RL =(items[13].rstrip())
    DIP = (items[11].rstrip())
    AZI = (items[12].rstrip())
    print (HOLEID,E,N,RL,DIP,AZI)
    coldict[HOLEID] = (E,N,RL,DIP,AZI)
runfile('C:/Users/gatesk/.spyder-py3/temp.py', wdir='C:/Users/gatesk/.spyder-py3')
coldict
coldict[9172]
coldict['9172']
coldict['9172'][1]
coldict['9172'][2]
coldict['9172'][3]
coldict['9172'][4]
coldict['9172'][5]
coldict['9172'][0]
import numpy as np

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')
import numpy as np

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    print (items[1])

#
import numpy as np

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    print (items[1])
import numpy as np

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    HOLEID_ASS = (items[3])
    INTERVAL = (items[7]-items[6])
    print (HOLEID_ASS, INTERVAL)
import numpy as np

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    HOLEID_ASS = (items[3])
    INTERVAL = (float(items[7])-float(items[6]))
    print (HOLEID_ASS, str(INTERVAL))
import numpy as np

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        INTERVAL = (float(items[7])-float(items[6]))
        print (HOLEID_ASS, str(INTERVAL))
    except:
        pass
runfile('C:/Users/gatesk/.spyder-py3/temp.py', wdir='C:/Users/gatesk/.spyder-py3')
import numpy as np

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        INTERVAL = ((float(items[7])+float(items[6]))/2)
        #print (HOLEID_ASS, str(INTERVAL))
        print (coldict[HOLEID_ASS][1]
    except:
        pass
for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        INTERVAL = ((float(items[7])+float(items[6]))/2)
        #print (HOLEID_ASS, str(INTERVAL))
        print (coldict[HOLEID_ASS][1])
    except:
        pass
import numpy as np

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        INTERVAL = ((float(items[7])+float(items[6]))/2)
        #print (HOLEID_ASS, str(INTERVAL))
        print (coldict[HOLEID_ASS][1])
    except:
        pass
coldict['00ACRC001']
runfile('C:/Users/gatesk/.spyder-py3/temp.py', wdir='C:/Users/gatesk/.spyder-py3')
coldict
coldict['00ACRC001']
runfile('C:/Users/gatesk/.spyder-py3/temp.py', wdir='C:/Users/gatesk/.spyder-py3')
import numpy as np

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    HOLEID_ASS = (items[3])
    r = ((float(items[7])+float(items[6]))/2)
    phi = coldict[HOLEID_ASS][4] * 2 * np.pi / 360
    theta = (90. - coldict[HOLEID_ASS][3]) * 2 * np.pi / 360.
    x = r*np.cos(phi)*np.sin(theta)
    y = r*np.sin(phi)*np.sin(theta)
    z = r*np.cos(theta)
    print (x,y,z)
import numpy as np

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)
        phi = coldict[HOLEID_ASS][4] * 2 * np.pi / 360
        theta = (90. - coldict[HOLEID_ASS][3]) * 2 * np.pi / 360.
        x = r*np.cos(phi)*np.sin(theta)
        y = r*np.sin(phi)*np.sin(theta)
        z = r*np.cos(theta)
        print (x,y,z)
    except Exception as e:
        print (e)
        pass
import math
math.cos(x)
cos(10)
from math import cos
cos(10)
from math import pi
pi
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)
        phi = coldict[HOLEID_ASS][4] * 2 * pi / 360
        theta = (90. - coldict[HOLEID_ASS][3]) * 2 * pi / 360.
        x = r*cos(phi)*sin(theta)
        y = r*sin(phi)*sin(theta)
        z = r*cos(theta)
        print (x,y,z)
    except Exception as e:
        print (e)
        pass
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)
        print (r)
        phi = coldict[HOLEID_ASS][4] * 2 * pi / 360
        print (phi)
        theta = (90. - coldict[HOLEID_ASS][3]) * 2 * pi / 360.
        print (theta)
        x = r*cos(phi)*sin(theta)
        print (x)
        y = r*sin(phi)*sin(theta)
        print (y)
        z = r*cos(theta)
        print (x,y,z)
    except Exception as e:
        print (e)
        pass
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)
        print (r)
        phi = coldict[HOLEID_ASS][4] * 2.0 * pi / 360.0
        print (phi)
        theta = (90.0 - coldict[HOLEID_ASS][3]) * 2.0 * pi / 360.0
        print (theta)
        x = r*cos(phi)*sin(theta)
        print (x)
        y = r*sin(phi)*sin(theta)
        print (y)
        z = r*cos(theta)
        print (x,y,z)
    except Exception as e:
        print (e)
        pass
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)
        print (type(r))
        phi = coldict[HOLEID_ASS][4] * 2.0 * pi / 360.0
        print (type(phi))
        theta = (90.0 - coldict[HOLEID_ASS][3]) * 2.0 * pi / 360.0
        print (type(theta))
        x = r*cos(phi)*sin(theta)
        print (x)
        y = r*sin(phi)*sin(theta)
        print (y)
        z = r*cos(theta)
        print (x,y,z)
    except Exception as e:
        print (e)
        pass
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)

#        print (type(r))
#        phi = coldict[HOLEID_ASS][4] * 2.0 * pi / 360.0
#        print (type(phi))
#        theta = (90.0 - coldict[HOLEID_ASS][3]) * 2.0 * pi / 360.0
#        print (type(theta))
#        x = r*cos(phi)*sin(theta)
#        print (x)
#        y = r*sin(phi)*sin(theta)
#        print (y)
#        z = r*cos(theta)
#        print (x,y,z)
    except Exception as e:
        print (e)
        pass
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)
        print (type(r))
        phi = coldict[HOLEID_ASS][4] * 2.0 * pi / 360.0

#        print (type(phi))
#        theta = (90.0 - coldict[HOLEID_ASS][3]) * 2.0 * pi / 360.0
#        print (type(theta))
#        x = r*cos(phi)*sin(theta)
#        print (x)
#        y = r*sin(phi)*sin(theta)
#        print (y)
#        z = r*cos(theta)
#        print (x,y,z)
    except Exception as e:
        print (e)
        pass
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)
        print (type(r))
        phi = (coldict[HOLEID_ASS][4]) * 2.0 * pi / 360.0

#        print (type(phi))
#        theta = (90.0 - coldict[HOLEID_ASS][3]) * 2.0 * pi / 360.0
#        print (type(theta))
#        x = r*cos(phi)*sin(theta)
#        print (x)
#        y = r*sin(phi)*sin(theta)
#        print (y)
#        z = r*cos(theta)
#        print (x,y,z)
    except Exception as e:
        print (e)
        pass
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)
        print (type(r))
        azi = coldict[HOLEID_ASS][4]
        azi = float(azi)
        phi = azi * 2.0 * pi / 360.0

#        print (type(phi))
#        theta = (90.0 - coldict[HOLEID_ASS][3]) * 2.0 * pi / 360.0
#        print (type(theta))
#        x = r*cos(phi)*sin(theta)
#        print (x)
#        y = r*sin(phi)*sin(theta)
#        print (y)
#        z = r*cos(theta)
#        print (x,y,z)
    except Exception as e:
        print (e)
        pass
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)
        print (type(r))
        azi = coldict[HOLEID_ASS][4]
        azi = float(azi)
        phi = azi * 2.0 * pi / 360.0
        print (type(phi))
        dip = coldict[HOLEID_ASS][3]
        dip = float(dip)
        theta = (90.0 - dip * 2.0 * pi / 360.0
        print (type(theta))
        x = r*cos(phi)*sin(theta)
        print (x)
        y = r*sin(phi)*sin(theta)
        print (y)
        z = r*cos(theta)
        print (x,y,z)
    except Exception as e:
        print (e)
        pass
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')

for line in intin:
    items = line.split(',')
    try:
        HOLEID_ASS = (items[3])
        r = ((float(items[7])+float(items[6]))/2)
        print (type(r))
        azi = coldict[HOLEID_ASS][4]
        azi = float(azi)
        phi = azi * 2.0 * pi / 360.0
        print (type(phi))
        dip = coldict[HOLEID_ASS][3]
        dip = float(dip)
        theta = (90.0 - dip) * 2.0 * pi / 360.0
        print (type(theta))
        x = r*cos(phi)*sin(theta)
        print (x)
        y = r*sin(phi)*sin(theta)
        print (y)
        z = r*cos(theta)
        print (x,y,z)
    except Exception as e:
        print (e)
        pass
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
        print (x,y,z)
    except Exception as e:
        print (e)
        pass
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
        print (xn,yn,zn)
    except Exception as e:
        print (e)
        pass
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
        print (x,y,z)
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
        pass
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
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
list(df)
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
list(df)
df.Au_Technique.unique()
df.Bi_Technique.unique()
gb = df.groupby('Au_Technique')
[gb.get_group(x) for x in gb.groups]
for x in gb.groups:
    print (x)
    
gb.get_group('BCL PM216')
pd.gb.get_group('BCL PM216').to_csv("test.csv")
pd.(gb.get_group('BCL PM216')).to_csv("test.csv")
[gb.get_group(x) for x in gb.groups]
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
df.describe()
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
list(df)
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
list(df)
len(df)
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
=488+223+33+159
488+223+33+159
len(df)
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')

## ---(Fri Nov  3 12:08:55 2017)---
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
df_list = [g for _, g in df.groupby(['Au_Technique', 'As_Technique'])]
df_list
df_list = [g for _, g in df.groupby(['Au_Technique', 'As_Technique'])]
for i in df_list:
    print (len(i))
len(df)
df_list = [g for _, g in df.groupby(['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique'])]
for i in df_list:
    print (len(i))
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
list(df)
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
list(df)
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
import pandas as pd
import os

filesin = ["G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Timbarra Geochem\Twelfth_annual_exploration_report,_EPLs_R00019462_2017-10-23\R00019462_Lab_ALS.xlsx",
 "G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Timbarra Geochem\Twelfth_annual_exploration_report,_EPLs_R00019462_2017-10-23\R00019462_Lab_ALS_Brisbane.xlsx",
"G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Timbarra Geochem\Twelfth_annual_exploration_report,_EPLs_R00019462_2017-10-23\R00019462_Lab_Analabs.xlsx",
"G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Timbarra Geochem\Twelfth_annual_exploration_report,_EPLs_R00019462_2017-10-23\R00019462_Lab_missing.xlsx",
"G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Timbarra Geochem\Twelfth_annual_exploration_report,_EPLs_R00019462_2017-10-23\R00019462_Lab_SGS_Sydney.xlsx",
"G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Timbarra Geochem\Twelfth_annual_exploration_report,_EPLs_R00019462_2017-10-23\R00019462_Lab_TASDofRE.xlsx"]

for f in filesin:
    fname = os.path.split(f)
    fname = os.path.splitext(fname[1])
    df = pd.read_excel(open(f,'rb'), sheetname='Sheet1')
    df[['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']] = df[['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']].fillna(value=0)
    #print (len(df))
    count = 0
    for i, g in df.groupby(['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']):
        g=g.dropna(axis=1,how='all')
        #colcount = "'',"*(len(list(g)))
        #print (colcount)
        #g.loc[0]=[str(colcount)]
        g.to_csv('{}.csv'.format('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\'+str(fname[0])+'_'+str(i).replace('/','_')), header=True, index=False,sep='|')
        count = count+len(g)
    print (count)
for f in os.walk(r'C:\Users\gatesk\.spyder-py3\R00019462'):
    print (f)
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')

## ---(Mon Nov  6 09:45:42 2017)---
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
content[0]
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
elements
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
values
dictonary
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
dictonary
dictionary
keys
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
fin = r"C:\Users\gatesk\.spyder-py3\R00019462\R00019462_Lab_ALS_Brisbane_KG_v2_('FA50 PM209', 'ICP IC588', 'ICP IC588', 'ICP IC588', 'ICP IC588', 0, 0, 0).csv"
findict = dict()
fout = open(r"C:\Users\gatesk\.spyder-py3\R00019462\R00019462_Lab_ALS_Brisbane_KG_v2_('FA50 PM209', 'ICP IC588', 'ICP IC588', 'ICP IC588', 'ICP IC588', 0, 0, 0)_HEADERS.csv",'w')

with open(fin) as f:
    content = f.readlines()
    keys = content[0].split('|')
    values = content[1].split('|')


dictionary = dict(zip(keys, values))

for i in keys:
    print (i)
    fout.write(i+'|')
for i in keys:
    try:
        print (i.split('_')[1])
        fout.write(i.split('_')[1]+'|')
    except:
        fout.write('|')
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
findict['As_Technique']
findict
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
lk
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
lk
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
lk
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
lk.get('Au')
lk.get('As')
lk.get('As')[1]
lk.get('As')[0]
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
lk.get('As')[0]
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
lk
dictionary
lk =  dict()
for i in ['Au','As','Ag','Bi','Mo','Cu','Pb','Zn']:
    lk[str(i)] = (dictionary.get(str(i)+'_Technique'),dictionary.get(str(i)+'_Det_Lim_(ppm)'),dictionary.get(str(i)+'_Det_Lim_(ppb)'))
lk
for i in keys:
    fout.write(i+'|')

fout.write('\n') 

for i in keys:
    try:
        fout.write(i.split('_')[1])
    except:
        pass
    fout.write('|')

fout.write('\n')

for i in keys:
    try:
        fout.write(lk.get(str(i[:2]))[1])
    except:
        pass
    fout.write('|')

fout.write('\n')

for i in keys:
    try:
        fout.write(lk.get(str(i[:2]))[0])
    except:
        pass
    fout.write('|')    

fout.write('\n')

fout.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
lk
dictionary
lk['Au']
lk['Au'][0]
lk
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
f
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
fout.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
import date
import time
time
time.date()
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
type(df['Assay_dates']

type(df['Assay_dates'])
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
df['Assay_Date']
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
samplecodes = input()
samplecodes
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for i in techniques:
        try:
            H0800_Assay_code.append(df.i.uniques())
        except:
            pass
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for i in techniques:
        try:
            H0800_Assay_code.append(df.i.uniques())
        except:
            pass
    
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
fout.close()
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for j in techniques:
        try:
            H0800_Assay_code.append(df.j.uniques())
        except:
            pass
    print (H0800_Assay_code)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for j in techniques:
        print (j)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for j in techniques:
        print (j)
        try:
            H0800_Assay_code.append(df.j.unique())
        except:
            pass
    print (H0800_Assay_code)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for j in techniques:
        print (j)
        try:
            H0800_Assay_code.append(df[str(j)].unique())
        except:
            pass
    print (H0800_Assay_code)
fout.close()
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for j in techniques:
        print (j)
        try:
            H0800_Assay_code.append(df[str(j)].unique())
        except:
            pass
    print (H0800_Assay_code)
fout.close()

runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
fout.close()


from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for j in techniques:
        print (j)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for j in techniques:
        print (j)
        try:
            k = H0800_Assay_code.append(df[str(j)].unique())
            print (k)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for j in techniques:
        print (j)
        try:
            k = H0800_Assay_code.append(df[str(j)].unique())
            print (k)
        except:
            pass
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for j in techniques:
        print (j)
        try:
            H0800_Assay_code.append(df[str(j)].unique())
            print (H0800_Assay_code)
        except:
            pass
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = ()
    for j in techniques:
        print (j)
        try:
            H0800_Assay_code.append(df[str(j)].unique())
            print (H0800_Assay_code)
        except:
            pass
    print (H0800_Assay_code)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for j in techniques:
        print (j)
        try:
            H0800_Assay_code.add(df[str(j)].unique())
            print (H0800_Assay_code)
        except:
            pass
    print (H0800_Assay_code)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    for j in techniques:
        #print (j)
        try:
            print (df[str(j)].unique())
            H0800_Assay_code.add(df[str(j)].unique())
            #print (H0800_Assay_code)
        except:
            pass
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    H0800_Assay_codes = set()
    for j in techniques:
        #print (j)
        try:
            #print (df[str(j)].unique())
            H0800_Assay_code.add(df[str(j)].unique())
            for l in H0800_Assay_code:
                H0800_Assay_codes.add(l)
            #print (H0800_Assay_code)
        except:
            pass
    print (H0800_Assay_codes)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    H0800_Assay_codes = set()
    for j in techniques:
        #print (j)
        try:
            print (df[str(j)].unique())
            H0800_Assay_code.add(df[str(j)].unique())
            for l in H0800_Assay_code:
                H0800_Assay_codes.add(l)
            #print (H0800_Assay_code)
        except:
            pass
    print (H0800_Assay_codes)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    H0800_Assay_codes = set()
    for j in techniques:
        #print (j)
        try:
            ass =  str(df[str(j)].unique())
            H0800_Assay_code.add(df[str(j)].unique())
            for l in H0800_Assay_code:
                H0800_Assay_codes.add(l)
            #print (H0800_Assay_code)
        except:
            pass
    print (ass)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    H0800_Assay_codes = set()
    for j in techniques:
        #print (j)
        try:
            ass =  df[str(j)].unique()
            #H0800_Assay_code.add(df[str(j)].unique())
            for l in ass:
                H0800_Assay_codes.add(l)
            #print (H0800_Assay_code)
        except:
            pass
    print (ass)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    H0800_Assay_codes = set()
    for j in techniques:
        ass =  df[str(j)].unique()
        #H0800_Assay_code.add(df[str(j)].unique())
        for l in ass:
            H0800_Assay_codes.add(l)
            #print (H0800_Assay_code)
    print (ass)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    H0800_Assay_codes = set()
    for j in techniques:
        ass =  df[str(j)].unique()
        print (ass)
        #H0800_Assay_code.add(df[str(j)].unique())
        for l in ass:
            H0800_Assay_codes.add(l)
            #print (H0800_Assay_code)
    #print (ass)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    #print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    H0800_Assay_codes = set()
    for j in techniques:
        ass =  df[str(j)].unique()
        print (ass)
        #H0800_Assay_code.add(df[str(j)].unique())
        for l in ass:
            print (l)
            H0800_Assay_codes.add(l)
            #print (H0800_Assay_code)
    #print (ass)
from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break


for i in f:
    #print (i)
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i)+"_HEADERS.csv",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    H0800_Assay_codes = set()
    for j in techniques:
        ass =  df[str(j)].unique()
        #print (ass)
        #H0800_Assay_code.add(df[str(j)].unique())
        for l in ass:
            print (l)
            H0800_Assay_codes.add(l)
            print (H0800_Assay_codes)
            #print (H0800_Assay_code)
    #print (ass)
fout.close()

runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
fout.close()

runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
fout.close()

runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
fout.close()

runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
fout.close()

runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/datasorter_step_two2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/walk_os.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/coordinateconvert.py', wdir='C:/Users/gatesk/.spyder-py3')
fout.close()

runfile('C:/Users/gatesk/.spyder-py3/coordinateconvert.py', wdir='C:/Users/gatesk/.spyder-py3')
colin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\collars_coordinates_transform_latlong_subset.csv",'r')

'''
RPT_ID|HOLEID|FILE_ID|PROJECT|SITE_ID|EASTLON|NRTHLAT|ZONE|COORDSYS|TOTDEPTH|DRILLCODE|DIP|AZIMUTH|ELEVATION|DATE_DRILLED|UPDATED|COLOUR|LAT94|LNG94
'''

colout = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\collars_coordinates_transform_latlong_subset_converted.csv",'w')

from pyproj import Proj, transform
#EPSG:28354 138-144
#EPSG:28355 144-150
#EPSG:28356 150-156

for line in colin:
    #print (line)
    #input()
    items = line.split('|')
    try:
        lat =  (items[0].rstrip())
        long =  (items[1].rstrip())
        zone = (items[3].rstrip())
        inProj = Proj(init='epsg:4326')
        outProj = Proj(init='epsg:28354')
        #print (lat,long)
        lat = float(lat)
        long = float(long)
        zone = int(zone)
    except Exception as e:
        print (e)
        pass
    #print (lat,long)
    try:
        if zone == 54:
            outProj = Proj(init='epsg:28354')
        if zone == 55:
            outProj = Proj(init='epsg:28355')
        if zone == 56:
            outProj = Proj(init='epsg:28356')
        x2,y2 = transform(inProj,outProj,long,lat)
        colout.write(line.rstrip()+'|'+str(x2)+'|'+str(y2)+'\n')
        #print (x2,y2)
    except Exception as e:
        print (e)
        colout.write(line)
        pass
import pandas as pd

#read the collar and survey

colin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\collars_coordinates_transform_latlong_subset.csv",'r')

'''
RPT_ID|HOLEID|FILE_ID|PROJECT|SITE_ID|EASTLON|NRTHLAT|ZONE|COORDSYS|TOTDEPTH|DRILLCODE|DIP|AZIMUTH|ELEVATION|DATE_DRILLED|UPDATED|COLOUR|LAT94|LNG94
'''

colout = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\collars_coordinates_transform_latlong_subset_converted.csv",'w')

from pyproj import Proj, transform
#EPSG:28354 138-144
#EPSG:28355 144-150
#EPSG:28356 150-156

for line in colin:
    #print (line)
    #input()
    items = line.split('|')
    try:
        lat =  (items[1].rstrip())
        long =  (items[0].rstrip())
        zone = (items[3].rstrip())
        inProj = Proj(init='epsg:4326')
        outProj = Proj(init='epsg:28354')
        #print (lat,long)
        lat = float(lat)
        long = float(long)
        zone = int(zone)
    except Exception as e:
        print (e)
        pass
    #print (lat,long)
    try:
        if zone == 54:
            outProj = Proj(init='epsg:28354')
        if zone == 55:
            outProj = Proj(init='epsg:28355')
        if zone == 56:
            outProj = Proj(init='epsg:28356')
        x2,y2 = transform(inProj,outProj,long,lat)
        colout.write(line.rstrip()+'|'+str(x2)+'|'+str(y2)+'\n')
        #print (x2,y2)
    except Exception as e:
        print (e)
        colout.write(line)
        pass
    #print (x2,y2)


colout.close()
colin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\collars_coordinates_transform_latlong_subset.csv",'r')

'''
RPT_ID|HOLEID|FILE_ID|PROJECT|SITE_ID|EASTLON|NRTHLAT|ZONE|COORDSYS|TOTDEPTH|DRILLCODE|DIP|AZIMUTH|ELEVATION|DATE_DRILLED|UPDATED|COLOUR|LAT94|LNG94
'''

colout = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\collars_coordinates_transform_latlong_subset_converted.csv",'w')

from pyproj import Proj, transform
#EPSG:28354 138-144
#EPSG:28355 144-150
#EPSG:28356 150-156

for line in colin:
    #print (line)
    #input()
    items = line.split('|')
    try:
        lat =  (items[1].rstrip())
        long =  (items[0].rstrip())
        zone = (items[2].rstrip())
        inProj = Proj(init='epsg:4326')
        outProj = Proj(init='epsg:28354')
        #print (lat,long)
        lat = float(lat)
        long = float(long)
        zone = int(zone)
    except Exception as e:
        print (e)
        pass
    #print (lat,long)
    try:
        if zone == 54:
            outProj = Proj(init='epsg:28354')
        if zone == 55:
            outProj = Proj(init='epsg:28355')
        if zone == 56:
            outProj = Proj(init='epsg:28356')
        x2,y2 = transform(inProj,outProj,long,lat)
        colout.write(line.rstrip()+'|'+str(x2)+'|'+str(y2)+'\n')
        #print (x2,y2)
    except Exception as e:
        print (e)
        colout.write(line)
        pass
    #print (x2,y2)


colout.close()
runfile('C:/Users/gatesk/.spyder-py3/temp.py', wdir='C:/Users/gatesk/.spyder-py3')
colin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\collars_coordinates_transform_latlong_subset.csv",'r')

'''
RPT_ID|HOLEID|FILE_ID|PROJECT|SITE_ID|EASTLON|NRTHLAT|ZONE|COORDSYS|TOTDEPTH|DRILLCODE|DIP|AZIMUTH|ELEVATION|DATE_DRILLED|UPDATED|COLOUR|LAT94|LNG94
'''

colout = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\collars_coordinates_transform_latlong_subset_converted.csv",'w')

from pyproj import Proj, transform
#EPSG:28354 138-144
#EPSG:28355 144-150
#EPSG:28356 150-156

for line in colin:
    #print (line)
    #input()
    items = line.split('|')
    try:
        lat =  (items[1].rstrip())
        long =  (items[0].rstrip())
        zone = (items[2].rstrip())
        inProj = Proj(init='epsg:4326')
        outProj = Proj(init='epsg:28354')
        #print (lat,long)
        lat = float(lat)
        long = float(long)
        zone = int(zone)
    except Exception as e:
        print (e)
        pass
    #print (lat,long)
    try:
        if zone == 54:
            outProj = Proj(init='epsg:28354')
        if zone == 55:
            outProj = Proj(init='epsg:28355')
        if zone == 56:
            outProj = Proj(init='epsg:28356')
        x2,y2 = transform(inProj,outProj,long,lat)
        colout.write(line.rstrip()+'|'+str(x2)+'|'+str(y2)+'\n')
        #print (x2,y2)
    except Exception as e:
        print (e)
        colout.write(line)
        pass
    #print (x2,y2)


colout.close()
runfile('C:/Users/gatesk/.spyder-py3/coordinateconvert.py', wdir='C:/Users/gatesk/.spyder-py3')
colutmin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_LOC_DATA_INTERNAL_v2_utm_surveys_RL_20171108.txt",'r')
coldict = dict()

for line in colutmin:
    items = line.split(',')
    HOLEID = (items[4].rstrip())
    E = (items[32].rstrip())
    N = (items[33].rstrip())
    RL =(items[39].rstrip())
    DIP = (items[19].rstrip())
    AZI = (items[20].rstrip())
    #print (HOLEID,E,N,RL,DIP,AZI)
    coldict[HOLEID] = (E,N,RL,DIP,AZI)
coldict

colutmin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_LOC_DATA_INTERNAL_v2_utm_surveys_RL_20171108.txt",'r')
coldict = dict()

for line in colutmin:
    items = line.split('|')
    HOLEID = (items[5].rstrip())
    E = (items[32].rstrip())
    N = (items[33].rstrip())
    RL =(items[39].rstrip())
    DIP = (items[19].rstrip())
    AZI = (items[20].rstrip())
    #print (HOLEID,E,N,RL,DIP,AZI)
    coldict[HOLEID] = (E,N,RL,DIP,AZI)
colutmin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_LOC_DATA_INTERNAL_v2_utm_surveys_RL_20171108.txt",'r')
coldict = dict()

for line in colutmin:
    print (line)
runfile('C:/Users/gatesk/.spyder-py3/desurvey_interval_file.py', wdir='C:/Users/gatesk/.spyder-py3')
coldict

runfile('C:/Users/gatesk/.spyder-py3/desurvey_interval_file.py', wdir='C:/Users/gatesk/.spyder-py3')
coldict

coldict['DDHK1-2]]

coldict['DDHK1-2']

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
coldict['DDHK1-2']
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')
intout = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU_desurved.csv",'w')

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
from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')
intout = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU_desurved.csv",'w')

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
        intout.write(line.rstrip()+','+str(xn)+','+str(xn)+','+str(xn)+'\n')
    except Exception as e:
        #print (e)
        intout.write(line)
        #print ('\n')
        pass
intout.close()

from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')
intout = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU_desurved.csv",'w')

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
        #print (x,y,z)
        print (xn,yn,zn)
        #print ('\n')
        intout.write(line.rstrip()+','+str(xn)+','+str(xn)+','+str(xn)+'\n')
        input()
    except Exception as e:
        #print (e)
        intout.write(line)
        #print ('\n')
        pass
intout.close()

from math import cos, sin, pi

intin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU.csv",'r')
intout = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\ASSAY_MAX_DRILL_TRACE_SAMP_MAX_AU_desurved.csv",'w')

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
        #print (x,y,z)
        print (xn,yn,zn)
        #print ('\n')
        intout.write(line.rstrip()+','+str(xn)+','+str(xn)+','+str(xn)+'\n')
        #input()
    except Exception as e:
        #print (e)
        intout.write(line)
        #print ('\n')
        pass
intout.close()

runfile('C:/Users/gatesk/.spyder-py3/desurvey_interval_file.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/untitled8.py', wdir='C:/Users/gatesk/.spyder-py3')
fin = open("G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DiGS_GBjoin_KG_SIMPLE.csv",'r')
for line in fin:
    e = line.split('|')
    print (e[0])
runfile('C:/Users/gatesk/.spyder-py3/untitled8.py', wdir='C:/Users/gatesk/.spyder-py3')
fin.close()

runfile('C:/Users/gatesk/.spyder-py3/untitled8.py', wdir='C:/Users/gatesk/.spyder-py3')
uniques

runfile('C:/Users/gatesk/.spyder-py3/untitled8.py', wdir='C:/Users/gatesk/.spyder-py3')
uniques

runfile('C:/Users/gatesk/.spyder-py3/untitled8.py', wdir='C:/Users/gatesk/.spyder-py3')
DINS

runfile('C:/Users/gatesk/.spyder-py3/untitled8.py', wdir='C:/Users/gatesk/.spyder-py3')
foutRINS.close()

foutDINS.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled8.py', wdir='C:/Users/gatesk/.spyder-py3')
for i in RINS:
    foutRINS.write(i+'\n')

for i in DINS:
    foutDINS.write(i+'\n')
foutRINS.close()

foutDINS.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled8.py', wdir='C:/Users/gatesk/.spyder-py3')
for i in RINS:
    foutRINS.write(i+'\n')

for i in DINS:
    foutDINS.write(i+'\n')
foutDINS.close()

foutRINS.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled9.py', wdir='C:/Users/gatesk/.spyder-py3')
df

list(df)
df['MD_DOCDESC'].str.contains('Drill')
df['MD_DOCDESC_drill'] = df['MD_DOCDESC'].str.contains('Drill')
list(df)
df

df['MD_DOCDESC_drill'] = df['MD_DOCDESC'].str.contains(['Drill','RC','Reverse','Diamond'])
runfile('C:/Users/gatesk/.spyder-py3/untitled9.py', wdir='C:/Users/gatesk/.spyder-py3')
df
runfile('C:/Users/gatesk/.spyder-py3/untitled9.py', wdir='C:/Users/gatesk/.spyder-py3')
df
runfile('C:/Users/gatesk/.spyder-py3/untitled9.py', wdir='C:/Users/gatesk/.spyder-py3')
df
runfile('C:/Users/gatesk/.spyder-py3/untitled9.py', wdir='C:/Users/gatesk/.spyder-py3')
df

df.to_csv("G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DiGS_GBjoinAll.csv",sep='|')
df.to_csv("G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DiGS_GBjoinAll_flagged.csv",sep='|')
runfile('C:/Users/gatesk/.spyder-py3/desurvey_interval_file.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/untitled9.py', wdir='C:/Users/gatesk/.spyder-py3')
df.sort(columns ='SITE_ID')
df.sort_values(by=['SITE_ID'])
df = df.sort_values(by=['SITE_ID'])
df[0:10000].to_csv(r"C:\Users\gatesk\Documents\DiGS_GBjoinAll_flagged.csv",sep='|')
df['sum_true'] = (df[['MR_SUBJECT_drill','AB_ABSTRACT_drill','MD_DOCDESC_drill']] == 'TRUE').sum(axis=1)
df['sum_true'] = (df[['MR_SUBJECT_drill','AB_ABSTRACT_drill','MD_DOCDESC_drill']] == TRUE).sum(axis=1)
df['sum_true'] = (df[['MR_SUBJECT_drill','AB_ABSTRACT_drill','MD_DOCDESC_drill']] = 'TRUE').sum(axis=1)
df['sum_true'] = (df[['MR_SUBJECT_drill','AB_ABSTRACT_drill','MD_DOCDESC_drill']]).sum(axis=1)
df

list(df)
summary = df.groupby(['SITE_ID','RPTNAME','DIGS_RIN'], as_index=False)['sum_true'].sum()
summary

summary.to_csv(r"C:\Users\gatesk\Documents\summary.csv",sep=',')
summary.to_csv(r"C:\Users\gatesk\Documents\summary.csv",sep=',',index=False)

## ---(Thu Nov  9 13:23:21 2017)---
runfile('C:/Users/gatesk/.spyder-py3/untitled0.py', wdir='C:/Users/gatesk/.spyder-py3')
df
list(df)
dfas = df['DRILLCODE',
 'RPT_ID',
 'ASSAY_FILE_ID',
 'HOLEID',
 'SAMPLEID',
 'SAMPCODE',
 'TOPP',
 'BASE',
 'Ag_ppm+Max*(CONV_RESULT)']
dfas = df[['DRILLCODE',
 'RPT_ID',
 'ASSAY_FILE_ID',
 'HOLEID',
 'SAMPLEID',
 'SAMPCODE',
 'TOPP',
 'BASE',
 'Ag_ppm+Max*(CONV_RESULT)']]
list(dfas)
list(df)
dfas.to_csv(r"C:\Users\gatesk\Documents\sdfas.csv",sep=',',index=False)
runfile('C:/Users/gatesk/.spyder-py3/desurvey_interval_file.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/untitled4.py', wdir='C:/Users/gatesk/.spyder-py3')
df
runfile('C:/Users/gatesk/.spyder-py3/untitled4.py', wdir='C:/Users/gatesk/.spyder-py3')
list(survey)
runfile('C:/Users/gatesk/.spyder-py3/untitled4.py', wdir='C:/Users/gatesk/.spyder-py3')
list(survey)
list(collar)
runfile('C:/Users/gatesk/.spyder-py3/untitled4.py', wdir='C:/Users/gatesk/.spyder-py3')
list(collar)
list(survey)
surveyholes = np.unique(survey[['RPT_ID','HOLEID']].values)
runfile('C:/Users/gatesk/.spyder-py3/untitled4.py', wdir='C:/Users/gatesk/.spyder-py3')
surveyholes
surveyholes = survey.groupby(['RPT_ID','HOLEID'])
surveyholes
surveyholes = survey.groupby(['RPT_ID','HOLEID'], as_index=False)
surveyholes
for i in surveyholes:
    print (i)
for i, g in  survey.groupby(['RPT_ID','HOLEID'], as_index=False):
    print (i)
runfile('C:/Users/gatesk/.spyder-py3/untitled4.py', wdir='C:/Users/gatesk/.spyder-py3')
colnosur = collar_rpt_holes - surveys_rpt_holes
surnocol = surveys_rpt_holes - collar_rpt_holes
colnosur
len(colnosur)
len(surnocol)
result = pd.concat([survey, collar], axis=1)
result
collar
survey
result
collar
survey
result = pd.concat([survey, collar], axis=1, join='outer')
result
result.to_csv(r'C:\Users\gatesk\Documents\missing_surveys\\collarsurvey.csv',sep='|')
result = survey.merge(collar[['RPT_ID','HOLEID']],how='left').fillna("")
result.to_csv(r'C:\Users\gatesk\Documents\missing_surveys\\collarsurvey.csv',sep='|')
merged = pd.merge(survey, collar, how='left', on=['RPT_ID','HOLEID'])
merged.to_csv(r'C:\Users\gatesk\Documents\missing_surveys\\collarsurvey.csv',sep='|')
merged = pd.merge(survey, collar, how='outer', on=['RPT_ID','HOLEID'])
merged.to_csv(r'C:\Users\gatesk\Documents\missing_surveys\\collarsurvey.csv',sep='|')

## ---(Fri Nov 10 10:54:31 2017)---
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
absoluteFilePaths(r"C:\Users\gatesk\Documents\missing_surveys")
runfile('C:/Users/gatesk/.spyder-py3/untitled2.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/search_for_surveys_within_the_DIGS_metadata.py', wdir='C:/Users/gatesk/.spyder-py3')
df
df.sort_values(['SITE_ID'])
df = df.sort_values(['SITE_ID'])
SITEIDS = []
SITEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in SITEIDSin:
    line = str(int(line))
    line = line.lstrip('0') or '0'
    SITEIDS.append(line.rstrip())


dfsurveys =  df[df['SITE_ID'].isin(SITEIDS)]

df.to_csv(r"C:\Users\gatesk\Documents\DiGS_GBjoinAll_flagged_surveys.csv",sep='|')
'''get the list of holes'''    
SITEIDS = []
SITEIDSin = open(r"C:\Users\gatesk\Documents\missing_\SITE_LIST.txt")
for line in SITEIDSin:
    line = str(int(line))
    line = line.lstrip('0') or '0'
    SITEIDS.append(line.rstrip())


dfsurveys =  df[df['SITE_ID'].isin(SITEIDS)]

df.to_csv(r"C:\Users\gatesk\Documents\DiGS_GBjoinAll_flagged_surveys.csv",sep='|')
dfsurveys.to_csv(r"C:\Users\gatesk\Documents\DiGS_GBjoinAll_flagged_surveys.csv",sep='|')
runfile('C:/Users/gatesk/.spyder-py3/untitled17.py', wdir='C:/Users/gatesk/.spyder-py3')
a = 'abc'
b = ['abc','df','dgdg']
a in b
if a in b:
    print ('y')
runfile('C:/Users/gatesk/.spyder-py3/untitled17.py', wdir='C:/Users/gatesk/.spyder-py3')
getlines.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled17.py', wdir='C:/Users/gatesk/.spyder-py3')
import os
import re

getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
searchdir = 'X:\\'

'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'w')

'''get the lines from survey files'''
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))


for i in absoluteFilePaths(searchdir):
    if 'urv' in str(i):
        with open(i) as f:
            for line in f:
                surveyfilemerge.write(line)

surveyfilemerge.close()
import os
import re

getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
searchdir = 'X:\\'

'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'w')

'''get the lines from survey files'''
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))


for i in absoluteFilePaths(searchdir):
    try:
        if 'urv' in str(i):
            with open(i) as f:
                for line in f:
                    surveyfilemerge.write(line)
    except:
        pass

surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for fn in HOLEIDS:
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for fn in HOLEIDS:
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled17.py', wdir='C:/Users/gatesk/.spyder-py3')
import pandas as pd
df = pd.read_csv(r"G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\Archive\UpdateRINS_GS_REPORT\DiGS_GBjoinAll.csv",sep='|')

df['MR_SUBJECT_drill'] = df['MR_SUBJECT'].str.contains('svy|survey|SVY|Survey|surv|Surv|surveys|Surveys|SURVEY|SURVEYS|SURV')
df['AB_ABSTRACT_drill'] = df['AB_ABSTRACT'].str.contains('svy|survey|SVY|Survey|surv|Surv|surveys|Surveys|SURVEY|SURVEYS|SURV')
df['MD_DOCDESC_drill'] = df['MD_DOCDESC'].str.contains('svy|survey|SVY|Survey|surv|Surv|surveys|Surveys|SURVEY|SURVEYS|SURV')
df.sort_values(['SITE_ID'])

'''get the list of holes'''    
SITEIDS = []
SITEIDSin = open(r"C:\Users\gatesk\Documents\missing_\SITE_LIST.txt")
for line in SITEIDSin:
    line = str(int(line))
    line = line.lstrip('0') or '0'
    SITEIDS.append(line.rstrip())


dfsurveys =  df[df['SITE_ID'].isin(SITEIDS)]

dfsurveys.to_csv(r"C:\Users\gatesk\Documents\DiGS_GBjoinAll_flagged_surveys_all_sites.csv",sep='|')
import os
import re

getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
searchdir = 'C:\Users\gatesk\Documents\missing_\candidate_files'

'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'w')

'''get the lines from survey files'''
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))


for i in absoluteFilePaths(searchdir):
    try:
        if 'urv' in str(i):
            with open(i) as f:
                for line in f:
                    surveyfilemerge.write(line)
    except:
        pass

surveyfilemerge.close()


surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for fn in HOLEIDS:
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        #print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled17.py', wdir='C:/Users/gatesk/.spyder-py3')
import os
import re

getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
searchdir = r'C:\Users\gatesk\Documents\missing_\candidate_files'

'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'w')

'''get the lines from survey files'''
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))


for i in absoluteFilePaths(searchdir):
    try:
        if 'urv' in str(i):
            with open(i) as f:
                for line in f:
                    surveyfilemerge.write(line)
    except:
        pass

surveyfilemerge.close()


surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for fn in HOLEIDS:
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        #print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled17.py', wdir='C:/Users/gatesk/.spyder-py3')
HOLEIDS
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for fn in HOLEIDS:
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        print (lineelements)
        #print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')



for fn in HOLEIDS:
    print (fn)
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        print (lineelements)
        #print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
for line in surveyfilemerge:
    print (line)
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for fn in HOLEIDS:
    print (fn)
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        print (lineelements)
        #print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))
for line in surveyfilemerge:
    lineelements = re.split('[ \t,]',line)
lineelements
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for fn in HOLEIDS:
    print (fn)
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        print (lineelements)
        #print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
for line in surveyfilemerge:
    lineelements = re.split('[ \t,]',line)
    print (lineelements)
    #print (lineelements)
    if str(fn) in lineelements:
        print (str(fn) +' '+ str(line))
        getlines.write(line+'|'+str(fn))
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
for line in surveyfilemerge:
    lineelements = re.split('[ \t,]',line)
    print (lineelements)
    #print (lineelements)
    if str(fn) in lineelements:
        print (str(fn) +' '+ str(line))
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for fn in HOLEIDS:
    print (fn)
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))
for line in surveyfilemerge:
    lineelements = re.split('[ \t,]',line)
    print (lineelements)
    for fn in HOLEIDS:
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for line in surveyfilemerge:
    lineelements = re.split('[ \t,]',line)
    print (lineelements)
    for fn in HOLEIDS:
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')


for fn in HOLEIDS:
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        print (lineelements)
            if str(fn) in lineelements:
                print (str(fn) +' '+ str(line))
                getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')


for fn in HOLEIDS:
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
getlines.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')


for fn in HOLEIDS:
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
for fn in HOLEIDS:
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        #print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line)


getlines.close()
surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')


for fn in HOLEIDS:
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        #print (lineelements)
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line)


getlines.close()
surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for fn in HOLEIDS:
    for line in surveyfilemerge:
        lineelements = re.split('[ \t,]',line)
        #print (lineelements)
        if fn in lineelements:
            print (fn +' '+ str(line))
            getlines.write(line)


getlines.close()
surveyfilemerge.close()
HOLEIDS
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for fn in HOLEIDS:
    for line in surveyfilemerge:
        if fn in line:
            print (fn +' '+ str(line))
            getlines.write(line)
        #lineelements = re.split('[ \t,]',line)
        #print (lineelements)

#        if fn in lineelements:
#            print (fn +' '+ str(line))
#            getlines.write(line)

getlines.close()
surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for fn in HOLEIDS:
    for line in surveyfilemerge:
        print (line)
        if fn in line:
            print (fn +' '+ str(line))
            getlines.write(line)
        #lineelements = re.split('[ \t,]',line)
        #print (lineelements)

#        if fn in lineelements:
#            print (fn +' '+ str(line))
#            getlines.write(line)

getlines.close()
surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for line in surveyfilemerge:
    lineelements = re.split('[ \t,]',line)
    print (lineelements)
    for fn in HOLEIDS:
        if str(fn) in lineelements:
            print (str(fn) +' '+ str(line))
            getlines.write(line+'|'+str(fn))


getlines.close()
surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for line in surveyfilemerge:
    lineelements = re.split('[ \t,]',line)
    print (lineelements)
    for fn in HOLEIDS:
        if str(fn) in lineelements:
            #print (str(fn) +' '+ str(line))
            getlines.write(line)


getlines.close()
surveyfilemerge.close()
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
lines = set()

for line in surveyfilemerge:
    lineelements = re.split('[ \t,]',line)
    print (lineelements)
    for fn in HOLEIDS:
        if str(fn) in lineelements:
            #print (str(fn) +' '+ str(line))
            lines.add(line)


for i in lines:
    getlines.write(str(i))


getlines.close()
surveyfilemerge.close()
import os, json, zipfile, shutil, magic

local_mountpoint = "R:\\"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"

'''get the RIN LIST'''
RINS = []
RINSin = open(r"C:\Users\gatesk\Documents\missing_\RIN_LIST.txt",'r')
for line in RINSin:
    RINS.append(line.rstrip())


'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

'''GRAB THE RINS'''
#with open("cobar_rins_list_conf_2017-04-19.json") as fp:
#    solr_result = json.load(fp)
#    cobar_docs = solr_result['response']['docs']
#    print("Loaded cobar search:", len(cobar_docs))
#
#cobar_rins = set()
#for d in cobar_docs:
#    cobar_rins.add(d['mr_rin'])

for rin in RINS:
    rin_path = "%s/%s/%s" % (rin[0:3], rin[3:6], rin[6:9])
    #din_file_path = os.path.join(local_mountpoint, rin_path)
    rin_folder_path = os.path.join(local_mountpoint, rin_path)
    #print(rin_folder_path)
    assert os.path.exists(rin_folder_path)
    assert os.path.isdir(rin_folder_path)


#    if not os.path.exists(base_folder):
#        os.mkdir(base_folder)
#    else:
#        print("output folder %s exists already." % out_folder)
    
    out_folder = os.path.join(base_folder, rin)
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    else:
        print("output folder %s exists already." % out_folder)
    
    rin_files = os.listdir(rin_folder_path)
    print(len(rin_files))
    for f in rin_files:
        outfile = os.path.join(out_folder, f)
        infile = os.path.join(rin_folder_path, f)
        if not os.path.exists(outfile):
            print("Copying %s" % outfile)
            shutil.copy(infile, outfile)
        else:
            print("File %s exists already." % outfile)
import os, zipfile, shutil #magic

local_mountpoint = "R:\\"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"

'''get the RIN LIST'''
RINS = []
RINSin = open(r"C:\Users\gatesk\Documents\missing_\RIN_LIST.txt",'r')
for line in RINSin:
    RINS.append(line.rstrip())


'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

'''GRAB THE RINS'''
#with open("cobar_rins_list_conf_2017-04-19.json") as fp:
#    solr_result = json.load(fp)
#    cobar_docs = solr_result['response']['docs']
#    print("Loaded cobar search:", len(cobar_docs))
#
#cobar_rins = set()
#for d in cobar_docs:
#    cobar_rins.add(d['mr_rin'])

for rin in RINS:
    rin_path = "%s/%s/%s" % (rin[0:3], rin[3:6], rin[6:9])
    #din_file_path = os.path.join(local_mountpoint, rin_path)
    rin_folder_path = os.path.join(local_mountpoint, rin_path)
    #print(rin_folder_path)
    assert os.path.exists(rin_folder_path)
    assert os.path.isdir(rin_folder_path)


#    if not os.path.exists(base_folder):
#        os.mkdir(base_folder)
#    else:
#        print("output folder %s exists already." % out_folder)
    
    out_folder = os.path.join(base_folder, rin)
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    else:
        print("output folder %s exists already." % out_folder)
    
    rin_files = os.listdir(rin_folder_path)
    print(len(rin_files))
    for f in rin_files:
        outfile = os.path.join(out_folder, f)
        infile = os.path.join(rin_folder_path, f)
        if not os.path.exists(outfile):
            print("Copying %s" % outfile)
            shutil.copy(infile, outfile)
        else:
            print("File %s exists already." % outfile)
import magic
import libmagic
import os, zipfile, shutil #magic

local_mountpoint = "R:\\"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"

'''get the RIN LIST'''
RINS = []
RINSin = open(r"C:\Users\gatesk\Documents\missing_\RIN_LIST.txt",'r')
for line in RINSin:
    RINS.append(line.rstrip())


'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

'''GRAB THE RINS'''
#with open("cobar_rins_list_conf_2017-04-19.json") as fp:
#    solr_result = json.load(fp)
#    cobar_docs = solr_result['response']['docs']
#    print("Loaded cobar search:", len(cobar_docs))
#
#cobar_rins = set()
#for d in cobar_docs:
#    cobar_rins.add(d['mr_rin'])

for rin in RINS:
    rin_path = "%s/%s/%s" % (rin[0:3], rin[3:6], rin[6:9])
    #din_file_path = os.path.join(local_mountpoint, rin_path)
    rin_folder_path = os.path.join(local_mountpoint, rin_path)
    #print(rin_folder_path)
    assert os.path.exists(rin_folder_path)
    assert os.path.isdir(rin_folder_path)


#    if not os.path.exists(base_folder):
#        os.mkdir(base_folder)
#    else:
#        print("output folder %s exists already." % out_folder)
    
    out_folder = os.path.join(base_folder, rin)
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    else:
        print("output folder %s exists already." % out_folder)
    
    rin_files = os.listdir(rin_folder_path)
    print(len(rin_files))
    for f in rin_files:
        outfile = os.path.join(out_folder, f)
        infile = os.path.join(rin_folder_path, f)
        if not os.path.exists(outfile):
            print("Copying %s" % outfile)
            shutil.copy(infile, outfile)
        else:
            print("File %s exists already." % outfile)


rin_folders = os.listdir(base_folder)

import filetype

def fixfile(path):
    kind = filetype.guess(path)
    if kind is None:
        print('Cannot guess file type!')
        return
    newpath = path + "." + kind.extension
    shutil.rename(path,newpath)


for r in rin_folders:
    rf = os.path.join(base_folder, r)
    if os.path.isdir(rf):
        rin_files = os.listdir(rf)
        print("%s %s" % (r, len(rin_files)))
        for f in rin_files:
            ext = os.path.splitext(f)[1]
            print(ext)
            f_path = os.path.join(rf, f)
            if ext == '.file':
                fixfile(f_path)
import os, zipfile, shutil #magic

local_mountpoint = "R:\\"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"

'''get the RIN LIST'''
RINS = []
RINSin = open(r"C:\Users\gatesk\Documents\missing_\RIN_LIST.txt",'r')
for line in RINSin:
    RINS.append(line.rstrip())


'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

'''GRAB THE RINS'''
#with open("cobar_rins_list_conf_2017-04-19.json") as fp:
#    solr_result = json.load(fp)
#    cobar_docs = solr_result['response']['docs']
#    print("Loaded cobar search:", len(cobar_docs))
#
#cobar_rins = set()
#for d in cobar_docs:
#    cobar_rins.add(d['mr_rin'])

for rin in RINS:
    rin_path = "%s/%s/%s" % (rin[0:3], rin[3:6], rin[6:9])
    #din_file_path = os.path.join(local_mountpoint, rin_path)
    rin_folder_path = os.path.join(local_mountpoint, rin_path)
    #print(rin_folder_path)
    assert os.path.exists(rin_folder_path)
    assert os.path.isdir(rin_folder_path)


#    if not os.path.exists(base_folder):
#        os.mkdir(base_folder)
#    else:
#        print("output folder %s exists already." % out_folder)
    
    out_folder = os.path.join(base_folder, rin)
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    else:
        print("output folder %s exists already." % out_folder)
    
    rin_files = os.listdir(rin_folder_path)
    print(len(rin_files))
    for f in rin_files:
        outfile = os.path.join(out_folder, f)
        infile = os.path.join(rin_folder_path, f)
        if not os.path.exists(outfile):
            print("Copying %s" % outfile)
            shutil.copy(infile, outfile)
        else:
            print("File %s exists already." % outfile)


rin_folders = os.listdir(base_folder)

import filetype

def fixfile(path):
    kind = filetype.guess(path)
    if kind is None:
        print('Cannot guess file type!')
        return
    newpath = path + "." + kind.extension
    shutil.move(path,newpath)


for r in rin_folders:
    rf = os.path.join(base_folder, r)
    if os.path.isdir(rf):
        rin_files = os.listdir(rf)
        print("%s %s" % (r, len(rin_files)))
        for f in rin_files:
            ext = os.path.splitext(f)[1]
            print(ext)
            f_path = os.path.join(rf, f)
            if ext == '.file':
                fixfile(f_path)
'''unzip the folders'''
extension = ".zip"

for r in rin_folders:
    for item in os.listdir(r): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(r) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
'''unzip the folders'''
extension = ".zip"

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(rf) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
'''unzip the folders'''
extension = ".zip"

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    print (rf)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(rf) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
basefolder
base_folder
'''unzip the folders'''
extension = ".zip"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    print (rf)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(rf) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
'''unzip the folders'''
extension = ".zip"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    print (rf)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            print (filename)
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(rf) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
'''unzip the folders'''
extension = ".zip"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    print (rf)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            print (file_name)
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(rf) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
'''unzip the folders'''
extension = ".zip"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    print (rf)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.join(rf,item) # get full path of files
            print (file_name)
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(rf) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
import os, zipfile, shutil #magic

local_mountpoint = "R:\\"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"

'''get the RIN LIST'''
RINS = []
RINSin = open(r"C:\Users\gatesk\Documents\missing_\RIN_LIST.txt",'r')
for line in RINSin:
    RINS.append(line.rstrip())


'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

'''GRAB THE RINS'''
#with open("cobar_rins_list_conf_2017-04-19.json") as fp:
#    solr_result = json.load(fp)
#    cobar_docs = solr_result['response']['docs']
#    print("Loaded cobar search:", len(cobar_docs))
#
#cobar_rins = set()
#for d in cobar_docs:
#    cobar_rins.add(d['mr_rin'])

for rin in RINS:
    rin_path = "%s/%s/%s" % (rin[0:3], rin[3:6], rin[6:9])
    #din_file_path = os.path.join(local_mountpoint, rin_path)
    rin_folder_path = os.path.join(local_mountpoint, rin_path)
    #print(rin_folder_path)
    assert os.path.exists(rin_folder_path)
    assert os.path.isdir(rin_folder_path)


#    if not os.path.exists(base_folder):
#        os.mkdir(base_folder)
#    else:
#        print("output folder %s exists already." % out_folder)
    
    out_folder = os.path.join(base_folder, rin)
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    else:
        print("output folder %s exists already." % out_folder)
    
    rin_files = os.listdir(rin_folder_path)
    print(len(rin_files))
    for f in rin_files:
        outfile = os.path.join(out_folder, f)
        infile = os.path.join(rin_folder_path, f)
        if not os.path.exists(outfile):
            print("Copying %s" % outfile)
            shutil.copy(infile, outfile)
        else:
            print("File %s exists already." % outfile)


rin_folders = os.listdir(base_folder)

import filetype

def fixfile(path):
    kind = filetype.guess(path)
    if kind is None:
        print('Cannot guess file type!')
        return
    newpath = path + "." + kind.extension
    shutil.move(path,newpath)


for r in rin_folders:
    rf = os.path.join(base_folder, r)
    if os.path.isdir(rf):
        rin_files = os.listdir(rf)
        print("%s %s" % (r, len(rin_files)))
        for f in rin_files:
            ext = os.path.splitext(f)[1]
            print(ext)
            f_path = os.path.join(rf, f)
            if ext == '.file':
                fixfile(f_path)



'''unzip the folders'''
extension = ".zip"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    print (rf)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.join(rf,item) # get full path of files
            print (file_name)
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(rf) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
runfile('C:/Users/gatesk/.spyder-py3/untitled19.py', wdir='C:/Users/gatesk/.spyder-py3')
from winmagic import magic

## ---(Mon Nov 13 08:04:25 2017)---
from winmagic import magic
runfile('C:/Users/gatesk/.spyder-py3/untitled19.py', wdir='C:/Users/gatesk/.spyder-py3')
magic.detect_from_filename("C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029712\R00029712.D005078810.D.file")
magic.detect_from_filename(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029712\R00029712.D005078810.D.file")
magic.from_file(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029712\R00029712.D005078810.D.file")
magic.from_file(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029712\R00029712.D005078810.D.file",mime=True)
runfile('C:/Users/gatesk/.spyder-py3/untitled19.py', wdir='C:/Users/gatesk/.spyder-py3')
magic.from_file(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029712\R00029712.D005078810.D.file",mime=True)
fix_a_file(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029712\R00029712.D005078810.D.file")
fix_a_file(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029712\R00029712.D005078820.D.file")
fix_a_file(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029712\R00029712.D005078830.D.file")
runfile('C:/Users/gatesk/.spyder-py3/untitled5.py', wdir='C:/Users/gatesk/.spyder-py3')
from winmagic import magic
import os

base_folder = r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029712"
rin_folders = os.listdir(base_folder)

file_exts = {
    "application/zip": "zip",
    "application/pdf": "pdf",
    "image/jpeg": "jpeg",
    "image/tiff": "tiff",
    "text/plain": "txt",
    "text/x-fortran": "f",
    "application/octet-stream": "bin"
}


def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))


def fixfile(file_path: str):
    detected = magic.from_file(file_path,mime=True)
    if detected in file_exts:
        print("%s -> %s" % (detected, file_exts[detected]))
        os.rename(file_path, file_path + "." + file_exts[detected])
    else:
        print("%s not found?" % (detected))
        assert False


for i in absoluteFilePaths(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029712"):
    try:
        fixfile(i)
    except:
        pass
runfile('C:/Users/gatesk/.spyder-py3/untitled5.py', wdir='C:/Users/gatesk/.spyder-py3')
extension = ".zip"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"
rin_folders = os.listdir(base_folder)

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    print (rf)
'''unzip the folders'''
extension = ".zip"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"
rin_folders = os.listdir(base_folder)

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    print (rf)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.join(rf,item) # get full path of files
            print (file_name)
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(rf) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
'''unzip the folders'''
import zipfile
extension = ".zip"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"
rin_folders = os.listdir(base_folder)

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    print (rf)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.join(rf,item) # get full path of files
            print (file_name)
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(rf) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
import zipfile
extension = ".zip"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"
rin_folders = os.listdir(base_folder)

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    #print (rf)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.join(rf,item) # get full path of files
            #print (file_name)
            try:
                zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                zip_ref.extractall(rf) # extract file to dir
                zip_ref.close() # close file
                os.remove(file_name) # delete zipped file
            except Exception as e:
                print (file_name)
                print (e)
                pass
runfile('C:/Users/gatesk/.spyder-py3/untitled6.py', wdir='C:/Users/gatesk/.spyder-py3')
headers
headersorted = sorted(headers)
headersorted
uniqueheaders = open("unique_headers.txt",'r')
uniqueheaders = open("unique_headers.txt",'w')
for i in sorted(headers):
    uniqueheaders.write(i+'\n')
uniqueheaders.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled6.py', wdir='C:/Users/gatesk/.spyder-py3')
uniqueheaders = open("unique_headers.txt",'w')
for i in sorted(headers):
    uniqueheaders.write(i+'\n')
uniqueheaders.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled6.py', wdir='C:/Users/gatesk/.spyder-py3')
H1000fields = open("H1000_fields.txt",'r')

for line in H1000fields:
    if line.split('\t')[1:] != '':
        print (line)
runfile('C:/Users/gatesk/.spyder-py3/untitled6.py', wdir='C:/Users/gatesk/.spyder-py3')
surveyfiles
'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())



for file in surveyfiles:
    print (file)
'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for file in surveyfiles:
    with open(i) as f:
        for line in f:
            #if 'H1000' in line:
            #    getlines.write(line)
            for hole in HOLEIDS:
                if hole in line:
                    print (line)
                    #getlines.write(line)
surveyfiles
'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for file in surveyfiles:
    try:
        with open(i) as f:
            for line in f:
                #if 'H1000' in line:
                #    getlines.write(line)
                for hole in HOLEIDS:
                    if hole in line:
                        print (line)
                        #getlines.write(line)
    except:
        pass
'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for file in surveyfiles:
    try:
        with open(file) as f:
            for line in f:
                #if 'H1000' in line:
                #    getlines.write(line)
                for hole in HOLEIDS:
                    if hole in line:
                        print (line)
                        #getlines.write(line)
    except:
        pass
'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')

for file in surveyfiles:
    try:
        with open(file) as f:
            for line in f:
                #if 'H1000' in line:
                #    getlines.write(line)
                for hole in HOLEIDS:
                    elements = re.split('[ \t,]', line)
                    if hole in elements:
                        print (line.rstrip('\n'))
                        #getlines.write(line)
    except:
        pass
surveyfiles
runfile('C:/Users/gatesk/.spyder-py3/untitled6.py', wdir='C:/Users/gatesk/.spyder-py3')
'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


surveyout = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
surveylines = set()

for file in surveyfiles:
    try:
        with open(file) as f:
            for line in f:
                #if 'H1000' in line:
                #    getlines.write(line)
                for hole in HOLEIDS:
                    elements = re.split('[ \t,]', line)
                    if hole in elements:
                        surveyline = line.rstrip('\n')
                        if surveyline not in surveylines:
                            surveylines.add(surveyline)
                            surveyout.write(file+'\t'+surveyline+'\n')
                        else:
                            pass
    
    except:
        pass
runfile('C:/Users/gatesk/.spyder-py3/untitled6.py', wdir='C:/Users/gatesk/.spyder-py3')
with open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydatamerge.txt") as f:
    for line in f:
        for hole in HOLEIDS:
            elements = re.split('[ \t,]', line)
            if hole in elements:
                surveyline = line.rstrip('\n')
                if surveyline not in surveylines:
                    surveylines.add(surveyline)
                    surveyout.write(file+'\t'+surveyline+'\n')
                else:
                    pass
HOLEIDS
'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


surveyoutmerge = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydatamerge.txt",'w')
surveyout = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
surveylines = set()

for file in surveyfiles:
    with open(file) as f:
        for line in f:
            surveyoutmerge.write(line)

surveyoutmerge.close()

print ('here')
#with open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydatamerge.txt") as f:
#    for line in f:
#        for hole in HOLEIDS:
#            elements = re.split('[ \t,]', line)
#            if hole in elements:
#                surveyline = line.rstrip('\n')
#                if surveyline not in surveylines:
#                    surveylines.add(surveyline)
#                    surveyout.write(file+'\t'+surveyline+'\n')
#                else:
#                    pass

with open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydatamerge.txt") as f:
    for line in f:
        elements = re.split('[ \t,]', line)
        for hole in HOLEIDS:
            if hole in elements:
                surveyline = line.rstrip('\n')
                #if surveyline not in surveylines:
                    #surveylines.add(surveyline)
                surveyout.write(hole+'\t'+file+'\t'+surveyline+'\n')
                #else:
                #    pass
'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


surveyoutmerge = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydatamerge.txt",'w')
surveyout = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
surveylines = set()

for file in surveyfiles:
    with open(file) as f:
        for line in f:
            surveyoutmerge.write(line)

surveyoutmerge.close()

print ('here')
#with open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydatamerge.txt") as f:
#    for line in f:
#        for hole in HOLEIDS:
#            elements = re.split('[ \t,]', line)
#            if hole in elements:
#                surveyline = line.rstrip('\n')
#                if surveyline not in surveylines:
#                    surveylines.add(surveyline)
#                    surveyout.write(file+'\t'+surveyline+'\n')
#                else:
#                    pass

with open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydatamerge.txt") as f:
    for idx, line in enumerate(f):
        if idx % 100 == 0:
            print (idx)
        elements = re.split('[ \t,]', line)
        for hole in HOLEIDS:
            if hole in elements:
                surveyline = line.rstrip('\n')
                #if surveyline not in surveylines:
                    #surveylines.add(surveyline)
                surveyout.write(hole+'\t'+file+'\t'+surveyline+'\n')
                #else:
                #    pass
runfile('C:/Users/gatesk/.spyder-py3/untitled6.py', wdir='C:/Users/gatesk/.spyder-py3')
'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())


surveyoutmerge = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydatamerge.txt",'w')
surveyout = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
surveylines = set()

for file in surveyfiles: 
    RIN = str(file).split('\\')[-2]
    with open(file) as f:
        for line in f:
            if line.startswith('D'):
                outline = "\t".join((RIN,file,line))
                surveyoutmerge.write(outline)

surveyoutmerge.close()

print ('here')
#with open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydatamerge.txt") as f:
#    for line in f:
#        for hole in HOLEIDS:
#            elements = re.split('[ \t,]', line)
#            if hole in elements:
#                surveyline = line.rstrip('\n')
#                if surveyline not in surveylines:
#                    surveylines.add(surveyline)
#                    surveyout.write(file+'\t'+surveyline+'\n')
#                else:
#                    pass

with open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydatamerge.txt") as f:
    for idx, line in enumerate(f):
        if idx % 100 == 0:
            print (idx)
        elements = re.split('[ \t,]', line)
        for hole in HOLEIDS:
            if hole in elements:
                surveyline = line.rstrip('\n')
                #if surveyline not in surveylines:
                    #surveylines.add(surveyline)
                surveyout.write(hole+'\t'+file+'\t'+surveyline+'\n')
                #else:
                #    pass
runfile('C:/Users/gatesk/.spyder-py3/untitled6.py', wdir='C:/Users/gatesk/.spyder-py3')
surveyout.close()
runfile('C:/Users/gatesk/.spyder-py3/untitled6.py', wdir='C:/Users/gatesk/.spyder-py3')
surveyout.close()
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
rinholes['RC008']
rinholes['JR15']
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
foundsurveys
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
df
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
df
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
merged
df
'BHID' in df
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
list(df)
df = df.sort_values(by=['BHID','DEPTH'])
df
list(df)
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
df
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
df
df.to_csv('text_out.csv',sep='|')
merged
merged.to_csv('text_out.csv',sep='|')
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
master
list(merged)
merged
merged = merged.sort_values(by=['BHID','DEPTH'])
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
merged = merged.sort_values(by=['BHID','DEPTH'])
list(merged)
merged
merged.to_csv('merged_out.csv',sep='|')
merged.to_csv('merged_out.csv',sep='|',index=False)
'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())
len(HOLEIDS)
rinholes = defaultdict(list)
root = r'C:/Users/gatesk/Documents/missing_/RINS_SEARCH'

with open(r"C:/Users/gatesk/Documents/missing_/RIN_HOLES_MASTER.csv") as master:
    rdr = csv.reader(master, delimiter='|')
    for line in rdr:
        #print (line)
        rin = line[2]
        hole = line[5]
        rinholes[hole].append(rin)


all_rins = set()
all_rins
rinholes
rinholes['OT1']
import csv, os
from collections import defaultdict
from H1000_survey_lk import surveyheaders, surveyheaders2
import re
import pandas as pd

rinholes = defaultdict(list)
root = r'C:/Users/gatesk/Documents/missing_/RINS_SEARCH'

with open(r"C:/Users/gatesk/Documents/missing_/RIN_HOLES_MASTER.csv") as master:
    rdr = csv.reader(master, delimiter='|')
    for line in rdr:
        #print (line)
        rin = line[2]
        hole = line[5]
        rinholes[hole].append(rin)


all_rins = set()

for hole,rins in rinholes.items():
    for rin in rins:
        all_rins.add(rin)


rinfiles = defaultdict(list)

def findsurveys(fold):
    def absoluteFilePaths(directory):
       for dirpath,_,filenames in os.walk(directory):
           for f in filenames:
               yield os.path.abspath(os.path.join(dirpath, f))
    
    def is_a_survey(headerline):
        elements = re.split('[ \t,]', headerline)
        #if headers suggests it is a survey file
        for e in elements:
           if e in  surveyheaders:
               return True
    
    
    def isH1000(fin):
        with open(fin) as f:
            for idx, line in enumerate(f):
                if idx > 100:
                    break
                if line.startswith('H1000'):
                    return idx,line
                if line.startswith('"H1000'):
                    return idx,line
            return -1, None
    
    surveyfiles = []
    
    for f in absoluteFilePaths(fold):
        ext = os.path.splitext(f)[1]
        if ext not in ['.txt']:
            continue
        idx, line = isH1000(f)
        if idx != -1:
            if is_a_survey(line):
                surveyfiles.append([f,idx,line,None])
    
    return surveyfiles


surveyfiles_by_rin = defaultdict(list)

for rin in all_rins:
    rinfolder = os.path.join(root,rin)
    #print (rinfolder)
    foundsurveys = findsurveys(rinfolder)
    #print (rin,len(foundsurveys))
    #print (rin,foundsurveys)
    surveyfiles_by_rin[rin] = foundsurveys
surveyfiles_by_rin
surveyfiles_by_rin['R00054921']
'''cleanup the headers to dict mappings for survey files'''
for rin,surveys in  surveyfiles_by_rin.items():
    #print (rin,len(surveys))
    for s in surveys:
        f = s[0]
        idx = s[1]
        line = s[2]
        elements = re.split('[ \t,]', line.strip())
        #print (elements)
        newheader = []
        for e in elements:
            if e in surveyheaders:
                realheader = surveyheaders[e]
                newheader.append(realheader)
            elif e in surveyheaders2:
                realheader = surveyheaders2[e]
                newheader.append(realheader)
            else:
                newheader.append(e)
        s[3] = newheader
surveyfiles_by_rin['R00054921']
survey_dfs = dict()

for rin,surveys in  surveyfiles_by_rin.items():
    for s in surveys:
        f = s[0]
        idx = s[1]
        line = s[2]
        newheaders = s[3]
        #print (rin,f)
        #assert "BHID" in newheaders
        #assert "DEPTH" in newheaders
        if "BHID" not in newheaders:
            #print ("rejecting file - no BHID: ", newheaders)
            continue
        if "DIP" not in newheaders:
            print ("rejecting file - no DIP: ", newheaders)
            continue
        #print (idx)
        try:
            df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
            #df = pd.read_csv()
            #print (df)
        except Exception as e:
            print (e)
            pass
        survey_dfs[f] = df
for rin,surveys in  surveyfiles_by_rin['R00054921']:
    for s in surveys:
        f = s[0]
        idx = s[1]
        line = s[2]
        newheaders = s[3]
        #print (rin,f)
        #assert "BHID" in newheaders
        #assert "DEPTH" in newheaders
        if "BHID" not in newheaders:
            #print ("rejecting file - no BHID: ", newheaders)
            continue
        if "DIP" not in newheaders:
            print ("rejecting file - no DIP: ", newheaders)
            continue
        #print (idx)
        try:
            df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
            #df = pd.read_csv()
            #print (df)
        except Exception as e:
            print (e)
            pass
        survey_dfs[f] = df
for rin,surveys in  surveyfiles_by_rin.items():
    for s in surveys:
        print (s)
        f = s[0]
        idx = s[1]
        line = s[2]
        newheaders = s[3]
        #print (rin,f)
        #assert "BHID" in newheaders
        #assert "DEPTH" in newheaders
        if "BHID" not in newheaders:
            #print ("rejecting file - no BHID: ", newheaders)
            continue
        if "DIP" not in newheaders:
            print ("rejecting file - no DIP: ", newheaders)
            continue
        #print (idx)
        try:
            df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
            #df = pd.read_csv()
            #print (df)
        except Exception as e:
            print (e)
            pass
        survey_dfs[f] = df
for rin,surveys in  surveyfiles_by_rin.items():
    for s in surveys:
        f = s[0]
        idx = s[1]
        line = s[2]
        newheaders = s[3]
        #print (rin,f)
        #assert "BHID" in newheaders
        #assert "DEPTH" in newheaders
        if f == 'C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00054921\\EL6321_200611_08_appendix.txt':
            if "BHID" not in newheaders:
                #print ("rejecting file - no BHID: ", newheaders)
                continue
            if "DIP" not in newheaders:
                print ("rejecting file - no DIP: ", newheaders)
                continue
            #print (idx)
            try:
                df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
                #df = pd.read_csv()
                #print (df)
            except Exception as e:
                print (e)
                pass
            survey_dfs[f] = df
surveyfiles_by_rin['R00029437']
for rin,surveys in  surveyfiles_by_rin.items():
    for s in surveys:
        f = s[0]
        idx = s[1]
        line = s[2]
        newheaders = s[3]
        #print (rin,f)
        #assert "BHID" in newheaders
        #assert "DEPTH" in newheaders
        if f == 'C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00029437\\R00029437.D005062820.D.file.txt':
            if "BHID" not in newheaders:
                #print ("rejecting file - no BHID: ", newheaders)
                continue
            if "DIP" not in newheaders:
                print ("rejecting file - no DIP: ", newheaders)
                continue
            #print (idx)
            try:
                df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
                #df = pd.read_csv()
                #print (df)
            except Exception as e:
                print (e)
                pass
            survey_dfs[f] = df
df
def checkfile_by_path(path):
    for rin,surveys in  surveyfiles_by_rin.items():
        for s in surveys:
            f = s[0]
            idx = s[1]
            line = s[2]
            newheaders = s[3]
            #print (rin,f)
            #assert "BHID" in newheaders
            #assert "DEPTH" in newheaders
            if f == path:
                if "BHID" not in newheaders:
                    #print ("rejecting file - no BHID: ", newheaders)
                    continue
                if "DIP" not in newheaders:
                    print ("rejecting file - no DIP: ", newheaders)
                    continue
                #print (idx)
                try:
                    df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
                    #df = pd.read_csv()
                    #print (df)
                except Exception as e:
                    print (e)
                    pass
                survey_dfs[f] = df
checkfile_by_path(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029437\R00029437.D005062820.D.file.txt")
checkfile_by_path('C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00029437\\R00029437.D005062820.D.file.txt')
def checkfile_by_path(path):
    for rin,surveys in  surveyfiles_by_rin.items():
        for s in surveys:
            f = s[0]
            idx = s[1]
            line = s[2]
            newheaders = s[3]
            #print (rin,f)
            #assert "BHID" in newheaders
            #assert "DEPTH" in newheaders
            if f == path:
                if "BHID" not in newheaders:
                    #print ("rejecting file - no BHID: ", newheaders)
                    continue
                if "DIP" not in newheaders:
                    print ("rejecting file - no DIP: ", newheaders)
                    continue
                #print (idx)
                try:
                    df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
                    #df = pd.read_csv()
                    #print (df)
                except Exception as e:
                    print (e)
                    pass
                survey_dfs[f] = df
    return df
checkfile_by_path('C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00029437\\R00029437.D005062820.D.file.txt')
def checkfile_by_path(path):
    for rin,surveys in  surveyfiles_by_rin.items():
        for s in surveys:
            f = s[0]
            idx = s[1]
            line = s[2]
            newheaders = s[3]
            #print (rin,f)
            #assert "BHID" in newheaders
            #assert "DEPTH" in newheaders
            if f == path:
                if "BHID" not in newheaders:
                    #print ("rejecting file - no BHID: ", newheaders)
                    continue
                if "DIP" not in newheaders:
                    print ("rejecting file - no DIP: ", newheaders)
                    continue
                #print (idx)
                try:
                    df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
                    #df = pd.read_csv()
                    #print (df)
                    return df
                except Exception as e:
                    print (e)
                    pass
checkfile_by_path('C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00029437\\R00029437.D005062820.D.file.txt')
surveyfiles_by_rin['R00029437']
checkfile_by_path('C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00029437\\R00029437.D005062820.D.file.txt')
surveyfiles_by_rin['R00054921']
checkfile_by_path('C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00054921\\EL6321_200611_08_appendix.txt')
runfile('C:/Users/gatesk/Documents/missing_/RINS_SEARCH/R00054921/untitled14.py', wdir='C:/Users/gatesk/Documents/missing_/RINS_SEARCH/R00054921')
encoding
m
runfile('C:/Users/gatesk/Documents/missing_/RINS_SEARCH/R00054921/untitled14.py', wdir='C:/Users/gatesk/Documents/missing_/RINS_SEARCH/R00054921')
detectencoding(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_06_appendix.txt")
detectencoding(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029437\R00029437.D005062820.D.file.txt")
runfile('C:/Users/gatesk/Documents/missing_/RINS_SEARCH/R00054921/untitled14.py', wdir='C:/Users/gatesk/Documents/missing_/RINS_SEARCH/R00054921')
predict_encoding(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_06_appendix.txt")
predict_encoding(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_08_appendix.txt")
runfile('C:/Users/gatesk/Documents/missing_/RINS_SEARCH/R00054921/untitled14.py', wdir='C:/Users/gatesk/Documents/missing_/RINS_SEARCH/R00054921')
predict_encoding(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_08_appendix.txt")
predict_encoding(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_06_appendix.txt")
detectencoding(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00029437\R00029437.D005062820.D.file.txt")
detectencoding(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_06_appendix.txt")
checkfile_by_path('C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00029437\\R00029437.D005062820.D.file.txt')
checkfile_by_path('C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00054921\\EL6321_200611_08_appendix.txt')
def checkfile_by_path(path):
    for rin,surveys in  surveyfiles_by_rin.items():
        for s in surveys:
            f = s[0]
            idx = s[1]
            line = s[2]
            newheaders = s[3]
            #print (rin,f)
            #assert "BHID" in newheaders
            #assert "DEPTH" in newheaders
            if f == path:
                if "BHID" not in newheaders:
                    #print ("rejecting file - no BHID: ", newheaders)
                    continue
                if "DIP" not in newheaders:
                    print ("rejecting file - no DIP: ", newheaders)
                    continue
                #print (idx)
                try:
                    df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
                    #df = pd.read_csv()
                    #print (df)
                    return df
                except Exception as e:
                    raise (e)
                    pass
checkfile_by_path('C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00054921\\EL6321_200611_08_appendix.txt')
def checkfile_by_path(path):
    for rin,surveys in  surveyfiles_by_rin.items():
        for s in surveys:
            f = s[0]
            idx = s[1]
            line = s[2]
            newheaders = s[3]
            #print (rin,f)
            #assert "BHID" in newheaders
            #assert "DEPTH" in newheaders
            if f == path:
                if "BHID" not in newheaders:
                    #print ("rejecting file - no BHID: ", newheaders)
                    continue
                if "DIP" not in newheaders:
                    print ("rejecting file - no DIP: ", newheaders)
                    continue
                #print (idx)
                try:
                    df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
                    #df = pd.read_csv()
                    #print (df)
                    return df
                except UnicodeDecodeError as readerror:
                    df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders,encoding='windows-1252')
                except Exception as e:
                    raise (e)
                    pass
checkfile_by_path('C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00054921\\EL6321_200611_08_appendix.txt')
df
def checkfile_by_path(path):
    for rin,surveys in  surveyfiles_by_rin.items():
        for s in surveys:
            f = s[0]
            idx = s[1]
            line = s[2]
            newheaders = s[3]
            #print (rin,f)
            #assert "BHID" in newheaders
            #assert "DEPTH" in newheaders
            if f == path:
                if "BHID" not in newheaders:
                    #print ("rejecting file - no BHID: ", newheaders)
                    continue
                if "DIP" not in newheaders:
                    print ("rejecting file - no DIP: ", newheaders)
                    continue
                #print (idx)
                try:
                    df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
                    #df = pd.read_csv()
                    #print (df)
                    return df
                except UnicodeDecodeError as readerror:
                    df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders,encoding='windows-1252')
                except Exception as e:
                    raise (e)
                    pass
def checkfile_by_path(path):
    for rin,surveys in  surveyfiles_by_rin.items():
        for s in surveys:
            f = s[0]
            idx = s[1]
            line = s[2]
            newheaders = s[3]
            #print (rin,f)
            #assert "BHID" in newheaders
            #assert "DEPTH" in newheaders
            if f == path:
                if "BHID" not in newheaders:
                    #print ("rejecting file - no BHID: ", newheaders)
                    continue
                if "DIP" not in newheaders:
                    print ("rejecting file - no DIP: ", newheaders)
                    continue
                #print (idx)
                try:
                    df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders)
                    #df = pd.read_csv()
                    #print (df)
                    return df
                except UnicodeDecodeError as readerror:
                    df = pd.read_csv(f,sep='\t',skiprows=idx,names=newheaders,encoding='windows-1252')
                    return df
                except Exception as e:
                    raise (e)
                    pass
checkfile_by_path('C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\\R00054921\\EL6321_200611_08_appendix.txt')
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
merged.to_csv('merged_out.csv',sep='|')
merged.to_csv('merged_out_v2.csv',sep='|')
merged = merged.sort_values(by=['BHID','DEPTH'])
merged.to_csv('text_out.csv',sep='|',index=False)
merged.to_csv('merged_out_v3.csv',sep='|',index=False)
merged
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
df
runfile('C:/Users/gatesk/.spyder-py3/untitled15.py', wdir='C:/Users/gatesk/.spyder-py3')
detect_delimter(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_06_appendix.txt")
runfile('C:/Users/gatesk/.spyder-py3/untitled15.py', wdir='C:/Users/gatesk/.spyder-py3')
detect_delimter(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_06_appendix.txt")
runfile('C:/Users/gatesk/.spyder-py3/untitled15.py', wdir='C:/Users/gatesk/.spyder-py3')
detect_delimter(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_06_appendix.txt")
runfile('C:/Users/gatesk/.spyder-py3/untitled15.py', wdir='C:/Users/gatesk/.spyder-py3')
detect_delimter(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_06_appendix.txt")
runfile('C:/Users/gatesk/.spyder-py3/untitled15.py', wdir='C:/Users/gatesk/.spyder-py3')
detect_delimter(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_06_appendix.txt")
runfile('C:/Users/gatesk/.spyder-py3/untitled15.py', wdir='C:/Users/gatesk/.spyder-py3')
detect_delimter(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_06_appendix.txt")
runfile('C:/Users/gatesk/.spyder-py3/untitled15.py', wdir='C:/Users/gatesk/.spyder-py3')
detect_delimter(r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH\R00054921\EL6321_200611_06_appendix.txt")
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
surveyfiles
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
surveyfiles
import csv, os
from collections import defaultdict
from H1000_survey_lk import surveyheaders, surveyheaders2
import re
import pandas as pd

rinholes = defaultdict(list)
root = r'C:/Users/gatesk/Documents/missing_/RINS_SEARCH'

with open(r"C:/Users/gatesk/Documents/missing_/RIN_HOLES_MASTER.csv") as master:
    rdr = csv.reader(master, delimiter='|')
    for line in rdr:
        #print (line)
        rin = line[2]
        hole = line[5]
        rinholes[hole].append(rin)


all_rins = set()

for hole,rins in rinholes.items():
    for rin in rins:
        all_rins.add(rin)


rinfiles = defaultdict(list)

def findsurveys(fold):
    def absoluteFilePaths(directory):
       for dirpath,_,filenames in os.walk(directory):
           for f in filenames:
               yield os.path.abspath(os.path.join(dirpath, f))
    
    def is_a_survey(headerline):
        elements = re.split('[ \t,]', headerline)
        #if headers suggests it is a survey file
        for e in elements:
           if e in  surveyheaders:
               return True
    
    
    def isH1000(fin):
        with open(fin) as f:
            for idx, line in enumerate(f):
                if idx > 100:
                    break
                if line.startswith('H1000'):
                    return idx,line
                if line.startswith('"H1000'):
                    return idx,line
            return -1, None
    
    surveyfiles = []
    
    def detect_delimter(fin):
        try:
            with open(fin, 'r') as f:
                dialect = csv.Sniffer().sniff(f.read())    
            return dialect.delimiter
        except Exception as e:
            return 'delimiter_error'
    
    
    for f in absoluteFilePaths(fold):
        ext = os.path.splitext(f)[1]
        if ext not in ['.txt']:
            continue
        idx, line = isH1000(f)
        if idx != -1:
            if is_a_survey(line):
                sep = detect_delimter(f)
                surveyfiles.append([f,idx,line,None,sep])
    
    return surveyfiles


surveyfiles_by_rin = defaultdict(list)
surveyfiles
surveyfiles_by_rin
import csv, os
from collections import defaultdict
from H1000_survey_lk import surveyheaders, surveyheaders2
import re
import pandas as pd

rinholes = defaultdict(list)
root = r'C:/Users/gatesk/Documents/missing_/RINS_SEARCH'

with open(r"C:/Users/gatesk/Documents/missing_/RIN_HOLES_MASTER.csv") as master:
    rdr = csv.reader(master, delimiter='|')
    for line in rdr:
        #print (line)
        rin = line[2]
        hole = line[5]
        rinholes[hole].append(rin)


all_rins = set()

for hole,rins in rinholes.items():
    for rin in rins:
        all_rins.add(rin)


rinfiles = defaultdict(list)

def findsurveys(fold):
    def absoluteFilePaths(directory):
       for dirpath,_,filenames in os.walk(directory):
           for f in filenames:
               yield os.path.abspath(os.path.join(dirpath, f))
    
    def is_a_survey(headerline):
        elements = re.split('[ \t,]', headerline)
        #if headers suggests it is a survey file
        for e in elements:
           if e in  surveyheaders:
               return True
    
    
    def isH1000(fin):
        with open(fin) as f:
            for idx, line in enumerate(f):
                if idx > 100:
                    break
                if line.startswith('H1000'):
                    return idx,line
                if line.startswith('"H1000'):
                    return idx,line
            return -1, None
    
    surveyfiles = []
    
    def detect_delimter(fin):
        try:
            with open(fin, 'r') as f:
                dialect = csv.Sniffer().sniff(f.read())    
            return dialect.delimiter
        except Exception as e:
            return 'delimiter_error'
            pass
    
    
    for f in absoluteFilePaths(fold):
        ext = os.path.splitext(f)[1]
        if ext not in ['.txt']:
            continue
        idx, line = isH1000(f)
        if idx != -1:
            if is_a_survey(line):
                sep = detect_delimter(f)
                surveyfiles.append([f,idx,line,None,sep])
    
    return surveyfiles


surveyfiles_by_rin = defaultdict(list)
surveyfiles_by_rin
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
import csv, os
from collections import defaultdict
from H1000_survey_lk import surveyheaders, surveyheaders2
import re
import pandas as pd

rinholes = defaultdict(list)
root = r'C:/Users/gatesk/Documents/missing_/RINS_SEARCH'

with open(r"C:/Users/gatesk/Documents/missing_/RIN_HOLES_MASTER.csv") as master:
    rdr = csv.reader(master, delimiter='|')
    for line in rdr:
        #print (line)
        rin = line[2]
        hole = line[5]
        rinholes[hole].append(rin)


all_rins = set()

for hole,rins in rinholes.items():
    for rin in rins:
        all_rins.add(rin)


rinfiles = defaultdict(list)

def findsurveys(fold):
    def absoluteFilePaths(directory):
       for dirpath,_,filenames in os.walk(directory):
           for f in filenames:
               yield os.path.abspath(os.path.join(dirpath, f))
    
    def is_a_survey(headerline):
        elements = re.split('[ \t,]', headerline)
        #if headers suggests it is a survey file
        for e in elements:
           if e in  surveyheaders:
               return True
    
    
    def isH1000(fin):
        with open(fin) as f:
            for idx, line in enumerate(f):
                if idx > 100:
                    break
                if line.startswith('H1000'):
                    return idx,line
                if line.startswith('"H1000'):
                    return idx,line
            return -1, None
    
    surveyfiles = []
    
    def detect_delimter(fin):
        try:
            with open(fin, 'r') as f:
                dialect = csv.Sniffer().sniff(f.read())    
            return dialect.delimiter
        except Exception as e:
            print (fin,e)
            pass
    
    
    for f in absoluteFilePaths(fold):
        ext = os.path.splitext(f)[1]
        if ext not in ['.txt']:
            continue
        idx, line = isH1000(f)
        if idx != -1:
            if is_a_survey(line):
                sep = detect_delimter(f)
                surveyfiles.append([f,idx,line,None,sep])
    
    return surveyfiles
surveyfiles_by_rin
import csv, os
from collections import defaultdict
from H1000_survey_lk import surveyheaders, surveyheaders2
import re
import pandas as pd

rinholes = defaultdict(list)
root = r'C:/Users/gatesk/Documents/missing_/RINS_SEARCH'

with open(r"C:/Users/gatesk/Documents/missing_/RIN_HOLES_MASTER.csv") as master:
    rdr = csv.reader(master, delimiter='|')
    for line in rdr:
        #print (line)
        rin = line[2]
        hole = line[5]
        rinholes[hole].append(rin)


all_rins = set()

for hole,rins in rinholes.items():
    for rin in rins:
        all_rins.add(rin)


rinfiles = defaultdict(list)

def findsurveys(fold):
    def absoluteFilePaths(directory):
       for dirpath,_,filenames in os.walk(directory):
           for f in filenames:
               yield os.path.abspath(os.path.join(dirpath, f))
    
    def is_a_survey(headerline):
        elements = re.split('[ \t,]', headerline)
        #if headers suggests it is a survey file
        for e in elements:
           if e in  surveyheaders:
               return True
    
    
    def isH1000(fin):
        with open(fin) as f:
            for idx, line in enumerate(f):
                if idx > 100:
                    break
                if line.startswith('H1000'):
                    return idx,line
                if line.startswith('"H1000'):
                    return idx,line
            return -1, None
    
    surveyfiles = []
    
    def detect_delimter(fin):
        try:
            with open(fin, 'r') as f:
                dialect = csv.Sniffer().sniff(f.read())    
            return dialect.delimiter
        except Exception as e:
            print (fin,e)
            pass
    
    
    for f in absoluteFilePaths(fold):
        ext = os.path.splitext(f)[1]
        if ext not in ['.txt']:
            continue
        idx, line = isH1000(f)
        if idx != -1:
            if is_a_survey(line):
                sep = detect_delimter(f)
                surveyfiles.append([f,idx,line,None,sep])
    
    return surveyfiles
surveyfiles
import csv, os
from collections import defaultdict
from H1000_survey_lk import surveyheaders, surveyheaders2
import re
import pandas as pd

rinholes = defaultdict(list)
root = r'C:/Users/gatesk/Documents/missing_/RINS_SEARCH'

with open(r"C:/Users/gatesk/Documents/missing_/RIN_HOLES_MASTER.csv") as master:
    rdr = csv.reader(master, delimiter='|')
    for line in rdr:
        #print (line)
        rin = line[2]
        hole = line[5]
        rinholes[hole].append(rin)


all_rins = set()

for hole,rins in rinholes.items():
    for rin in rins:
        all_rins.add(rin)


rinfiles = defaultdict(list)

def findsurveys(fold):
    def absoluteFilePaths(directory):
       for dirpath,_,filenames in os.walk(directory):
           for f in filenames:
               yield os.path.abspath(os.path.join(dirpath, f))
    
    def is_a_survey(headerline):
        elements = re.split('[ \t,]', headerline)
        #if headers suggests it is a survey file
        for e in elements:
           if e in  surveyheaders:
               return True
    
    
    def isH1000(fin):
        with open(fin) as f:
            for idx, line in enumerate(f):
                if idx > 100:
                    break
                if line.startswith('H1000'):
                    return idx,line
                if line.startswith('"H1000'):
                    return idx,line
            return -1, None
    
    surveyfiles = []
    
    def detect_delimter(fin):
        try:
            with open(fin, 'r') as f:
                dialect = csv.Sniffer().sniff(f.read())    
            return dialect.delimiter
        except Exception as e:
            print (fin,e)
            pass
    
    
    for f in absoluteFilePaths(fold):
        ext = os.path.splitext(f)[1]
        if ext not in ['.txt']:
            continue
        idx, line = isH1000(f)
        if idx != -1:
            if is_a_survey(line):
                #sep = detect_delimter(f)
                surveyfiles.append([f,idx,line,None])
    
    return surveyfiles
surveyfiles
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
problemfiles.close()
merged = merged.sort_values(by=['BHID','DEPTH'])
merged.to_csv('merged_out_v4.csv',sep='|',index=False)
def checkfile_by_path(path):
    for rin,surveys in  surveyfiles_by_rin.items():
        for s in surveys:
            f = s[0]
            idx = s[1]
            line = s[2]
            newheaders = s[3]
            delimiter = s[4]
            #print (rin,f)
            #assert "BHID" in newheaders
            #assert "DEPTH" in newheaders
            if "BHID" not in newheaders:
                #print ("rejecting file - no BHID: ", newheaders)
                continue
            if "DIP" not in newheaders:
                print ("rejecting file - no DIP: ", newheaders)
                continue
            #print (idx)
            print (idx,f,delimiter)
            try:
                df = pd.read_csv(f,sep=delimiter,skiprows=idx,names=newheaders)
                #df = pd.read_csv()
                #print (df)
                #return df
            except UnicodeDecodeError as readerror:
                df = pd.read_csv(f,sep=delimiter,skiprows=idx,names=newheaders,encoding='windows-1252')
                #return df
            except Exception as e:
                #raise (e)
                print ("failed to read into df: ",idx,f,e)
                problemfiles.write("failed to read into df|"+'|'+str(f)+'|'+str(e)+'\n')
                #os.startfile((f),'open')
                pass
checkfile_by_path(r'C:\Users\gatesk\Documents\missing_\RINS_SEARCH\RE0001652\RE0001652.DE01652040.D.file.txt')
surveydf['C:\Users\gatesk\Documents\missing_\RINS_SEARCH\RE0001652\RE0001652.DE01652040.D.file.txt']
surveydf[r'C:\Users\gatesk\Documents\missing_\RINS_SEARCH\RE0001652\RE0001652.DE01652040.D.file.txt']
survey_df['C:\Users\gatesk\Documents\missing_\RINS_SEARCH\RE0001652\RE0001652.DE01652040.D.file.txt']
survey_df[r'C:\Users\gatesk\Documents\missing_\RINS_SEARCH\RE0001652\RE0001652.DE01652040.D.file.txt']
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
merged = merged.sort_values(by=['BHID','DEPTH'])
merged.to_csv('merged_out_v5.csv',sep='|',index=False)
runfile('C:/Users/gatesk/.spyder-py3/master.py', wdir='C:/Users/gatesk/.spyder-py3')
runfile('C:/Users/gatesk/.spyder-py3/untitled16.py', wdir='C:/Users/gatesk/.spyder-py3')
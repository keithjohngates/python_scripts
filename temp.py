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


#collarxyz = np.array([450000,6868000,500]) #x,y,z
#collarsurvey = np.array([-60,270])#dip azi
## several data points 
        
#r = np.array([0, 14, 64, 114]) #depths from interval file
#phi = np.array([255.6, 255.6, 261.7, 267.4]) #azimuths
#theta = np.array([-79.5, -79.5, -79.4, -78.8]) #dips

## get lengths of the separate segments 
#r[1:] = r[1:] - r[:-1]
#print (r)
## convert azimuths to radians
#phi = phi * 2 * np.pi / 360.
#print (phi)
## in spherical coordinates theta is measured from zenith down; you are measuring it from horizontal plane up 
#theta = (90. - theta) * 2 * np.pi / 360.
#print (theta)
## get x, y, z from known formulae
#x = r*np.cos(phi)*np.sin(theta)
#print (x)
#y = r*np.sin(phi)*np.sin(theta)
#print (y)
#z = r*np.cos(theta)
#print (z)

# np.cumsum is employed to gradually sum resultant vectors 
# ax.plot(np.cumsum(x),np.cumsum(y),np.cumsum(z))

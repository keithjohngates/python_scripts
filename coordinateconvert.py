from pyproj import Proj, transform

fin = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\collars_coordinates_MGA_TO_LAT_LONG.csv",'r')
fout = open(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\collars_coordinates_MGA_TO_LAT_LONG_converted.csv",'w')
count = 0
for line in fin:
    E = line.split('|')[0]
    N = line.split('|')[1]
    inProj = line.split('|')[2]
    E = float(E)
    N = float(N)
    try:
        #inProj = str(line.split('|')[2].rstrip())
        #outProj = 'epsg:283'+ str(inProj[-2:])
        inProj = Proj(init=inProj)
        outProj = Proj(init='epsg:4326')
        x2,y2 = transform(inProj,outProj,E,N)
        fout.write(line.rstrip()+'|'+str(x2)+'|'+str(y2)+'\n')
    except:
        print (count)
        fout.write(line)
        pass
    count = count + 1
    
fout.close()

#for line in colin:
#    #print (line)
#    #input()
#    items = line.split('|')
#    try:
#        lat =  (items[17].rstrip())
#        long =  (items[18].rstrip())
#        zone = (items[7].rstrip())
#        inProj = Proj(init='epsg:4326')
#        outProj = Proj(init='epsg:28354')
#        #print (lat,long)
#        lat = float(lat)
#        long = float(long)
#        zone = int(zone)
#    except Exception as e:
#        print (e)
#        pass
#    #print (lat,long)
#    try:
#        if zone == 54:
#            outProj = Proj(init='epsg:28354')
#        if zone == 55:
#            outProj = Proj(init='epsg:28355')
#        if zone == 56:
#            outProj = Proj(init='epsg:28356')
#        x2,y2 = transform(inProj,outProj,long,lat)
#        colout.write(line.rstrip()+'|'+str(x2)+'|'+str(y2)+'\n')
#        #print (x2,y2)
#    except Exception as e:
#        print (e)
#        colout.write(line)
#        pass
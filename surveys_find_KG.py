surveyheaders = {"Az-GRID": "AZI_GRID",
"AZI_GRID": "AZI_GRID",
"AziGrid": "AZI_GRID",
"AZI-GRID": "AZI_GRID",
"AZIMUTHGRIDNAME": "AZI_GRID",
"Az_loc": "AZI_LOCAL",
"Azimuth_Local": "AZI_LOCAL",
"Local_Azimuth": "AZI_LOCAL",
"Local_Azimuth_grid": "AZI_LOCAL",
"Local_Collar_Azimuth": "AZI_LOCAL",
"LocalAzim": "AZI_LOCAL",
"(Mag)": "AZI_MAG",
"az(mag)": "AZI_MAG",
"Az_mag": "AZI_MAG",
"AZI_MAG": "AZI_MAG",
"Azi_Mag": "AZI_MAG",
"Azi_mag": "AZI_MAG",
"AziMag": "AZI_MAG",
"Azimuth(mag)": "AZI_MAG",
"Azimuth_MAG": "AZI_MAG",
"Azimuth_Mag": "AZI_MAG",
"Azimuth_mag": "AZI_MAG",
"Azimuth_Magnetic": "AZI_MAG",
"Azimuth_TRUE": "AZI_MAG",
"Azimuth-mag": "AZI_MAG",
"Az-MAG": "AZI_MAG",
"Col_Azi_Mag": "AZI_MAG",
"mag_azim": "AZI_MAG",
"MAG_Azimuth": "AZI_MAG",
"mag_azimuth": "AZI_MAG",
"SurvAzimuthMag": "AZI_MAG",
"SurvAzimuthTN": "AZI_MAG",
"AZIMUTHTYPE": "AZI_TYPE",
"Az": "AZI_UNK",
"Azim": "AZI_UNK",
"azimith": "AZI_UNK",
"AZIMUTH": "AZI_UNK",
"Azimuth": "AZI_UNK",
"azimuth": "AZI_UNK",
"Azimuth_M": "AZI_UNK",
"collar_az": "AZI_UNK",
"Collar_Azimuth": "AZI_UNK",
"Collar_azimuth": "AZI_UNK",
"CollarAzi": "AZI_UNK",
"Corrected_Orig_Azimuth": "AZI_UNK",
"Orig_Azimuth": "AZI_UNK",
"Ref_Azimuth": "AZI_UNK",
"ref_azimuth": "AZI_UNK",
"RefAzim": "AZI_UNK",
"work_azimuth": "AZI_UNK",
"AMG_AGD66_Z54_GDAZIMUTH": "AZI_UTM",
"AMG_Azim": "AZI_UTM",
"AMG_Azimuth": "AZI_UTM",
"amg_azimuth": "AZI_UTM",
"Az(MGA)": "AZI_UTM",
"az(MGA)": "AZI_UTM",
"Az_MGA": "AZI_UTM",
"Azi_AMG": "AZI_UTM",
"Azimuth(grid)": "AZI_UTM",
"AZIMUTH_AMG": "AZI_UTM",
"Azimuth_AMG": "AZI_UTM",
"Azimuth_GDA": "AZI_UTM",
"Azimuth_Grid": "AZI_UTM",
"Azimuth_grid": "AZI_UTM",
"Azimuth_MGA": "AZI_UTM",
"Azimuth_mga": "AZI_UTM",
"Col_Azi_AMG": "AZI_UTM",
"Collar_grid_azimuth": "AZI_UTM",
"gda_azim": "AZI_UTM",
"Grid_Azimuth": "AZI_UTM",
"MGA_Azimuth": "AZI_UTM",
"MGA_azimuth": "AZI_UTM",
"MGAAzim": "AZI_UTM",
"NAT_Azimuth": "AZI_UTM",
"(dip": "DIP",
"(incl": "DIP",
"Angle": "DIP",
"ANGLES": "DIP",
"Col_Dip": "DIP",
"Coll_Dip": "DIP",
"collar_dip": "DIP",
"Collar_Inclination": "DIP",
"Collar_inclination": "DIP",
"CollarDip": "DIP",
"DIP": "DIP",
"Dip": "DIP",
"dip": "DIP",
"Dip/Dir": "DIP",
"Dip_Az.": "DIP",
"DIP_DIRECTION": "DIP",
"Dip_Direction": "DIP",
"incl.": "DIP",
"Inclination": "DIP",
"SurvDip": "DIP",
"tdip_dirM": "DIP",
"tdip_dirRef": "DIP",
"true_dipM": "DIP",
"true_dipRef": "DIP"
}


import os
import re
path = r"C:\Users\gatesk\Documents\missing_\RINS_SEARCH"
headers = set()
uniqueheaders = open("unique_headers.txt",'w')
H1000fields = open("H1000_fields.txt",'w')

def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))
           
def isH1000(fin):
    with open(fin) as f:
        if 'H1000' in f.read():
            yield fin
        else:
            pass

def getallH1000headers(e):
    headers.add(e.strip('\n'))
    return headers

surveyfiles = set()

def H1000lines(fin):
    with open(fin) as f:
        for line in f:
            elements = re.split('[ \t,]', line)
            if "H1000" in elements:
                
                H1000fields.write(str(fin).split('\\')[-2]+'\t'+str(fin))
                for h in elements:
                    H1000fields.write('\t'+h.strip('\n'))
                H1000fields.write('\n')
                
                H1000fields.write(str(fin).split('\\')[-2]+'\t'+str(fin))
                for h in elements:
                    if h in surveyheaders:
                        surveyfiles.add(fin)
                        H1000fields.write('\t'+surveyheaders[h])
                    else:
                        H1000fields.write('\t')
                H1000fields.write('\n')
                
                for e in elements:
                    getallH1000headers(e)
            else:
                pass
            
for i in absoluteFilePaths(path):
    if str(i).endswith('txt'):
      #print (i.split("\\")[-2])
      for j in isH1000(i):
          H1000lines(j)
          #print (j)

for i in sorted(headers):
    uniqueheaders.write(i+'\n')
uniqueheaders.close()
H1000fields.close()


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
        if idx % 1000 == 0:
            print (idx)
        elements = re.split('[ \t,]', line)
        for hole in HOLEIDS:
            if hole in elements:
                surveyline = line.rstrip('\n')
                if surveyline not in surveylines:
                    surveylines.add(surveyline)
                    surveyout.write(surveyline.strip()+'\n')
                else:
                    pass      
                
                
                
                
                
                                
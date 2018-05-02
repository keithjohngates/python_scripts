from os import walk
import os
import pandas as pd

f = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\gatesk\.spyder-py3\R00019462"):
    f.extend(filenames)
    break

count = 1
for i in f:
    fin = os.path.join("C:\\Users\\gatesk\\.spyder-py3\\R00019462\\",str(i))
    fout = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\R00019462_EL2619_'+str(count)+"_SG1_A.txt",'w')
    df = pd.read_csv(open(fin,'rb'),sep='|')
    
    '''creates some lists for the header fields'''
    try:
        H0203_Number_of_data_records  = len(df)
        H0802_Assay_company = df.Laboratory.unique()
        H0200_Start_date_of_data_aquisition = min(df['Assay Date'].unique())
        H0201_End_date_of_data_aquisition = max(df['Assay Date'].unique())
        H0600_Sample_code = df['SAMPLE_CODE'].unique()
    except:
        pass
    
    '''creates the assay code lists'''
    techniques = ['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']
    H0800_Assay_code = []
    H0800_Assay_codes = set()
    for j in techniques:
        ass =  df[str(j)].unique()
        for l in ass:
            H0800_Assay_codes.add(str(l).rstrip())
    try:        
        H0800_Assay_codes.remove('0')
    except:
        pass
    try:        
        H0800_Assay_codes.remove('0.0')
    except:
        pass

    fout.write('H0001|Exploration licence data header\n')
    fout.write('H0002|Version 1|A\n')
    fout.write('H0003|Date_generated|06/11/2017\n')
    fout.write('H0004|Reporting period end_date|15/01/2000\n')
    fout.write('H0005|State|NSW\n')
    fout.write('H0100|Tenement_name|EL2619\n')
    fout.write('H0101|Tenement_holder|Ross Mining NL\n')
    fout.write('H0102|Project_name|Timbarra\n')
    fout.write('H0200|Start_date_of_data_aquisition|'+str(H0200_Start_date_of_data_aquisition)+'\n')		
    fout.write('H0201|End_date_of_data_aquisition|'+str(H0201_End_date_of_data_aquisition)+'\n')						
    fout.write('H0202|Template_format|SG1\n')				
    fout.write('H0203|Number_of_data_records|'+str(H0203_Number_of_data_records)+'\n')		
    fout.write('H0204|Date_of_metadata_update\n')
    fout.write('H0500|Feature_located|Sample Location\n')
    fout.write('H0501|Geodetic_datum|AGD66\n')
    fout.write('H0502|Vertical_datum|AHD\n')
    fout.write('H0503|Projection|UTM\n')
    fout.write('H0530|Coordinate_system|AMG\n')
    fout.write('H0531|Projection_zone|56\n')
    fout.write('H0532|Surveying_instrument\n')
    fout.write('H0533|Surveying_comapny\n')
    
    fout.write('H0600|Sample_code')    
    for i in H0600_Sample_code:     
        fout.write('|'+str(i).strip())
    fout.write('\n')
        
    fout.write('H0601|Sample_type\n')

    fout.write('H0800|Assay_code')
    for i in H0800_Assay_codes:
        #print (i)
        fout.write('|'+str(i.rstrip()))
    fout.write('\n') 

    fout.write('H0802|Assay_company')
    for i in H0802_Assay_company:
        fout.write('|'+str(i).rstrip())
    fout.write('\n')
    
    '''creates a dict for the headers and the first record of each column'''
    with open(fin) as f:
        content = f.readlines()
        keys = content[0].rstrip().split('|')
        values = content[1].rstrip().split('|')
    dictionary = dict(zip(keys, values))
    
    '''creates a dict for the elements and the detection limits and the techniques created in the dict above'''
    lk =  dict()
    for i in ['Au','As','Ag','Bi','Mo','Cu','Pb','Zn']:
        lk[str(i)] = (dictionary.get(str(i)+'_Technique'),dictionary.get(str(i)+'_Det_Lim_(ppm)'),dictionary.get(str(i)+'_Det_Lim_(ppb)'))
    
    '''writes out the headers'''   
    for i in keys:
        fout.write(str(i).strip()+'|')
    fout.write('\n') 
    
    '''writes out the suffixes after of the headers'''     
    for i in keys:
        try:
            fout.write(i.strip().split('_')[1])
        except:
            pass
        fout.write('|')
    fout.write('\n')

    '''writes out the detection limits by looking up in the dict'''    
    for i in keys:
        try:
            #print (i)
            #print (lk.get(str(i[:2]))[1])
            fout.write(lk.get(str(i.strip()[:2]))[1])
        except:
            pass
        fout.write('|')
    fout.write('\n')
    
    '''writes out the assay methods by looking up in the dict'''  
    for i in keys:
        try:
            #print (i)
            #print (lk.get(str(i[:2]))[0])
            fout.write(lk.get(str(i[:2]))[0])
        except:
            pass
        fout.write('|')    
    fout.write('\n')
    
    '''writes out the remaining data lines'''  
    for i in content[1:]:
        fout.write(str(i))
    fout.close()
    count = count+1
fout.close()
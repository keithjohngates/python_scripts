# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:33:54 2018

@author: gatesk
"""
newroot = r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO\RE0003971_cleaned'

import os
import csv

from gather_db_data_dgc import GatherDatabaseData
from database_connection_dgc import DatabaseConnection
dbconnection_string = r'DSN=GEODWH;UID=gatesk;PWD=Oldsp00n'


#for a,b,c in os.walk(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix'):
#    for file in c:
#        rin = a.split('\\')[-1]
#        filepath =  os.path.join(a,file)
#        with open(filepath,'r') as fin:
#            for line in fin:
#                if line.startswith('H0202'):
#                    if 'DG' in line:
##                        print (line)
##                        print (filepath)
#                        newname = rin+'_'+file
#                        newpath = os.path.join(newroot, newname)
##                        print (newpath)
#                        shutil.copy(filepath, newpath)

def get_file_delimiters(filepath):
    with open(filepath, 'r') as fin:
        line = fin.readline()
        try:
            dialect = csv.Sniffer().sniff(line, delimiters = '\t,')
            if dialect.delimiter == '\t':
                delimiter = '\t'
            elif dialect.delimiter == ',':
                delimiter = ','
            else:
                delimiter = 'unk'
        except:
            delimiter = 'unk'
    return delimiter

def create_new_filename(delimiter, rin):
    get_new_filename = GatherDatabaseData(dbconnection_string, rin, delimiter).get_new_filename()
    return get_new_filename

#newheadersout = open(r'C:\Users\gatesk\Documents\_downhole_assays_fix\newheadersout.txt','w')


H1000lk_dict = dict()
    
with open('H1000set_file.txt','r')as H1000setfile:
    for line in H1000setfile:
        lk = line.split('\t')
        H1000lk_dict[lk[0]] = lk[1].strip()

H1000lk_dict[''] = ''

#for k,v in  H1000lk_dict.items():
#    print (k,v)


for a,b,c in os.walk(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO\RE0003971'):
    
    for file in c:
        newfile = 'new_'+ file
        rin = file.split('_')[0]
        filepath =  os.path.join(a,file)
        delimiter = get_file_delimiters(filepath)
        dbgather =  GatherDatabaseData(dbconnection_string, rin, delimiter)
        newfilename = create_new_filename(delimiter,rin)
        newfilename = f'{newfilename[0]}_{newfilename[1]}_01_DGC_{newfilename[2]}_{file}'
        newfilepath =  os.path.join(a,newfilename)
        print (newfilename)
#        newheadersout.write(filepath+'\n')
        newfilepath =  os.path.join(newroot,newfilename)
        print (newfilepath)
#        os.rename(filepath,newfilepath)
#        os.rename('a.txt', newfilename)
        
        db_corrected_headers = GatherDatabaseData(dbconnection_string, rin, delimiter).current_database_lookup_headers()
#        newfilepath = open(newfilepath,'w')
        with open(newfilepath,'w') as fout:
            for i in db_corrected_headers:
#            newheadersout.write(i+'\n')
                fout.write(i+'\n')
#                newfilepath.write(i+'\n')
            with open(filepath,'r') as old:
                for line in old:
                    if line.startswith('H0200'):
                        fout.write(line)
                    if line.startswith('H0201'):
                        fout.write(line)
                    if line.startswith('H0203'):
                        fout.write(line)
                    if line.startswith('H06'):
                        fout.write(line)
                    if line.startswith('H08'):
                        fout.write(line)
                    if line.startswith('H1000'):
                        fout.write(line)
                        
                        lineitems = line.split(delimiter)
                        lineitems = [x.strip() for x in lineitems]
                        
                        converted = []
                        
                        for items in lineitems:
                            convert = H1000lk_dict[items]
                            converted.append(convert)
                        fout.write(delimiter.join(converted))
                        
                        fout.write('\n')
                        
                    if line.startswith('H1001'):
                        fout.write(line)
                    if line.startswith('H1002'):
                        fout.write(line)
                    if line.startswith('D'):
                        line = line.replace('<','-').replace('< ','-').replace('>','').replace('> ','')
                        fout.write(line)
#        newfilepath.close()
#
#newheadersout.close()

'''generate the H1000 set file'''
#H1000set = set()
#for a,b,c in os.walk(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\GOLD_SGC'):    
#    for file in c:
#        filepath =  os.path.join(a,file)
#        delimiter = get_file_delimiters(filepath)
#        with open(filepath,'r') as old:
#            for line in old:
#                if line.startswith('H1000'):
#                    H1000 = line.split(delimiter)
#                    for item in H1000:
#                        H1000set.add(item.strip())
#                        
#with open('H1000set_file.txt','w')as H1000setfile:
#    for item in H1000set:
#        H1000setfile.write(item+'\n')
        











                
            
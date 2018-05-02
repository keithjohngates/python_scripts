# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:07:46 2018

@author: gatesk
"""
import shelve
import os 
import shutil

local_mountpoint = r'R:\\'
base_folder = r"C:\Users\gatesk\Documents\_downhole_assays_fix\potential_gold_error_rins\\"
#unzippableroot = r'C:\Users\gatesk\Documents\_downhole_assays_fix\_unzippable'
sourceroot = r'G:\Geosurvey\Shared\CogentII\DATA\DIGS_2018_ORIGINAL_DBSOURCE_FILES\RINS_v3\\'

'''grab the rin folders as per the list and create folders and then move the files'''
def gen_RIN_folders(rin):
    rin_path = "%s/%s/%s" % (rin[0:3], rin[3:6], rin[6:9])
    rin_folder_path = os.path.join(local_mountpoint, rin_path)
    print (rin_folder_path)
    assert os.path.exists(rin_folder_path)
    assert os.path.isdir(rin_folder_path)
    out_folder = os.path.join(base_folder, rin)
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    else:
        pass
        print("output folder %s exists already." % out_folder)

    '''move the files into the folder structure'''
    rin_files = os.listdir(rin_folder_path)
    for f in rin_files:
        outfile = os.path.join(out_folder, f)
        infile = os.path.join(rin_folder_path, f)
        if not os.path.exists(outfile):
            print("Copying %s" % outfile)
            shutil.copy(infile, outfile)
        else:
            pass
            print("File %s exists already." % outfile)


checked_dict =  shelve.open(r"G:\Transit\kgates\checked_dict_RINS.db")

for i in checked_dict.items():
    if i[1] == False:
        print (f"\nworking {i}\n")
#        source = os.path.join(sourceroot,i[0])
#        dest =  os.path.join(base_folder,i[0])
#        if not os.path.exists(dest):
#            os.mkdir(dest)
#            
#        print (source,dest)
#        shutil.copy(source,dest)
        gen_RIN_folders(i[0])
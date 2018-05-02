# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 12:43:43 2018

@author: gatesk
"""

import shelve
import shutil
import os

local_mountpoint = r'R:\\'
base_folder = r"X:\_SS_RELOAD\TO BE DONE -20180410\SURF\\"
unzippableroot = r'C:\Users\gatesk\Documents\_downhole_assays_fix\_unzippable'

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


ERRORS_pct_greater_than_100_SURF = []

with open(r"X:\_SS_RELOAD\TO BE DONE -20180410\ERRORS_pct_greater_than_100_SURF.txt") as ringtoh:
    for line in ringtoh:
        ERRORS_pct_greater_than_100_SURF.append(line.strip())
        print (line.strip())
        gen_RIN_folders(line.strip())
        
#with shelve.open(r"G:\Transit\kgates\checked_dict_au.db") as checked_au:
#    for k,v in checked_au.items():
#        if v == False:
#            rin = k.split('\\')[-2]
#            oldpath = fr'C:\Users\gatesk\Documents\_downhole_assays_fix\potential_gold_error_rins\{rin}'
#            
##            newpath = fr'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\{rin}'
##            print (oldpath,newpath)
#            
#            gen_RIN_folders(rin)
#            try:
#                shutil.move(oldpath,newpath)
#            except Exception as e:
#                print (e)
#            print (rin)
#            print (k,v)
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:55:41 2018

@author: gatesk
"""
import os 
import shutil

local_mountpoint = r'R:\\'
base_folder = r"C:\Users\gatesk\Documents\_downhole_assays_fix\\"
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
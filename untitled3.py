# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:38:04 2018

@author: gatesk
"""

import os
#import magic
#import shutil
#import multiprocessing as mp

local_mountpoint = r'R:\\'
base_folder = r"G:\\Geosurvey\\Shared\\CogentII\\DATA\\DIGS_2018_ORIGINAL_DBSOURCE_FILES\RINS_v2\\"
rin_folders = os.listdir(base_folder)

'''generator function to loop through a directory returning the filepaths of contents'''
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))

'''get a list of RINS from a text file'''
def gen_rin_list():
    RINS = []
    RINSin = open(r"G:\Geosurvey\Shared\CogentII\DATA\DIGS_2018_ORIGINAL_DBSOURCE_FILES\scripts\RIN_LIST_notdonev3.txt", 'r')
    for line in RINSin:
        RINS.append(line.rstrip())
    return RINS


RINS = gen_rin_list()
for i in RINS:
    print (i)

# gen_rin_list()
# for i in gen_rin_list():
#     print (i)

'''grab the rin folders as per the list and create folders and then move the files'''
def gen_RIN_folders(rin):
    rin_path = "%s/%s/%s" % (rin[0:3], rin[3:6], rin[6:9])
    rin_folder_path = os.path.join(local_mountpoint, rin_path)
    print (rin_folder_path)
    assert os.path.exists(rin_folder_path)
    assert os.path.isdir(rin_folder_path)
#    out_folder = os.path.join(base_folder, rin)
#    if not os.path.exists(out_folder):
#        os.mkdir(out_folder)
#    else:
#        pass
#        print("output folder %s exists already." % out_folder)
        
RINS = gen_rin_list()

for i in RINS:
    gen_RIN_folders(i)
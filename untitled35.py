# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 08:53:38 2018

@author: gatesk
"""

import os
import shelve
import shutil
toroot = r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix_short'
fromroot = r'G:\Geosurvey\Shared\CogentII\DATA\DIGS_2018_ORIGINAL_DBSOURCE_FILES\RINS_v3'
local_mountpoint = r'R:\\'


with shelve.open(r"G:\Transit\kgates\checked_dict_au.db") as checked_au:
        for idx, i in enumerate(sorted(checked_au)):
#            print (len(checked_au))
            rin = str(i.split('\\')[-2])
            rin_path = "%s/%s/%s" % (rin[0:3], rin[3:6], rin[6:9])
            rin_folder_path = os.path.join(local_mountpoint, rin_path)
            rin_folder_path = os.path.abspath(rin_folder_path)
#            print (rin)
#            print (i)
            if checked_au[i] == False:
                fname = os.path.split(i)[-1]
                oldfname = fname[:-4]
                newfilename = rin+'_'+fname
                old = os.path.join(fromroot,rin_folder_path)
                old = os.path.join(old,oldfname)
                new = os.path.join(toroot,newfilename)
#                filename = os.path.split(checked_au[i])
#                print (old)
#                print (new)
                try:
                    shutil.copy(old,new)
                except Exception as e:
                    print (e)
                    pass
                

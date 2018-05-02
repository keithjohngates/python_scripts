# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:33:54 2018

@author: gatesk
"""
newroot = r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix_short'

import os
import shutil

for a,b,c in os.walk(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix'):
    for file in c:
        rin = a.split('\\')[-1]
        filepath =  os.path.join(a,file)
        with open(filepath,'r') as fin:
            for line in fin:
                if line.startswith('H0202'):
                    if 'DG' in line:
#                        print (line)
#                        print (filepath)
                        newname = rin+'_'+file
                        newpath = os.path.join(newroot, newname)
#                        print (newpath)
                        shutil.copy(filepath, newpath)
                        
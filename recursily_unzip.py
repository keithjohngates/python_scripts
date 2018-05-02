# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:18:40 2018

@author: gatesk
"""

import re
import os
import zipfile
folder = r'C:\Users\gatesk\Documents\_downhole_assays_fix\_unzippable'

def get_zip_files(folder):
    zipfiles = []
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if re.search(r'\.zip$', filename):
                fileSpec = os.path.join(root, filename)
                zipfiles.append(fileSpec)
    return zipfiles
                
def unzip(file_to_unzip):
    zipfold = os.path.split(file_to_unzip)[0]
    zip_ref = zipfile.ZipFile(file_to_unzip) 
    zip_ref.extractall(zipfold) 
    zip_ref.close() 
    os.remove(file_to_unzip) 

def rec_unzip(folder):
    files_to_unzip = get_zip_files(folder)
    print (files_to_unzip)
    if len(files_to_unzip) >= 1:
        for file in files_to_unzip:
            unzip(file)
        return rec_unzip(folder)
    else:
        return None
    
            
rec_unzip(r'C:\Users\gatesk\Documents\_downhole_assays_fix\_unzippable')
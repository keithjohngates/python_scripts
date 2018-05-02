# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:18:40 2018

@author: gatesk
"""

import re
import os
import zipfile
import shelve
import threading
from queue import Queue


q = Queue(maxsize=0)
num_threads = 10

base_folder = r"C:\Users\gatesk\Documents\_downhole_assays_fix\potential_gold_error_rins\\"

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
    
#            
#checked_dict =  shelve.open(r"G:\Transit\kgates\checked_dict_RINS.db")
#def gen_rin_list():
#    for i in checked_dict.items():
#        if i[1] == False:
#            rinpath = os.path.join(base_folder,i[0])
#            q.put(rinpath)
#            
#gen_rin_list()

rins = os.listdir(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\PCT')

for i in rins:
    print (i)
    path = os.path.join(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\PCT',i)
    q.put(path)


def get_files(q):
    while not q.empty():
        rin =  q.get()
        print (rin)
        rec_unzip(rin)
#        gen_RIN_folders(rin)
        q.task_done()

def main():
    for i in range(num_threads):
      worker = threading.Thread(target=get_files, args=(q,))
      worker.start()

main()
print ('Please wait - we are working on it')
q.join()
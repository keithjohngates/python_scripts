# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 10:47:57 2018

@author: gatesk
"""

import os 
import magic
import threading
from queue import Queue
import shelve

q = Queue(maxsize=0)
num_threads = 10
base_folder = r"C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\PCT\\"

file_exts = {
    "application/zip": "zip",
    "application/pdf": "pdf",
    "image/jpeg": "jpeg",
    "image/tiff": "tiff",
    "text/plain": "txt",
    "text/x-fortran": "f",
    "application/octet-stream": "bin"}


'''generator function to loop through a directory returning the filepaths of contents'''
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           filename = os.path.abspath(os.path.join(dirpath, f))
           print (filename)
           yield filename

def fix_a_file(file_path: str):
    detected = magic.from_file(file_path, mime=True)
    if detected in file_exts:
        print("%s -> %s" % (detected, file_exts[detected]))
        os.rename(file_path, file_path + "." + file_exts[detected])
    else:
        print("%s not found?" % (detected))
        assert False

def fix_files(rin):
    for fin in absoluteFilePaths(os.path.join(base_folder,rin)):
        print (fin)
        if str(fin).endswith("file"):
            try:
                fix_a_file(fin)
                print("Converted: " + str(fin))
            except Exception as e:
                print(e)
                print("Failed on:" + str(fin))
                pass
        else:
            pass

rins = os.listdir(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\PCT')

for i in rins:
    print (i)
    q.put(i)

def get_files(q):
    while not q.empty():
        rin =  q.get()
        fix_files(rin)
        q.task_done()

def main():
    for i in range(num_threads):
      worker = threading.Thread(target=get_files, args=(q,))
      worker.start()

main()
print ('Please wait - we are working on it')
q.join()

















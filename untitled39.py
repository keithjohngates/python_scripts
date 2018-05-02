# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:05:44 2018

@author: gatesk
"""

import os 
import threading
from queue import Queue
import csv
from itertools import islice

q = Queue(maxsize=0)
num_threads = 10
base_folder = r"C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO\\"


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

'''generator function to loop through a directory returning the filepaths of contents'''
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           filename = os.path.abspath(os.path.join(dirpath, f))
           yield filename
       

DGFILES = []

def do_work(path):
    with open(path) as fin:
        head = list(islice(fin, 50))
        for line in head:
            dialect = None
            if line.startswith('H0202'):
                try:
                    dialect = csv.Sniffer().sniff(line, delimiters = '\t,')
                    if dialect.delimiter == '\t':
                        delimiter = '\t'
                    elif dialect.delimiter == ',':
                        delimiter = ','
                    else:
                        delimiter = None
                except:
                    pass
                
                try:
                    if line.split(delimiter)[2][:2] == 'DG':
                        DGFILES.append((path, line.split(delimiter)[2]))
#                        print (line.split(delimiter)[2])
                        
                except:
                    print ('No line found')




rins = os.listdir(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO')


sourcefolder = r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO'
destfolder = r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO_RENAMED'

import shutil

for rin in rins:
    for file in absoluteFilePaths(sourcefolder):
        if file.endswith('.txt'):
            do_work(file)

for i in DGFILES:
    source = (i[0])
    sourcepath = os.path.join(sourcefolder,source)
    rin = source.split('\\')[-2]
    destfilename = os.path.split(source)[1]
    destfilename = rin+'_'+destfilename
    dest = os.path.join(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\ROUND_TWO_RENAMED',destfilename)
#    print (source)
#    print (rin)
#    print (destfilename)
    print (sourcepath)
    print (dest)
    shutil.copy(sourcepath,dest)
    
    

#def get_files(q):
#    while not q.empty():
#        rin =  q.get()
#        fix_files(rin)
#        q.task_done()
#
#def main():
#    for i in range(num_threads):
#      worker = threading.Thread(target=get_files, args=(q,))
#      worker.start()
#
#main()
#print ('Please wait - we are working on it')
#q.join()
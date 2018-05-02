# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 10:42:31 2018

@author: gatesk
"""

import os
import threading
from queue import Queue
import csv
from itertools import islice

queue = Queue(maxsize=0)
num_threads = 50

working_folder = r"C:\Users\gatesk\Documents\_downhole_assays_fix\potential_gold_error_rins\\"

'''function to loop through a directory returning the filepaths of contents adding them to a queue'''
def get_paths_queue(directory, queue):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           if os.path.splitext(f)[1] == '.txt':
               path = os.path.abspath(os.path.join(dirpath, f))
               queue.put(path)
        
get_paths_queue(working_folder,queue)

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
                        print (line.split(delimiter)[2])
                        
                except:
                    print ('No line found')


def do_queued_work(q):
    while not queue.empty():
        path =  queue.get()
        do_work(path)
        queue.task_done()


def main():
    for i in range(num_threads):
      worker = threading.Thread(target=do_queued_work, args=(queue,))
      worker.start()

main()
print ('Please wait - we are working on it')
queue.join()

for i in DGFILES:
    print (i[0])
    
    
moveto = r'C:\Users\gatesk\Documents\_downhole_assays_fix\to_check'

import shutil

for i in DGFILES:
    
#    rin = i[0].split('\\')[-2]
#    print (rin)
#    filename = os.path.split(i[0])[1]
#    newfilename = rin + '_' + filename
#    dest = os.path.join(moveto,newfilename)
#    print (i[0])
#    print (dest)
#    shutil.copyfile(i[0],dest)





















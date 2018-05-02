# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 09:39:00 2018

@author: gatesk
"""

import os
import threading
from queue import Queue
import mmap

path = r'X:\\'
queue = Queue(maxsize=0)
num_threads = 100

'''function to loop through a directory returning the filepaths of contents adding them to a queue'''
def get_paths_queue(directory, queue):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           if os.path.splitext(f)[1] == '.txt':
               path = os.path.abspath(os.path.join(dirpath, f))
               queue.put(path)
        
get_paths_queue(path,queue)


def do_work(path):
    with open(path, 'rb', 0) as file, \
         mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if s.find(b'BAR09-02') != -1:
            print(f'found the drillhole in {path}')
                    
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

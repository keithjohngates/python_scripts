# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:06:05 2018

@author: gatesk
"""



import threading
import time
import os
import multiprocessing as mp

from queue import Queue

root = 'X:\_SS_RELOAD\_converted'
files = os.listdir(r'X:\_SS_RELOAD\_converted')
files  = [os.path.join(root,x) for x in files]

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print ('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed


def do_stuff(q):
  while True: 
    fin  = q.get()
    fin = open(fin,'r')
    x = fin.readlines()
#    print (x[0])
    fin.close()
    q.task_done()


q = Queue(maxsize=0)
num_threads = 10
[q.put(x) for x in files]

@timeit
def queue():
    for i in range(num_threads):
      worker = threading.Thread(target=do_stuff, args=(q,))
      worker.setDaemon(True)
      worker.start()

def read_a_file(fin):
    fin = open(fin,'r')
    fin.readlines()
    fin.close()

@timeit
def main_threaded():
    threads = []
    for f in files:
        t = threading.Thread(target=read_a_file(f))
        threads.append(t)    
    for t in threads:
        t.start()


@timeit
def main_unthreaded():
    for f in files:
        read_a_file(f)
#        
#def gen_rin_list():
#    RINS = []
#    RINSin = open(r"G:\Geosurvey\Shared\CogentII\DATA\DIGS_2018_ORIGINAL_DBSOURCE_FILES\scripts\RIN_LIST.txt", 'r')
#    for line in RINSin:
#        RINS.append(line.rstrip())
#    return RINS


#@timeit
#def multiprocess():
#    # automatically uses mp.cpu_count() as number of workers
#    # mp.cpu_count() is 4 -> use 4 jobs
#    with mp.Pool() as pool:
#        tokens = pool.map(read_a_file, files)
queue()
main_unthreaded()
main_threaded()

#multiprocess()
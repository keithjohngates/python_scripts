# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:07:02 2018

@author: gatesk
"""
import shelve
import matplotlib.pyplot as plt
#
#print ('Reading data')
db =  shelve.open(r"G:\Transit\kgates\DDZ_ASSAY_DH_DRILL_UNIQUE_RINS.db")
#    
##with shelve.open(r"G:\Transit\kgates\checked_dict_RINS.db") as checked_dict:
##    for rin, state in checked_dict.items():
##                rin = input('rin: ?')
##                df = db[rin]
##                dfau = df.loc[df['ELEMENT'] == 'Au']
##                print (dfau[['ELEMENT', 'RESULT', 'UNITS', 'CONV_ELEMENT', 'CONV_RESULT', 'CONV_UNITS', 'HEADING']].describe())
##                print (dfau['CONV_UNITS'].describe())
##                dfau['CONV_RESULT'].plot.hist()
##                plt.show()
#
#import os
#import threading
#from queue import Queue
#import csv
#from itertools import islice
#
#queue = Queue(maxsize=0)
#num_threads = 50
#
#working_folder = r"C:\Users\gatesk\Documents\_downhole_assays_fix\potential_gold_error_rins\\"
#
#'''function to loop through a directory returning the filepaths of contents adding them to a queue'''
#def get_paths_queue(directory, queue):
#   for dirpath,_,filenames in os.walk(directory):
#       for f in filenames:
#           if os.path.splitext(f)[1] == '.txt':
#               path = os.path.abspath(os.path.join(dirpath, f))
#               queue.put(path)
#        
#get_paths_queue(working_folder,queue)
#
#DGFILES = []
#
#def do_work(path):
#    with open(path) as fin:
#        head = list(islice(fin, 50))
#        for line in head:
#            dialect = None
#            if line.startswith('H0202'):
#                try:
#                    dialect = csv.Sniffer().sniff(line, delimiters = '\t,')
#                    if dialect.delimiter == '\t':
#                        delimiter = '\t'
#                    elif dialect.delimiter == ',':
#                        delimiter = ','
#                    else:
#                        delimiter = None
#                except:
#                    pass
#                
#                try:
#                    if line.split(delimiter)[2][:2] == 'DG':
#                        DGFILES.append((path, line.split(delimiter)[2]))
#                        print (line.split(delimiter)[2])
#                        
#                except:
#                    print ('No line found')
#
#
#def do_queued_work(q):
#    while not queue.empty():
#        path =  queue.get()
#        do_work(path)
#        queue.task_done()
#
#
#def main():
#    for i in range(num_threads):
#      worker = threading.Thread(target=do_queued_work, args=(queue,))
#      worker.start()
#
#main()
#print ('Please wait - we are working on it')
#queue.join()

#with shelve.open(r"G:\Transit\kgates\checked_dict_au.db") as checked_au:
#    for i in checked_au:
#        print (i.split('\\')[-2])
#    for i in DGFILES:
#        checked_au[i[0]] = None

import os



with shelve.open(r"G:\Transit\kgates\checked_dict_au.db") as checked_au:
        for idx, i in enumerate(sorted(checked_au)):
#            print (len(checked_au))
            rin = str(i.split('\\')[-2])
#            print (rin)
#            print (i)
            if checked_au[i] == False:
                print (rin)
                print (i)
                os.system("start "+i)
                df = db[rin]
                dfau = df.loc[df['ELEMENT'] == 'Au']
                print (dfau[['ELEMENT', 'RESULT', 'UNITS', 'CONV_ELEMENT', 'CONV_RESULT', 'CONV_UNITS', 'HEADING']].describe())
                print (dfau['CONV_UNITS'].describe())
                dfau['CONV_RESULT'].plot.hist()
#                dfau.to_csv(f'C:\\Users\\gatesk\\Documents\\_downhole_assays_fix\\to_check\\{rin}_dfau.csv')
#                os.system("start "+f'C:\\Users\\gatesk\\Documents\\_downhole_assays_fix\\to_check\\{rin}_dfau.csv')
                plt.show()
                checker = input()
                if checker == "'":
                    checked_au[i] = True # true = its fine
                    os.system("taskkill /f /im  Excel.exe")
                if checker == ";":
                    checked_au[i] = False # false = reload
                    os.system("taskkill /f /im  Excel.exe")
                if checker not in ("'",';'):
                    break
                    















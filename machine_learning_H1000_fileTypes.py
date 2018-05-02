# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 10:34:18 2017

@author: gatesk
"""
import os, random, shutil, time
from textblob.classifiers import NaiveBayesClassifier
import _pickle as pickle
#import multiprocessing as mp

train = open(r"C:\Users\gatesk\Documents\Lithology_files\MRT_TRAINING_NODUPS_BIMODAL_SURFACESAMPLE.csv",'r')
all_training_data = []

for line in train:
    all_training_data.append((str(line.split('|')[1]).replace('\\t',' ').lower(),line.split('|')[0]))

random.shuffle(all_training_data)
train_data = all_training_data[:int((len(all_training_data)+1)*.1)] #Remaining 10% to training set
test_data = all_training_data[int(len(all_training_data)*.1+1):] #Splits 90% data to test set
print (len(train_data))

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts))
        else:
            print ('%r  %2.2f s' % \
                  (method.__name__, (te - ts)))
        return result
    return timed

@timeit
def clasify(data):
    cl = NaiveBayesClassifier(data)
    return cl

cl = clasify(train_data)

'''function taking directory and '''
processing = []

pickle_in = open(r"G:\Geosurvey\Shared\CogentII\DATA\DIGS_2018_ORIGINAL_DBSOURCE_FILES\files_dict.pickle","rb")
fdict = pickle.load(pickle_in)

for key, val in fdict.items():
    headers = fdict[key][2]
    ftype = fdict[key][1]
    print (key, ftype, headers)
    if headers == None and key.endswith(('csv','txt')):
        with open(key,'r')as fin:
            first_line = fin.readline()
            #print (first_line)
            processing.append((str(key), first_line.rstrip().lower().replace('\t', ' ').replace(',', ' ')))


for i in processing:
    print (i)

# def absoluteFilePaths(directory):
#     for dirpath,_,filenames in os.walk(directory):
#         for f in filenames:
#             fpath = os.path.abspath(os.path.join(dirpath, f))
#             fin = open(os.path.abspath(os.path.join(dirpath, f)),'r')
#             for line in fin:
#                 if line.startswith('H1000'):
#                     processing.append((str(fpath),line.rstrip().lower().replace('\t',' ').replace(',',' ')))
#                 if line.startswith('"H1000'):
#                     processing.append((str(fpath),line.rstrip().lower().replace('\t',' ').replace(',',' ')))
#     return processing
#
# '''function taking a line from file and returns a tuple containing the suggested file type and the probabilty'''
# p = absoluteFilePaths(storefolder)
#
# def classify_line(line):
#     prob_dist = cl.prob_classify(line)
#     ftype = prob_dist.max()
#     ftypeprob = round(prob_dist.prob(ftype), 2)
#     #print (ftype,ftypeprob)
#     return ftype,ftypeprob
#
# for i in p:
#     sourcepath = i[0]
#     destpath =  (os.path.join(COPYFOLDER,os.path.basename(i[0])))
#     ftype = classify_line(i[1])[0]
#     if ftype == 'SURFACESamp':
#         shutil.copy(sourcepath,destpath)




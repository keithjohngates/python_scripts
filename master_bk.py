# -*- coding: utf-8 -*-

import csv, os
from collections import defaultdict
from H1000_survey_lk import surveyheaders
import re

rinholes = defaultdict(list)
root = r'C:/Users/gatesk/Documents/missing_/RINS_SEARCH'

with open(r"C:/Users/gatesk/Documents/missing_/RIN_HOLES_MASTER.csv") as master:
    rdr = csv.reader(master, delimiter='|')
    for line in rdr:
        #print (line)
        rin = line[2]
        hole = line[5]
        rinholes[hole].append(rin)

all_rins = set()

for hole,rins in rinholes.items():
    for rin in rins:
        all_rins.add(rin)
        
rinfiles = defaultdict(list)

def findsurveys(fold):
    def absoluteFilePaths(directory):
       for dirpath,_,filenames in os.walk(directory):
           for f in filenames:
               yield os.path.abspath(os.path.join(dirpath, f))
    
    def is_a_survey(headerline):
        elements = re.split('[ \t,]', headerline)
        #if headers suggests it is a survey file
        for e in elements:
           if e in  surveyheaders:
               return True
                
        
    def isH1000(fin):
        with open(fin) as f:
            for idx, line in enumerate(f):
                if idx > 100:
                    break
                if line.startswith('H1000'):
                    return idx,line
                if line.startswith('"H1000'):
                    return idx,line
            return -1, None
    
    surveyfiles = []
    
    for f in absoluteFilePaths(fold):
        ext = os.path.splitext(f)[1]
        if ext not in ['.txt']:
            continue
        idx, line = isH1000(f)
        if idx != -1:
            if is_a_survey(line):
                surveyfiles.append((f,idx,line))
            
    return surveyfiles
        
for rin in all_rins:
    rinfolder = os.path.join(root,rin)
    #print (rinfolder)
    foundsurveys = findsurveys(rinfolder)
    #print (rin,len(foundsurveys))
    print (rin,foundsurveys)





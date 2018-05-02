# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:46:06 2017

@author: gatesk
"""
import os
import re

getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
searchdir = r'C:\Users\gatesk\Documents\missing_\RINS_SEARCH'

'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())
    
surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'w')

'''get the lines from survey files'''
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))
           
for i in absoluteFilePaths(searchdir):
    try:
        if 'urv' in str(i):
            with open(i) as f:
                for line in f:
                    surveyfilemerge.write(line)
    except:
        pass
surveyfilemerge.close()
        

surveyfilemerge = open(r"C:\Users\gatesk\Documents\missing_\survey_merge.txt",'r')
getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
lines = set()

for line in surveyfilemerge:
    lineelements = re.split('[ \t,]',line)
    print (lineelements)
    for fn in HOLEIDS:
        if str(fn) in lineelements:
            #print (str(fn) +' '+ str(line))
            lines.add(line)
            
for i in lines:
    getlines.write(str(i))
    
getlines.close()
surveyfilemerge.close()

#for i in absoluteFilePaths(searchdir):
#    try:
#        #print (i)
#        if 'urv' in str(i):
#            for fn in HOLEIDS:
#                if str(fn) in open(i).read():
#                    print("This survey file has the hole you are looking for: " + str(i))
#                    #os.startfile((i),'open')
#                    with open(i) as f:
#                        for line in f:
#                            lineelements = re.split('[ \t,]',line)
#                            if 'H1000' in line:
#                                getlines.write(line +'|'+str(i))
#                            if str(fn) in lineelements:
#                                print (str(fn) +' '+ str(line))
#                                getlines.write(line+'|'+str(fn))
#    except:
#        pass
#getlines.close()
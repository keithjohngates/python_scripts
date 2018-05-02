d# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:29:53 2017

@author: gatesk
"""
from os import walk
import os
import fileinput

f = []
for (dirpath, dirnames, filenames) in walk(r"\\maitprodgi\Digsdata\KJG\\"):
    f.extend(filenames)
    break



for i in f:
    print (i)
    '''open all the files'''
    os.startfile((r'\\maitprodgi\Digsdata\KJG\\'+str(i)),'open')
    
    '''infile replacement'''
    #for line in fileinput.input('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i), inplace = 1): 
    #    print (line.replace("|", "\t").rstrip().replace("Au_ppm", "Au").rstrip().replace("Au_ppb", "Au").rstrip().replace("Mo_ppm", "Mo").rstrip().replace("As_ppm", "As").rstrip().replace("Cu_ppm", "Cu").rstrip().replace("Zn_ppm", "Zn").rstrip().replace("Pb_ppm", "Pb").rstrip().replace("Bi_ppm", "Bi").rstrip().replace("Ag_ppm", "Ag").rstrip().replace("AuR_ppm", "Au").replace("AuR2_ppm", "Au").replace("AuR_ppb", "Au").replace("AuR2_ppb", "Au").replace("Bi_pmm", "Bi").replace("Mo_pmm", "Mo").replace("pmm", "ppm").replace("SAMPLE_NO", "SAMPLE_ID").replace("Au.1", "Au").replace("ppm.1", "ppm").replace("Au.2", "Au").replace("ppm.2", "ppm"))

    '''print a specific line in a file'''
    #fo = open('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\new\\'+str(i), "r")
    #line = fo.readlines()
    #print (line[25])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
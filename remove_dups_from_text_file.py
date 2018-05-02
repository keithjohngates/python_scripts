# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:59:10 2017

@author: gatesk
"""

lines = open(r"C:\Users\gatesk\Documents\Lithology_files\MRT_TRAINING.csv", 'r').readlines()

lines_set = set(lines)

out  = open(r"C:\Users\gatesk\Documents\Lithology_files\MRT_TRAINING_NODUPS.csv", 'w')

for line in lines_set:
    out.write(line)
    

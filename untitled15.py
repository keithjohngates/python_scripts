# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:27:56 2017

@author: gatesk
"""
import csv

def detect_delimter(fin): 
    with open(fin, 'r') as f:
        dialect = csv.Sniffer().sniff(f.read())    
    return dialect.delimiter

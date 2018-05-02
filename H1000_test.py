# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 09:07:33 2018

@author: gatesk
"""

import os
import csv
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt, mpld3
import sys
import collections
from valid_H1000_conversion import *

outfile = open(r'C:\Users\gatesk\Documents\SURFACE_SAMPLE_ASSAY_VALUE_ERRORS\test_H1000.txt','w')

def line_generator(filepath):
    with open(filepath) as fin:
        for line in fin:
            yield line

def detect_delimter(fin):
    '''
    Input: a filepath
    Output: the file's delimiter
    '''
    try:
        with open(fin, 'r') as f:
            dialect = csv.Sniffer().sniff(f.readline())
            if dialect.delimiter == ',':
                delimiter = ','
                return delimiter
            if dialect.delimiter == '\t':
                delimiter = '\t'
                return delimiter
            else:
                delimiter = 'unk'
                return delimiter
            
    except Exception as e:
        print (e, 'on %s' %fin)
        delimiter = 'error'
        return delimiter
    
    
def get_headers(line,delimiter,headers):
    '''
    Input: an open file, delimiter of the file, key header list
    Output: list of headers within the file
    '''
#    for line in fin:
    if line.startswith('H'):
        headers.add(line.split(delimiter)[0])
    return headers

def generate_H1000lk():
    H1000lk = dict()
    with open(r"C:\Users\gatesk\Documents\SURFACE_SAMPLE_ASSAY_VALUE_ERRORS\H1000set_CONVERSIONS.csv",'r') as fin:
        for line in fin:
            items = line.split(',')
            H1000lk[items[0]] = items[1:]
    return H1000lk

H1000lk = generate_H1000lk()


def fix_H1000(H1000s,H1000fix,H1000lk):
    for i in H1000s:
        H1000fix.append((H1000lk[i.strip()][0],H1000lk[i.strip()][1],H1000lk[i.strip()][2].strip()))
    return H1000fix

def H1000f(line,headers,delimiter,H1000):
    if 'H1000' in headers:
        if line.startswith('H1000'):
            try:
                for i in line.split(delimiter):
                    H1000.append(i)
            except:
                pass
        return H1000

def H1001f(line,headers,delimiter,H1001):
    if 'H1000' in headers:
        if 'H1001' in headers:
            if line.startswith('H1001'):
                try:
                    for i in line.split(delimiter):
                        if len(i) == '':
                            H1001.append('unk')
                        elif len(i) != '':
                            H1001.append(i.strip())
                except:
                    pass
        return H1001

def H1002f(line,headers,delimiter,H1002):
    if 'H1002' in headers:
        if line.startswith('H1002'):
            try:
                for i in line.split(delimiter):
                    H1002.append(i.strip())
            except:
                pass
        return H1002
    
def H1003f(line,headers,delimiter,H1003):
    if 'H1003' in headers:
        if line.startswith('H1003'):
            try:
                for i in line.split(delimiter):
                    H1003.append(i.strip())
            except:
                pass
        return H1003

def main():
    path = "X:\_SS_RELOAD\PENDING"
    folders = os.listdir(path)
    
    for folder in folders:    
        print (folder)
        rinfiles = os.listdir(os.path.join(path,folder))
        for file in rinfiles:
            
            filepath = os.path.join(os.path.join(path,folder),file)
            delimiter = detect_delimter(filepath)
            
            if delimiter == 'unk' or delimiter == 'error' :
                (print("Delimiter is not tab or csv - Manually examine the file"))
                sys.exit()
                
            H1000 = []
            H1000fix = []
            H1001 = []
            H1002 = []
            headers = set()
            
            for line in line_generator(filepath):
                headers = get_headers(line,delimiter,headers)
                
                
                H1000s = H1000f(line,headers,delimiter,H1000)
                H1001s = H1001f(line,headers,delimiter,H1001)
                H1002s = H1002f(line,headers,delimiter,H1002)
            
            check_H1000lk(H1000s,H1000lk)
            
            if 'H1000' in headers:
                H1000fixed = fix_H1000(H1000s,H1000fix,H1000lk)

            if 'H1000' not in headers:
                print ('No H1000 field')
                #sys.exit()
            
            if 'H1001' in headers and 'H1002' in headers:
                headersdict = dict()
                for idx, column in enumerate(H1000):
                    headersdict[column] = H1000fixed[idx],H1001[idx],H1002[idx]
                    if H1001[idx] == None:
                        H1001[idx] = 'unk'
                    if H1002[idx] == None:
                        H1002[idx] = 'unk'
            
            if 'H1001' in headers and 'H1002' not in headers:
                for idx, column in enumerate(H1000):
                    headersdict[column] = H1000fixed[idx],H1001[idx],'unk'
                    if H1001[idx] == None:
                        H1001[idx] = 'unk'
                    if H1002[idx] == None:
                        H1002[idx] = 'unk'
            
            if 'H1001' not in headers and 'H1002' not in headers:
                for idx, column in enumerate(H1000):
                    headersdict[column] = H1000fixed[idx],'unk','unk'
                    
            H1000convert = []
            for item in H1000fixed:
                H1000convert.append(item[0].strip())
                H1000convertline =  str(delimiter.join(H1000convert))
            
            H1001new = []
            for item in H1000s:
                H1001new.append(headersdict[item][0][1])
            H1001new[0] = 'H1001'
            H1001new[1] = 'UNITS'
            H1001newline =  str(delimiter.join(H1001new))
            
            H1002new = []
            for item in H1000s:
                H1002new.append(headersdict[item][0][2])
            H1002new[0] = 'H1002'
            H1002new[1] = 'ASSAY_CODE'
            H1002newline =  str(delimiter.join(H1002new))
            
            H1000s_line = delimiter.join(H1000s)
            H1001s_line = delimiter.join(H1001s)
            
            if 'H1002' in headers:
                H1002s_line = delimiter.join(H1002s)
            else:
                pass
            
            outfile.write(H1000s_line)
            outfile.write(H1000convertline+'\n')
            
            if "H1001" in headers:
                outfile.write(H1001s_line+'\n')
            else:
                pass
            
            outfile.write(H1001newline+'\n')
            
            if 'H1002' in headers:
                outfile.write(H1002s_line+'\n')
            else:
                pass
            
            outfile.write(H1002newline+'\n')
                
main()
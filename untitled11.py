# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 08:02:38 2018

@author: gatesk
"""
with open(r"H:\FILE_VALIDATION\sample_types_lk_v2.csv",'w') as fout:
    with open(r"H:\FILE_VALIDATION\sample_types_lk.csv",'r') as fin:
        for line in fin:
            fout.write(line.lower())
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:30:34 2018

@author: gatesk
"""

import csv

class FileReader(object):
    def __init__(self,filepath):
        self.filepath = filepath
        self.delimiter = self.get_file_delimiters(filepath)
        self.headers = self.get_file_headers(filepath)
        self.headers_dict = self.get_file_headers_dict(filepath)
        self.d, self.d_len_set = self.get_data_lines(filepath)
        self.filedict = self.build_file_dict()


    def get_file_delimiters(self,filepath):
        with open(filepath,'r') as fin:
            line = fin.readline()
            dialect = csv.Sniffer().sniff(line,delimiters = '\t,')
            if dialect.delimiter == '\t':
                self.delimiters = '\t'
            elif dialect.delimiter == ',':
                self.delimiters = ','
            else:
                self.delimiters = 'unk'
        return self.delimiters


    def get_file_headers(self,filepath):
        self.headers = []
        with open(filepath,'r') as fin:
            lines = fin.readlines()
            for line in lines:
                if line.startswith('H'):
                    H = line.split(self.delimiters)
                    self.headers.append(H[0])

        return self.headers


    def get_file_headers_dict(self,filepath):
        self.headers_dict = dict()
        with open(filepath,'r') as fin:
            lines = fin.readlines()
            for line in lines:
                if line.startswith('H'):
                    line = line.rstrip('\n').rstrip(self.delimiters)
                    self.H_dict_key = line.split(self.delimiters)[0]
                    self.H_dict_value = line.split(self.delimiters)[1:]
                    self.headers_dict[self.H_dict_key] = self.H_dict_value
        return self.headers_dict


    def get_data_lines(self,filepath):
        self.data_lines = []
        self.data_lines_len_set = set()
        with open(filepath,'r') as fin:
            lines = fin.readlines()
            for line in lines:
                if line.startswith('D'):            
                    line = line.rstrip('\n').rstrip(self.delimiters)
                    line = line.split(self.delimiters)
                    self.data_lines.append(line)
                    self.data_lines_len_set.add(len(line))
        return self.data_lines, self.data_lines_len_set
    
    
    def build_file_dict(self):
        self.fdict = dict()
        self.fdict = {
                  'headers'      : self.headers,
                  'headers_dict' : self.headers_dict,                      
                  'delimiter'    : self.delimiters,
                  'dlines'       : self.data_lines,
                  'dlines_set'   : self.data_lines_len_set
                  }
        return self.fdict
    
    
    
    
    
    
    
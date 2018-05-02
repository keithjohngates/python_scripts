# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:12:02 2018

@author: dell
"""
import os
import csv
import pandas as pd
import pyodbc

dbconnection_string = r'DSN=GEODWH;UID=gatesk;PWD=Oldsp00n'
rootpath = r'X:\_SS_RELOAD\PENDING\R00029160'

class DatabaseConnection(object):
    def __init__(self,dbconn,RIN):
        self.dbconn = dbconn
        self.conn = pyodbc.connect(self.dbconn)
        self.sqlGET_DD_RPT_GENERAL = "SELECT * FROM GEODWH.dbo.DD_RPT_GENERAL"
        self.sqlGET_DD_RPT_FILE = "SELECT * FROM GEODWH.dbo.DD_RPT_FILE"
        self.RIN = RIN
        
    def connect(self):
        self.DD_RPT_GENERAL = pd.read_sql(self.sqlGET_DD_RPT_GENERAL,self.conn) 
        self.DD_RPT_FILE = pd.read_sql(self.sqlGET_DD_RPT_FILE,self.conn)    
        return self.DD_RPT_GENERAL, self.DD_RPT_FILE
        
    def RPT_GENERAL(self):
        self.df = self.DD_RPT_GENERAL.loc[self.DD_RPT_GENERAL['RIN'] == self.RIN]
        self.df = self.df.reset_index()
        self.RPT_ID = self.df['RPT_ID'][0]
        return (self.df['RPT_ID'][0],self.df['PERIODEND'][0],self.df['TENEMENT'][0],self.df['COUNT_SF_SAMP'][0],self.df['RPT_CODE'][0],self.df['RPT_TYPE'][0],self.df['HOLDER'][0],self.df['PROJNAME'][0])
    
    def RPT_FILE(self):
        self.df = pd.DataFrame(self.DD_RPT_FILE.loc[self.DD_RPT_FILE['RPT_ID'] == self.RPT_ID])
        self.dfSS = self.df.loc[self.df['FILETYPE'] == 'SGC']
        return len(self.dfSS)

class FileReader(object):
    def __init__(self,folderpath):
        
        self.folderpath = folderpath
        self.files = self.get_file_names()
        self.fpaths = self.get_file_paths()
        self.delimiter = self.get_file_delimiters()
        self.headers = self.get_file_headers()
        self.headers_dict = self.get_file_headers_dict()
        self.d, self.d_len_set = self.get_data_lines()
        self.filedict = self.build_file_dict()

    def get_file_names(self):
        return os.listdir(self.folderpath)
        
    def get_file_paths(self):
        self.filepaths = []
        for f in self.files:
            self.filepaths.append(os.path.join(self.folderpath,f))
        return self.filepaths

    def get_file_delimiters(self):
        self.delimiters = []
        for f in self.fpaths:
            with open(f,'r') as fin:
                line = fin.readline()
                dialect = csv.Sniffer().sniff(line,delimiters = '\t,')
                if dialect.delimiter == '\t':
                    self.delimiters.append('\t')
                elif dialect.delimiter == ',':
                    self.delimiters.append(',')
                else:
                    self.delimiters.append('unk')
        return self.delimiters
    
    def get_file_headers(self):
        self.headers = []
        for idx, f in enumerate(self.fpaths):
            self.fheaders = []
            with open(f,'r') as fin:
                lines = fin.readlines()
                for line in lines:
                    if line.startswith('H'):
                        H = line.split(self.delimiters[idx])
                        self.fheaders.append(H[0])
            self.headers.append(self.fheaders)
        return self.headers

    def get_file_headers_dict(self):
        self.headers_dict = []
        for idx, f in enumerate(self.fpaths):
            self.fheaders_dict = dict()
            with open(f,'r') as fin:
                lines = fin.readlines()
                for line in lines:
                    if line.startswith('H'):
                        line = line.rstrip('\n').rstrip(self.delimiters[idx])
                        self.H_dict_key = line.split(self.delimiters[idx])[0]
                        self.H_dict_value = line.split(self.delimiters[idx])[1:]
                        self.fheaders_dict[self.H_dict_key] = self.H_dict_value
            self.headers_dict.append(self.fheaders_dict)
        return self.headers_dict

    def get_data_lines(self):
        self.data_lines = []
        self.data_lines_len_set = []
        for idx, f in enumerate(self.fpaths):
            self.fdata_lines = []
            self.fdata_lines_len_set = set()
            with open(f,'r') as fin:
                lines = fin.readlines()
                for line in lines:
                    if line.startswith('D'):            
                        line = line.rstrip('\n').rstrip(self.delimiters[idx])
                        line = line.split(self.delimiters[idx])
                        self.fdata_lines.append(line)
                        self.fdata_lines_len_set.add(len(line))
            self.data_lines_len_set.append(self.fdata_lines_len_set)          
            self.data_lines.append(self.fdata_lines)
        return self.data_lines, self.data_lines_len_set
    
    def build_file_dict(self):
        self.fdict = dict()
        for idx, f in enumerate(self.files):
            self.fdict[f] = {
                      'fpath' : self.fpaths[idx],
                      'headers'      : self.headers[idx],
                      'headers_dict' : self.headers_dict[idx],                      
                      'delimiter'    : self.delimiters[idx],
                      'dlines'       : self.data_lines[idx],
                      'dlines_set'   : self.data_lines_len_set[idx]
                      }
        return self.fdict
    
class ReportErrors(object):
    def __init__(self,fdict):
        self.fdict = fdict
        pass

    def data_len_check(self):
        for k,v in self.fdict.items():
#            print (self.fdict[k]['fpath'])
#            print (self.fdict[k]['delimiter'])
            self.h1000_len =  (len(self.fdict[k]['headers_dict']['H1000'])+1)
            self.dlines_set_count =  self.fdict[k]['dlines_set']

            if len(self.dlines_set_count) != 1:
                print ('Failed: Data lines have inconsistent lengths : %s' % str(self.dlines_set_count))
            if len(self.dlines_set_count) == 1:
                print ("Passed: All data lines have consistent lengths")
                
            if len(self.dlines_set_count) == 1:
                if list(self.dlines_set_count)[0] != self.h1000_len:
                    print ('Failed: H1000 (%s) and data lines (%s) have inconsistent lengths '% (self.h1000_len, self.dlines_set_count))
                else:
                    print ("Passed: H1000 and data lines have consistent lengths")
            




demo = FileReader(rootpath)
validation = ReportErrors(demo.build_file_dict())
print (validation.data_len_check())
#validation.dline_count()

#for k,v in demo.fdict.items():
#    print (demo.fdict[k]['fpath'])
#    print (demo.fdict[k]['delimiter'])
#    print (demo.fdict[k]['headers_dict']['H1000'])
#    print (demo.fdict[k]['dlines_set'])
#    print (demo.fdict[k]['dlines'])
#    

        
#   print (demo.fdict[k]['h1000'])
#    print (demo.fdict[k]['h1000len'])
#    print (demo.fdict[k]['dlines_set'])
#   print (demo.fdict[k]['dlines'][0])
#    pass

#class FileInterogation(self):
#    def __init__(self,filedict):
#        pass
#    
#    def plot_statistics(self):
#        pass
#    
#    def plot_geochemistry(self):
#        pass
#    
#    def plot_spatially(self):
#        pass

#    def build_pandas_data_df(self):
#        self.pandas_df = []
#        for idx, f in enumerate(self.fpaths):
#            columns = (self.h1000_row[idx])
#            self.dataframe = pd.DataFrame(columns = columns)
            #print (list(self.dataframe))
#            for row in self.data_lines[idx][0]:
#                print (row)
#                self.dataframe.loc[len(self.dataframe)] = row
#            self.pandas_df.append(self.dataframe)
#        return self.pandas_df
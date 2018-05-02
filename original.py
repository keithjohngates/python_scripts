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
    def __init__(self,dbconn,rin):
        self.dbconn = dbconn
        self.conn = pyodbc.connect(self.dbconn)
        self.sql_dd_rpt_general = "SELECT * FROM GEODWH.dbo.DD_RPT_GENERAL"
        self.sql_dd_rpt_file = "SELECT * FROM GEODWH.dbo.DD_RPT_FILE"
        self.rin = rin
        
    def connect(self):
        self.dd_rpt_general = pd.read_sql(self.sql_dd_rpt_general,self.conn) 
        self.dd_rpt_file = pd.read_sql(self.sql_dd_rpt_file,self.conn)    
        return self.dd_rpt_general, self.dd_rpt_file
        
    def rpt_general(self):
        self.df = self.dd_rpt_general.loc[self.dd_rpt_general['RIN'] == self.rin]
        self.df = self.df.reset_index()
        self.rpt_id = self.df['RPT_ID'][0]
        return (self.df['RPT_ID'][0],self.df['PERIODEND'][0],self.df['TENEMENT'][0],self.df['COUNT_SF_SAMP'][0],self.df['RPT_CODE'][0],self.df['RPT_TYPE'][0],self.df['HOLDER'][0],self.df['PROJNAME'][0])
    
    def rpt_file(self):
        self.df = pd.DataFrame(self.dd_rpt_file.loc[self.dd_rpt_file['RPT_ID'] == self.rpt_id])
        self.dfss = self.df.loc[self.df['FILETYPE'] == 'SGC']
        return self.dfss

class FolderReader(object):
    def __init__(self,folderpath):
        self.folderpath = folderpath
        self.rin = self.get_rin()
        self.files = self.get_file_names()
        self.fpaths = self.get_file_paths()

    def get_rin(self):
        return os.path.split(self.folderpath)[1]
    
    def get_file_names(self):
        return os.listdir(self.folderpath)
         
    def get_file_paths(self):
        self.filepaths = []
        for f in self.files:
            self.filepaths.append(os.path.join(self.folderpath,f))
        return self.filepaths
        
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

class ReportErrors(object):
    def __init__(self,fdict,filepath):
        self.validation_status = True
        self.filepath = filepath
        self.fdict = fdict
        
    def run(self):
        print ("Validating %s" % self.filepath)
        errors = []
        errors.extend(self.data_len_check())
        errors.extend(self.data_key_header_check())
        
        return errors
#        self.data_len_chk = self.data_len_check(self.fdict)
#        self.data_key_header_chk = self.data_key_header_check(fdict)
    
    def data_len_check(self):
        self.len_H1000_line = len(self.fdict['headers_dict']['H1000'])
        self.len_d_lines = len(self.fdict['dlines_set'])
        self.len_d_lines_set = self.fdict['dlines_set']
        errors = []
        
        if self.len_d_lines == 0:
            errors.append('Failed: No D lines are present')
            self.validation_status = False
            
        elif self.len_d_lines > 1:
            errors.append('Failed: Data lines have inconsistent lengths : %s' % str(self.len_d_lines))
            self.validation_status = False
                                
        elif self.len_d_lines == 1:
            print("Passed: All data lines have consistent lengths")
            
        else:
            errors.append("Failed: Some other reason")
            self.validation_status = False
            
        if self.len_d_lines == 1:
            if list(self.len_d_lines_set)[0]-1 != self.len_H1000_line:
                errors.append('Failed: H1000 (%s) and data lines (%s) have inconsistent lengths '% (self.len_H1000_line, list(self.len_d_lines_set)[0]-1))
                self.validation_status = False
            else:
                print("Passed: H1000 and data lines have consistent lengths")
                
        return errors

    def data_key_header_check(self):
        self.h1000_headers = self.fdict['headers']
        errors = []
        
        headerrepeat_check = len(self.h1000_headers) - len(set(self.h1000_headers))
        
        if headerrepeat_check != 0:
            errors.append("Failed: Some headers are repeated")
            self.validation_status = False
            
        if headerrepeat_check == 0:
            print ("Passed: No headers are repeated")

        return errors

files_in_rin = FolderReader(rootpath)

for file in files_in_rin.fpaths:
    fdict = FileReader(file).fdict
    validator = ReportErrors(fdict,file)
    
    errors = validator.run()
    print (errors)
    
    if validator.validation_status:
        print ("PASSED")
    else:
        print ("FAILED")

#    print(fdict['headers'])
#    print (FileReader(file).headers)
#    print (len(FileReader(file).headers_dict['H1000']))
#    print (FileReader(file).delimiters)
#    print (FileReader(file).data_lines)
#    print (FileReader(file).data_lines_len_set)
#    print (ReportErrors(file).data_len_chk)
    

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:28:12 2018

@author: gatesk
"""

import pyodbc
import pandas as pd

class DatabaseConnection(object):
    def __init__(self,dbconn,rin,delimiter):
        self.dbconn = dbconn
        self.delimiter = delimiter
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
    
    #for surface samples
#    def rpt_file(self):
#        self.df = pd.DataFrame(self.dd_rpt_file.loc[self.dd_rpt_file['RPT_ID'] == self.rpt_id])
#        self.dfss = self.df.loc[self.df['FILETYPE'] == 'SGC']
#        return self.dfss
    
    #for DGC samples
    def rpt_file(self):
        self.df = pd.DataFrame(self.dd_rpt_file.loc[self.dd_rpt_file['RPT_ID'] == self.rpt_id])
        self.dfss = self.df.loc[self.df['FILETYPE'] == 'DGC']
        return self.dfss
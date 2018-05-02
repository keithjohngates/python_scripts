# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 09:27:13 2018

@author: gatesk
"""
import csv
import pandas as pd
import pyodbc

reader = csv.reader(open(r"C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\RIN_UPDATE_RECORD.csv",'r'))    
dbconnection_string = r'DSN=GEODWH;UID=gatesk;PWD=Oldsp00n'

 
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
        return(self.df['COUNT_DH_SAMP'][0])
#        return (self.df['RPT_ID'][0],self.df['PERIODEND'][0],self.df['TENEMENT'][0],self.df['COUNT_SF_SAMP'][0],self.df['RPT_CODE'][0],self.df['RPT_TYPE'][0],self.df['HOLDER'][0],self.df['PROJNAME'][0])
    
class GatherDatabaseData(object):
    def __init__(self, dbconn, rin):
        self.dbconn = dbconn
        self.rin = rin
        dbconn = DatabaseConnection(self.dbconn, self.rin)
        dbconn.connect()
        self.rpt_general = dbconn.rpt_general()
        
    def current_database_lengths(self):
        sample_count_db = self.rpt_general[0]        
        print ('sample_count_db: ', sample_count_db)
        return sample_count_db



with open(r"C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix\RIN_UPDATE_RECORD_DB.csv",'w') as fout:
    for row in reader:
        try:
            count = GatherDatabaseData(dbconnection_string,row[0])
            print (count.rin)
            print (count.rpt_general)
            fout.write(','.join(row).strip()+','+str(count.rpt_general)+'\n')
        except Exception as e:
            print (e)
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:35:34 2018

@author: gatesk
"""
import time
import pyodbc
import pandas as pd
import threading
from queue import Queue
import shelve

rinsdatadict = dict()
q = Queue(maxsize=0)
num_threads = 10
dbconnection_string = r'DSN=GEODWH;UID=gatesk;PWD=Oldsp00n'

class DatabaseConnection(object):

    def __init__(self,dbconn,selectsql):
        self.dbconn = dbconn
        self.selectsql = "SELECT * FROM GEODWH.dbo.DDZ_ASSAY_DH_DRILL WHERE RIN = '%s'" % selectsql
        
    def connect(self):
        self.conn = pyodbc.connect(self.dbconn)
        
    def make_df(self):
        t1 = time.time()
        self.dh_assays = pd.read_sql(self.selectsql,self.conn)
        t2 =  time.time() - t1
        print (t2)
    
    def discon(self):
        self.conn.close()

dh_jobs = {}
print ('opening shelve')
with shelve.open(r"G:\Transit\kgates\DDZ_ASSAY_DH_DRILL_UNIQUE_RINS.db") as db:
    
    print ('shelve opened')
    with open(r"G:\Transit\kgates\DDZ_ASSAY_DH_DRILL_UNIQUE_RINS.csv") as rins:
        for idx, line in enumerate(rins):
            rin = line.strip().strip('"')
            if rin not in db:
                print (f'checking {rin}')
                rindf = DatabaseConnection(dbconnection_string, rin) 
                dh_jobs[rin] = rindf
                q.put(rindf)
            else:
                print (f'shelf contains {rin}')
          
def make_df(q):
  while not q.empty():
    dbconn =  q.get()
    dbconn.connect()
    dbconn.make_df()
    dbconn.discon()
    q.task_done()

def main():
    for i in range(num_threads):
      worker = threading.Thread(target=make_df, args=(q,))
#      worker.setDaemon(True)
      worker.start()

main()
print ('Please wait - we are working on it')
q.join()

with shelve.open(r"G:\Transit\kgates\DDZ_ASSAY_DH_DRILL_UNIQUE_RINS.db") as db:
    for rin, df in dh_jobs.items():
        db[rin] = df.dh_assays

print ('Completed - thank you for your patience')


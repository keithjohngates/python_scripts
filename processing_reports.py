# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 08:01:03 2018

@author: gatesk
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:12:02 2018

@author: dell
"""
import os
from valid_H1000_conversion import dbconnection_string
import pyodbc
import pandas as pd
import csv

rootpath = r'C:\Users\dell\Downloads\download\a61566\Unzip\Data\Data\Drilling and Results'

def connect(dbconnection_string = dbconnection_string):        
    conn = pyodbc.connect(dbconnection_string)    
    sqlGET_DD_RPT_GENERAL = "SELECT * FROM GEODWH.dbo.DD_RPT_GENERAL"
    sqlGET_DD_RPT_FILE = "SELECT * FROM GEODWH.dbo.DD_RPT_FILE" 
    DD_RPT_GENERAL = pd.read_sql(sqlGET_DD_RPT_GENERAL,conn) 
    DD_RPT_FILE = pd.read_sql(sqlGET_DD_RPT_FILE,conn)    
    return DD_RPT_GENERAL, DD_RPT_FILE

def RPT_GENERAL(RIN,DD_RPT_GENERAL):
    df = DD_RPT_GENERAL.loc[DD_RPT_GENERAL['RIN'] == RIN]
    df = df.reset_index()
    return (df['RPT_ID'][0],df['PERIODEND'][0],df['TENEMENT'][0],df['COUNT_SF_SAMP'][0],df['RPT_CODE'][0],df['RPT_TYPE'][0],df['HOLDER'][0],df['PROJNAME'][0])

def RPT_FILE(RPT_ID,DD_RPT_FILE):
    df = pd.DataFrame(DD_RPT_FILE.loc[DD_RPT_FILE['RPT_ID'] == RPT_ID])
    dfSS = df.loc[df['FILETYPE'] == 'SGC'] #SG%
    return len(dfSS)

class FolderReader(object):
    '''
    '''
    def __init__(self,folderpath):
        self.folderpath = folderpath
        self.filelist = self.filelist()
        self.filecount = self.filecount()
        self.rin = self.rin()
        
    def rin(self):
        return os.path.split(self.folderpath)[1]
        
    def filelist(self):
        return os.listdir(self.folderpath)
    
    def filecount(self):
        return len(os.listdir(self.folderpath))
    
class FileReader(FolderReader):
    '''
    '''
    def __init__(self,folderpath):
        super(FileReader,self).__init__(folderpath)
        self.fullpaths = self.fullpaths()
        
    def fullpaths(self):
        self.paths = []
        for f in self.filelist:
            path = os.path.join(self.folderpath,f)
            self.paths.append(path)
            #self.fullpaths = [].append(os.path.join(self.folderpath,f))
        return self.paths
  
def detect_delimter(fin):
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
        print (e, 'on %s' % fin)
        delimiter = 'error'
        return delimiter

def readlines(filepath):
    with open(filepath,'r') as f:
        for line in f:
            yield line

def count_all_the_Ds(files):
    total_D_count = 0
    for file in files:
        with open(file,'r') as fin:
            for line in fin:
                if line.startswith('D') or line.startswith('"D"'):
                    total_D_count = total_D_count + 1
    return total_D_count

def H05_lines_reader(readlines_generator_function):
    H05 = False
    H05_lines = []
    for line in readlines_generator_function:
        if line.startswith('H05'):
            H05 = True
            H05_lines.append(line)
    if H05 == False:
        H05_lines = ['H05 lines do not exist']
    return H05, H05_lines

def H06_lines_reader(readlines_generator_function):
    H06 = False
    H06_lines = [] 
    for line in readlines_generator_function:
        if line.startswith('H06'):
            H06 = True
            H06_lines.append(line)
    if H06 == False:
        H06_lines = ['H06 lines do not exist']
    return H06, H06_lines

def H08_lines_reader(readlines_generator_function):
    H08 = False
    H08_lines = []
    for line in readlines_generator_function:
        if line.startswith('H08'):
            H08 = True
            H08_lines.append(line)
    if H08 == False:
        H08_lines = ['H08 lines do not exist']
    return H08, H08_lines

def H1_lines_reader(readlines_generator_function):
    H1 = False
    H1_lines = []
    for line in readlines_generator_function:
        if line.startswith('H1'):
            H1 = True
            H1_lines.append(line)
    if H1 == False:
        H1_lines = ['H1 lines do not exist']
    return H1, H1_lines

def guess_zone(H05_fields):
    validzones = ['54','55','56','57']
    for item in H05_fields:
        for zone in validzones:
            if (str(item)).find(zone) == -1:
                return zone
                break
            else:
                return 'unk_zone'

def guess_geodetic(H05_fields):
    validdatums = ['GDA','AGD','MGA','AMG']
    for item in H05_fields:
        for datum in validdatums:
            if (str(item)).find(datum) == -1:
                if datum == 'MGA':
                    return 'GDA'
                if datum == 'AMG':
                    return 'AGD'
                return datum
            else:
                return 'unk_datum'
            
def pivot_H06(H06):
    H06_headers = []
    for line in H06:
        line = line.split(delimiter)
        if line[0] == 'H0600':
            H06_headers.append('H0600 : %s' % line[1])
        if line[0] == 'H0601':
            H06_headers.append('H0601 : %s' % line[1])
        if line[0] == 'H0602':
            H06_headers.append('H0602 : %s' % line[1])
    return H06_headers

def pivot_H08(H08):
    H08_headers = []
    for line in H08:
        line = line.split(delimiter)
        if line[0] == 'H0800':
            H08_headers.append('H0800 : %s' % line[1])
        if line[0] == 'H0801':
            H08_headers.append('H0801 : %s' % line[1])
        if line[0] == 'H0802':
            H08_headers.append('H0802 : %s' % line[1])
    return H08_headers

RPTGENERAL = connect(dbconnection_string)[0]
RPTFILE = connect(dbconnection_string)[1]

x = FileReader(r"X:\_SS_RELOAD\PENDING\RE0006488")
 
rpt_details = RPT_GENERAL(x.rin,RPTGENERAL)
RPTID = rpt_details[0]
db_SS_file_count = RPT_FILE(RPTID,RPTFILE)
db_SS_count = rpt_details[3]
rin_SS_count = count_all_the_Ds(x.fullpaths)

print ('rin : %s' % x.rin) 
print ('count of files in database : %s' % db_SS_file_count)
print ('count of files in rin      : %s' % len(x.fullpaths))
#warning for file count mismatches
print ('count of surfacesamples in database : %s' % db_SS_count)
print ('count of surfacesamples in rin      : %s' % rin_SS_count)
#warning for ss count mismatches

for file in x.fullpaths:
    delimiter = detect_delimter(file)
#    print ('file : %s' % file)
#    print ('delimiter : %s' % delimiter)
    H0002_line = delimiter.join(['H0002','version',rpt_details[5]])
    H0004_line = delimiter.join(['H0004', 'reporting_end_date',rpt_details[1]])
    H0100_line = delimiter.join(['H0100', 'tenement',rpt_details[2].split(',')[0]])
    H0101_line = delimiter.join(['H0101', 'tenement_holder',rpt_details[6]])
    H0102_line = delimiter.join(['H0102', 'project_name',rpt_details[7]])
    H0202_line = delimiter.join(['H0202', 'template_format','SGC'])    

    H05 =  H05_lines_reader(readlines(file))
    H0501_line = delimiter.join(['H0501', 'geodetic_datum',guess_geodetic(H05)])
    H0531_line = delimiter.join(['H0531', 'projection_zone',guess_zone(H05)])
     
    H06 =  H06_lines_reader(readlines(file))
    H06_pivoted = pivot_H06(H06[1])
    

    H08 =  H08_lines_reader(readlines(file))
    H08_pivoted = pivot_H08(H08[1])
    
    print (H0002_line)
    print (H0004_line)
    print (H0100_line)
    print (H0102_line)
    print (H0202_line)
    print (H0501_line)
    print (H0531_line)
    
    print (H06_pivoted)
    print (H06[1])
    print (H08_pivoted)
    print (H08[1])
    
#    H1  =  H1_lines_reader(readlines(file))















            
def generate_H1000lk():
    H1000lk = dict()
    with open(r"C:\Users\gatesk\Documents\SURFACE_SAMPLE_ASSAY_VALUE_ERRORS\H1000set_CONVERSIONS.csv",'r') as fin:
        for line in fin:
            items = line.split(',')
            H1000lk[items[0]] = items[1:]
    return H1000lk

H1000lk = generate_H1000lk()

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False
    return True


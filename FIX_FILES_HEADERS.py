# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:09:18 2018

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
import shutil


outfile = open('test.txt','w')
H0601_lk_dict = dict()

def update_not_number_lk(non_number_value, non_numeric_lk):
    non_numeric_lk[non_number_value] = input("replacement value for non number")
    return non_numeric_lk

def replace_df_non_numerics(df, non_numeric_lk):
    for key, value in non_numeric_lk.items():
        df.replace(key, value,inplace = True)
    return df



def connect(dbconnection_string = dbconnection_string):
    '''
    Input: connection string
    Output: DD_RPT_GENERAL and DD_RPT_FILE tables as pandas dataframes
    ''' 
    
    conn = pyodbc.connect(dbconnection_string)    
    sqlGET_DD_RPT_GENERAL = "SELECT * FROM GEODWH.dbo.DD_RPT_GENERAL"
    sqlGET_DD_RPT_FILE = "SELECT * FROM GEODWH.dbo.DD_RPT_FILE"
    
    DD_RPT_GENERAL = pd.read_sql(sqlGET_DD_RPT_GENERAL,conn) 
    DD_RPT_FILE = pd.read_sql(sqlGET_DD_RPT_FILE,conn)    
  
    return DD_RPT_GENERAL, DD_RPT_FILE
    

def RPT_GENERAL(RIN,DD_RPT_GENERAL):
    '''    
    Input: RIN, DD_RPT_GENERAL pandas df
    Output: a subset of key data used to match the file to the correct RPT_ID within the database based on the RIN
    '''
    
    df = DD_RPT_GENERAL.loc[DD_RPT_GENERAL['RIN'] == RIN]
    df = df.reset_index()
    return (df['RPT_ID'][0],df['PERIODEND'][0],df['TENEMENT'][0],df['COUNT_SF_SAMP'][0],df['RPT_CODE'][0],df['RPT_TYPE'][0],df['HOLDER'][0],df['PROJNAME'][0])


def RPT_FILE(RPT_ID,DD_RPT_FILE):
    '''
    Input: RIN, DD_RPT_FILE pandas df
    Output: a count of the number of SGC files associated to the RIN
    '''
    
    df = pd.DataFrame(DD_RPT_FILE.loc[DD_RPT_FILE['RPT_ID'] == RPT_ID])
    dfSS = df.loc[df['FILETYPE'] == 'SGC'] #SG%
    return len(dfSS)

def generate_H1000lk():
    H1000lk = dict()
    with open(r"C:\Users\gatesk\Documents\SURFACE_SAMPLE_ASSAY_VALUE_ERRORS\H1000set_CONVERSIONS.csv",'r') as fin:
        for line in fin:
            items = line.split(',')
            H1000lk[items[0]] = items[1:]
            
    return H1000lk

H1000lk = generate_H1000lk()

def check_H1000lk(H1000s,H1000lk):
    if H1000s != None:
        for i in H1000s:
            i = i.strip()
            if i not in H1000lk:
                addlk = tuple(input("Enter valid lookups (val,unit,meth) for %s : " % i))
#TODO validate the entered values
                H1000lk[i] = addlk
        return H1000lk

def fix_H1000(H1000,H1000fix,H1000lk):
    for i in H1000:
        H1000fix.append((H1000lk[i.strip()][0],H1000lk[i.strip()][1],H1000lk[i.strip()][2].strip()))
    return H1000fix

#        if i not in H1000lk:
#            print ('H1000 %s not in dictonary'%i)
#            H1000converison = input("Enter the header conversion for %s: "%i)
#            H1000lk[i][0] = H1000converison
#            H1000unitconverison = input("Enter the header unit conversion for %s: "%i)
#            H1000lk[i][1] = H1000unitconverison
#            H1000methodconverison = input("Enter the method('XRF' or 'XRF_err') conversion for %s: "%i)
#            H1000lk[i][2] = H1000methodconverison

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False
    return True

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


def guess_zone(potenialzoneslist):
    validzones = ['54','55','56','57']
    fields = potenialzoneslist
    for item in fields:
        for zone in validzones:
            if (str(item)).find(zone) == -1:
                return zone
                break
            else:
                return 'unk_zone'
            
def guess_geodetic(potenialdatumslist):
    validdatums = ['GDA','AGD','MGA','AMG']
    fields = validdatums
    for item in fields:
        for zone in validdatums:
            if (str(item)).find(zone) == -1:
                return zone
                break
            else:
                return 'unk_datum'

def get_headers(line,delimiter,headers):
    '''
    Input: an open file, delimiter of the file, key header list
    Output: list of headers within the file
    '''
#    for line in fin:
    if line.startswith('H'):
        headers.add(line.split(delimiter)[0])
        
    return headers
        
        
def get_missing_headers(headers,missing_headers):
    '''
    Input: list of headers within the file, empty missing_headers list
    Output: builds a list of missing headers for the file
    '''
    for key_header in key_headers:
        if key_header not in headers:
            missing_headers.add(key_header)
            #print ('Missing %s header'%key_header)
            
    return missing_headers


def count_D_lines(line,delimiter,D_lines):
    D = line.split(delimiter)[0]    
    if D == 'D':
        D_lines.append(D)
    return len(D_lines)


def H0203(line,delimiter,H0203_val):
    '''
    Input: filepath, delimiter of the file
    Outout: count of the number of 'D' prefixed datalines in the file
    '''
    
    if line.startswith('H0203'):
        try:
            H0203_val.append(line.split(delimiter)[2]) 
        except:
            pass
    return H0203_val


def H0002(line,headers,delimiter,oldversion,newversion,newrptversion):    
    if 'H0002' in headers:
        if line.startswith('H0002'):
            oldversion.add(delimiter.join(line.split(delimiter)))
    
    newversion.add(delimiter.join(['H0002','Version',newrptversion,'\n']))            
    return oldversion, newversion


def H0004(line,headers,delimiter,olddate,newdate,newrptdate):    
    if 'H0004' in headers:
        if line.startswith('H0004'):
            olddate.add(delimiter.join(line.split(delimiter)))
    
    newdate.add(delimiter.join(['H0004','Reporting end date',newrptdate,'\n']))            
    return olddate, newdate


def H0100(line,headers,delimiter,oldten,newten,newrptten):    
    if 'H0100' in headers:
        if line.startswith('H0100'):
            oldten.add(delimiter.join(line.split(delimiter)))    
    newten.add(delimiter.join(['H0100','TENID',newrptten,'\n']))
    return oldten, newten

def H0101(line,headers,delimiter,oldhold,newhold,newrpthold):    
    if 'H0101' in headers:
        if line.startswith('H0101'):
            oldhold.add(delimiter.join(line.split(delimiter)))    
    newhold.add(delimiter.join(['H0101','TEN HOLDER',newrpthold,'\n']))
    return oldhold, newhold

def H0102(line,headers,delimiter,oldproj,newproj,newrptproj):    
    if 'H0102' in headers:
        if line.startswith('H0102'):
            oldproj.add(delimiter.join(line.split(delimiter)))    
    newproj.add(delimiter.join(['H0102','PROJECT NAME',newrptproj,'\n']))
    return oldproj, newproj

def H0202(line,headers,delimiter,oldtem,newtem,newrpttem):
    if 'H0202' in headers:
        if line.startswith('H0202'):
            oldtem.add(delimiter.join(line.split(delimiter)))    
    newtem.add(delimiter.join(['H0202','TEMPLATE FORMAT','SGC','\n']))
    return oldtem, newtem


def Hf(line,headers,delimiter,HeaderField, Hfout = []):
    if HeaderField in headers:
        if line.startswith(HeaderField):
            try:
                for i in line.split(delimiter):
                    Hfout.append(i)
            except:
                pass
        return Hfout




def H0531(line,headers,delimiter,zone):
    if 'H0531' in headers:
        if line.startswith('H0531'):
            try:
                zone = line.split(delimiter)[2]
            except:
                pass
        return zone
    
    
def H0501(line,headers,delimiter,geodetic):
    if 'H0501' in headers:
        if line.startswith('H0501'):
            try:
                oldgeodetic = line.split(delimiter)[2]
                geodetic.add(oldgeodetic)
            except:
                pass
        return geodetic
    
    
def H0530f(line,headers,delimiter,H05):
    if 'H0530' in headers:
        if line.startswith('H0530'):
            try:
                oldzone = line.split(delimiter)[2]
                H05.add(oldzone)
            except:
                pass
        return H05

def H0502f(line,headers,delimiter,H05):
    if 'H0502' in headers:
        if line.startswith('H0502'):
            try:
                oldzone = line.split(delimiter)[2]
                H05.add(oldzone)
            except:
                pass
        return H05
    
def H0503f(line,headers,delimiter,H05):
    if 'H0503' in headers:
        if line.startswith('H0503'):
            try:
                oldzone = line.split(delimiter)[2]
                H05.add(oldzone)
            except:
                pass
        return H05
    
def H0504f(line,headers,delimiter,H05):
    if 'H0504' in headers:
        if line.startswith('H0504'):
            try:
                oldzone = line.split(delimiter)[2]
                H05.add(oldzone)
            except:
                pass
        return H05
    
def H0505f(line,headers,delimiter,H05):
    if 'H0505' in headers:
        if line.startswith('H0505'):
            try:
                oldzone = line.split(delimiter)[2]
                H05.add(oldzone)
            except:
                pass
        return H05
    
def H0506f(line,headers,delimiter,H05):
    if 'H0506' in headers:
        if line.startswith('H0506'):
            try:
                oldzone = line.split(delimiter)[2]
                H05.add(oldzone)
            except:
                pass
        return H05
    
def H0507f(line,headers,delimiter,H05):
    if 'H0507' in headers:
        if line.startswith('H0507'):
            try:
                oldzone = line.split(delimiter)[2]
                H05.add(oldzone)
            except:
                pass
        return H05
    
def H0508f(line,headers,delimiter,H05):
    if 'H0508' in headers:
        if line.startswith('H0508'):
            try:
                oldzone = line.split(delimiter)[2]
                H05.add(oldzone)
            except:
                pass
        return H05

def H0600f(line,headers,delimiter,H0600):
    if 'H0600' in headers:
        if line.startswith('H0600'):
            try:
                for i in line.split(delimiter):
                    H0600.append(i.rstrip())
            except:
                pass
        return H0600

def H0601f(line,headers,delimiter,H0601):
    if 'H0601' in headers:
        if line.startswith('H0601'):
            try:
                for i in line.split(delimiter):
                    H0601.append(i.rstrip())
            except:
                pass
        return H0601
    
def H0602f(line,headers,delimiter,H0602):
    if 'H0602' in headers:
        if line.startswith('H0602'):
            try:
                for i in line.split(delimiter):
                    H0602.append(i.rstrip())
            except:
                pass
        return H0602

def H0603f(line,headers,delimiter,H0603):
    if 'H0603' in headers:
        if line.startswith('H0603'):
            try:
                for i in line.split(delimiter):
                    H0603.append(i.rstrip())
            except:
                pass
        return H0603
    
def H0604f(line,headers,delimiter,H0604):
    if 'H0604' in headers:
        if line.startswith('H0604'):
            try:
                for i in line.split(delimiter):
                    H0604.append(i.rstrip())
            except:
                pass
        return H0604
    
def H0605f(line,headers,delimiter,H0605):
    if 'H0605' in headers:
        if line.startswith('H0605'):
            try:
                for i in line.split(delimiter):
                    H0605.append(i.rstrip())
            except:
                pass
        return H0605
    
def H0606f(line,headers,delimiter,H0606):
    if 'H0606' in headers:
        if line.startswith('H0606'):
            try:
                for i in line.split(delimiter):
                    H0606.append(i.rstrip())
            except:
                pass
        return H0606
    
def H0607f(line,headers,delimiter,H0607):
    if 'H0607' in headers:
        if line.startswith('H0607'):
            try:
                for i in line.split(delimiter):
                    H0607.append(i.rstrip())
            except:
                pass
        return H0607
    
def H0608f(line,headers,delimiter,H0608):
    if 'H0608' in headers:
        if line.startswith('H0608'):
            try:
                for i in line.split(delimiter):
                    H0608.append(i.rstrip())
            except:
                pass
        return H0608
    
def H0609f(line,headers,delimiter,H0609):
    if 'H0609' in headers:
        if line.startswith('H0609'):
            try:
                for i in line.split(delimiter):
                    H0609.append(i.rstrip())
            except:
                pass
        return H0609
    

def H0800f(line,headers,delimiter,H0800):
    if 'H0800' in headers:
        if line.startswith('H0800'):
            try:
                for i in line.split(delimiter):
                    H0800.append(i.rstrip())
            except:
                pass
        return H0800

def H0801f(line,headers,delimiter,H0801):
    if 'H0801' in headers:
        if line.startswith('H0801'):
            try:
                for i in line.split(delimiter):
                    H0801.append(i.rstrip())
            except:
                pass
        return H0801
    
def H0802f(line,headers,delimiter,H0802):
    if 'H0802' in headers:
        if line.startswith('H0802'):
            try:
                for i in line.split(delimiter):
                    H0802.append(i.rstrip())
            except:
                pass
        return H0802

def H0803f(line,headers,delimiter,H0803):
    if 'H0802' in headers:
        if line.startswith('H0803'):
            try:
                for i in line.split(delimiter):
                    H0803.append(i.rstrip())
            except:
                pass
        return H0803

def H0804f(line,headers,delimiter,H0804):
    if 'H0804' in headers:
        if line.startswith('H0804'):
            try:
                for i in line.split(delimiter):
                    H0804.append(i.rstrip())
            except:
                pass
        return H0804

def H0805f(line,headers,delimiter,H0805):
    if 'H0805' in headers:
        if line.startswith('H0805'):
            try:
                for i in line.split(delimiter):
                    H0805.append(i.rstrip())
            except:
                pass
        return H0805

def H0806f(line,headers,delimiter,H0806):
    if 'H0806' in headers:
        if line.startswith('H0806'):
            try:
                for i in line.split(delimiter):
                    H0806.append(i.rstrip())
            except:
                pass
        return H0806

def H0807f(line,headers,delimiter,H0807):
    if 'H0807' in headers:
        if line.startswith('H0807'):
            try:
                for i in line.split(delimiter):
                    H0807.append(i.rstrip())
            except:
                pass
        return H0807

def H0808f(line,headers,delimiter,H0808):
    if 'H0808' in headers:
        if line.startswith('H0808'):
            try:
                for i in line.split(delimiter):
                    H0808.append(i.rstrip())
            except:
                pass
        return H0808

def H0809f(line,headers,delimiter,H0809):
    if 'H0809' in headers:
        if line.startswith('H0809'):
            try:
                for i in line.split(delimiter):
                    H0809.append(i.rstrip())
            except:
                pass
        return H0809

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

def count_all_the_Ds(path,folder):
    total_D_count = 0
    files = os.listdir(os.path.join(path,folder))
    for file in files:
        filepath = os.path.join(os.path.join(path,folder),file)
        with open(filepath,'r') as fin:
            for line in fin:
                if line.startswith('D') or line.startswith('"D"'):
                    total_D_count = total_D_count + 1
    return total_D_count

class renamer():
     def __init__(self):
          self.d = dict()

     def __call__(self, x):
          if x not in self.d:
              self.d[x] = 0
              return x
          else:
              self.d[x] += 1
              return "%s_%d" % (x, self.d[x])


def main():
    path = "X:\_SS_RELOAD\PENDING"
    folders = os.listdir(path)
    RPTGENERAL = connect(dbconnection_string)[0]
    RPTFILE = connect(dbconnection_string)[1]
    
    '''iterate the folders'''
    for folder in folders:
        rinfiles = os.listdir(os.path.join(path,folder))

        rpt_details = RPT_GENERAL(folder,RPTGENERAL)
        RPTID = rpt_details[0]   
        newversion_item = str(rpt_details[5])
        newdate = str(rpt_details[1])
        newrptten = str(rpt_details[2].split(',')[0])
        newrpthold = str(rpt_details[6])
        newrptproj = str(rpt_details[7])
        
        total_D_count = count_all_the_Ds(path,folder)
        num_files = len(rinfiles)
        RPTID = rpt_details[0]
        db_sample_count = str(rpt_details[3])
        SS_file_count = RPT_FILE(RPTID,RPTFILE)
        
        print ('\n')
        outfile.write("\n-------\n")
        print ("Checking SGC files found in RIN: %s" % folder)
        outfile.write("Checking SGC files found in RIN: %s\n" % folder)
        
        #print ("Matching db RPT details: %s"% str(rpt_details))        
        print('DB file count %s verses RIN file count %s'%(str(SS_file_count),str(num_files)))
        outfile.write('DB file count %s verses RIN file count %s\n'%(str(SS_file_count),str(num_files)))
        if SS_file_count != num_files:
            print ("WARNING The number of files reported in the database does not match the number found in the RIN")
            outfile.write("WARNING The number of files reported in the database does not match the number found in the RIN\n")
        if SS_file_count == num_files:
            print ("Passed file count")
            outfile.write("Passed file count\n")
            
        print('DB sample count %s verses total RIN sample count %s'%(str(db_sample_count),str(total_D_count)))
        outfile.write('DB sample count %s verses total RIN sample count %s\n'%(str(db_sample_count),str(total_D_count)))
        if float(db_sample_count) != float(total_D_count):
            print ("WARNING The number of samples reported in the database does not match the number found in the files within the RIN")
            outfile.write("WARNING The number of samples reported in the database does not match the number found in the files within the RIN\n")
        if float(db_sample_count) == float(total_D_count):
            print ("Passed total sample count")
            outfile.write("Passed total sample count\n")
            
            
        '''iterate the files in the folders'''
        fcount = 0
        for file in rinfiles:
            outfile.write("\n-------\n")
            fcount = fcount + 1
            fcount_label = '00%s' %fcount
            formated_name = "%s_%s_%s_SGC_%s.txt"%(folder,newrptten,fcount_label,newversion_item)
            missing_H600 = False
            missing_H800 = False
            
            filepath = os.path.join(os.path.join(path,folder),file)
            
            print ("Checking file: %s" % file)
            print ("The location of file is: %s" % filepath)
            print ("The new name of file is: %s" % formated_name)
                
            #cont = input()
            cont = 'y'
            if cont == 'q':
                sys.exit()
            elif cont != 'q':
                pass


            
#TODO new file name
            
#NEW FILE TO WRITE OUT
            
            delimiter = detect_delimter(filepath)
            
            if delimiter == 'unk' or delimiter == 'error' :
                (input("Delimiter is not tab or csv - The file has been moved to delimiter error folder, hit enter to continue"))
                
                delimter_issues_path  = os.path.join(r"X:\_SS_RELOAD\issues_delimiter",folder)
                
                if not os.path.exists(delimter_issues_path):
                    os.makedirs(delimter_issues_path)
                
                move_to_path =  str(os.path.join(delimter_issues_path,file))
                
                shutil.move(filepath,move_to_path)
                break
            
            newrptversion = str(rpt_details[5])
            newrptdate = str(rpt_details[1])
            newrpttem = 'SGC'
#            newtenement = str(rpt_details[2])
            
            ### Setting the empty placeholders ###
            D_lines = []
            H0203_val = []
            headers = set()
            missing_headers = set()
            
            oldversion = set()
            newversion = set()
            
            olddate = set()
            newdate = set()
            
            oldten = set()
            newten = set()
            
            oldhold = set()
            newhold = set()
            
            oldproj = set()
            newproj = set()

            oldtem = set()
            newtem = set()
            
            zone = ''
            H05 = set()
            H0530 = set()
            H0502 = set()
            H0503 = set()
            H0504 = set()
            H0505 = set()
            H0506 = set()
            H0507 = set()
            H0508 = set()
                        
            geodetic = set()
            
            H0600 = []
            H0601 = []
            H0602 = []
            H0603 = []
            H0604 = []
            H0605 = []
            H0606 = []
            H0607 = []
            H0608 = []
            H0609 = []
            
            H0800 = []
            H0801 = []
            H0802 = []
            H0803 = []
            H0804 = []
            H0805 = []
            H0806 = []
            H0807 = []
            H0808 = []
            H0809 = []
            
            H1000 = []
            H1000fix = []
            
            H1001 = []
            H1002 = []
            H1003 = []
            
        
            '''iterate the lines in the files'''
            for line in line_generator(filepath):
                headers = get_headers(line,delimiter,headers)
#                counted_D_lines = count_D_lines(line,delimiter,D_lines)
#                H0203_count = H0203(line,delimiter,H0203_val)
                
#                oldv = H0002(line,headers,delimiter,oldversion,newversion,newrptversion)[0]
                newv = H0002(line,headers,delimiter,oldversion,newversion,newrptversion)[1]
                
#                oldd = H0004(line,headers,delimiter,olddate,newdate,newrptdate)[0]
                newd = H0004(line,headers,delimiter,olddate,newdate,newrptdate)[1]
                
#                oldt = H0100(line,headers,delimiter,oldten,newten,newrptten)[0]
                newt = H0100(line,headers,delimiter,oldten,newten,newrptten)[1]
                
#                oldh = H0101(line,headers,delimiter,oldhold,newhold,newrpthold)[0]
                newh = H0101(line,headers,delimiter,oldhold,newhold,newrpthold)[1]
                
#                oldp = H0102(line,headers,delimiter,oldproj,newproj,newrptproj)[0]
                newp = H0102(line,headers,delimiter,oldproj,newproj,newrptproj)[1]
                
#                oldtm = H0202(line,headers,delimiter,oldtem,newtem,newrpttem)[0]
                newtm = H0202(line,headers,delimiter,oldtem,newtem,newrpttem)[1]
                
                zone_H0531 = H0531(line,headers,delimiter,zone)
                geod = H0501(line,headers,delimiter,geodetic)
                
                H0530s = H0530f(line,headers,delimiter,H0530)
                H0502s = H0502f(line,headers,delimiter,H0502)
                H0503s = H0503f(line,headers,delimiter,H0503)
                H0504s = H0504f(line,headers,delimiter,H0504)
                H0505s = H0505f(line,headers,delimiter,H0505)
                H0506s = H0506f(line,headers,delimiter,H0506)
                H0507s = H0507f(line,headers,delimiter,H0507)
                H0508s = H0508f(line,headers,delimiter,H0508)
                H05 = list([H0502s,H0503s,H0504s,H0505s,H0506s,H0507s,H0508s,H0530s])

                H0600s = H0600f(line,headers,delimiter,H0600)
                H0601s = H0601f(line,headers,delimiter,H0601)
                H0602s = H0602f(line,headers,delimiter,H0602)
                H0603s = H0603f(line,headers,delimiter,H0603)
                H0604s = H0604f(line,headers,delimiter,H0604)
                H0605s = H0605f(line,headers,delimiter,H0605)
                H0606s = H0606f(line,headers,delimiter,H0606)
                H0607s = H0607f(line,headers,delimiter,H0607)
                H0608s = H0608f(line,headers,delimiter,H0608)
                H0609s = H0609f(line,headers,delimiter,H0609)
                
                H0800s = H0800f(line,headers,delimiter,H0800)
                H0801s = H0801f(line,headers,delimiter,H0801)
                H0802s = H0802f(line,headers,delimiter,H0802)
                H0803s = H0803f(line,headers,delimiter,H0803)
                H0804s = H0804f(line,headers,delimiter,H0804)
                H0805s = H0805f(line,headers,delimiter,H0805)
                H0806s = H0806f(line,headers,delimiter,H0806)
                H0807s = H0807f(line,headers,delimiter,H0807)
                H0808s = H0808f(line,headers,delimiter,H0808)
                H0809s = H0809f(line,headers,delimiter,H0809)
                
                H1000s = H1000f(line,headers,delimiter,H1000)
                H1001s = H1001f(line,headers,delimiter,H1001)
                H1002s = H1002f(line,headers,delimiter,H1002)
#                H1003s = H1003f(line,headers,delimiter,H1003)
            
            headers_missing = get_missing_headers(headers,missing_headers)
            
            if zone_H0531 is None:
                if len(H05) != 0:
                    print(H05)
                    guessedzone = guess_zone(H05)
                    H0531new = delimiter.join(['H0531','PROJECTION_ZONE',guessedzone])
                    
            if zone_H0531 is not None:
                if zone_H0531 in ['54','55','56','57']:
                    H0531new = delimiter.join(['H0531','PROJECTION_ZONE',guessedzone])
                else:
                    H0531new = delimiter.join(['H0531','PROJECTION_ZONE','unk_zone'])
            
            if geod is None:
                if len(H05) != 0:
                    print (str(H05))
                    datum = guess_geodetic(H05)
                    if datum in ['MGA','MGA94']:
                                datum = 'GDA'
                    if datum in ['AMG','AMG66','AMG84']:
                        datum = 'AGD'
                    if datum == 'GDA94':
                        datum = 'GDA'
                    if datum == 'AGD66' or datum == 'AGD84':
                        datum = 'AGD'
                    H0501new = delimiter.join(['H0501','GEODETIC DATUM',datum])
                            
            if geod is not None:             
                for datum in valid_datums: #imported from *
                    if (str(geod)).find(datum) == -1:
                            if datum in ['MGA','MGA94']:
                                datum = 'GDA'
                            if datum in ['AMG','AMG66','AMG84']:
                                datum = 'AGD'
                            if datum == 'GDA94':
                                datum = 'GDA'
                            if datum == 'AGD66' or datum == 'AGD84':
                                datum = 'AGD'
                            H0501new = delimiter.join(['H0501','GEODETIC DATUM',datum])
                            break
                else:
                    H0501new = delimiter.join(['H0501','GEODETIC DATUM','unk_datum'])
                    
            print ("Checking H0600-H0601-SAMPLE_CODES/SAMPLE_TYPES Header lines...")
                        
            if H0600s != None:
                print("File H0600 line is: %s" % str(delimiter.join(H0600s)).strip().rstrip(str(delimiter)))
            else:
                print ("File H0600 line does not exist\n Creating a dummy record")
                H0600newline = delimiter.join(['H0600','SAMPLE_CODE','unk'])
                missing_H600 = True
                
            if H0601s != None:
                print("File H0601 line is: %s" % str(delimiter.join(H0601s)).strip().rstrip(str(delimiter)))
            else:
                print ("File H0600 line does not exist\n Creating a dummy record")
                H0601newline = delimiter.join(['H0601','SAMPLE_TYPE','unk'])    
            
            if H0602s != None:
                print("File H0602 line is: %s" % str(delimiter.join(H0602s)).strip().rstrip(str(delimiter)))
            if H0603s != None:
                print("File H0603 line is: %s" % str(delimiter.join(H0603s)).strip().rstrip(str(delimiter)))
            if H0604s != None:
                print("File H0604 line is: %s" % str(delimiter.join(H0604s)).strip().rstrip(str(delimiter)))
            if H0605s != None:
                print("File H0605 line is: %s" % str(delimiter.join(H0605s)).strip().rstrip(str(delimiter)))
            if H0606s != None:
                print("File H0606 line is: %s" % str(delimiter.join(H0606s)).strip().rstrip(str(delimiter)))
            if H0607s != None:
                print("File H0607 line is: %s" % str(delimiter.join(H0607s)).strip().rstrip(str(delimiter)))
            if H0608s != None:
                print("File H0608 line is: %s" % str(delimiter.join(H0608s)).strip().rstrip(str(delimiter)))
            if H0609s != None:
                print("File H0609 line is: %s" % str(delimiter.join(H0609s)).strip().rstrip(str(delimiter)))
                
                
            H6x = []
            H6y = []
            if H0602s is not None:
                H6x.append(H0602s[1])
                H6y.append(H0602s[2])
            if H0603s is not None:
                H6x.append(H0603s[1])
                H6y.append(H0603s[2])
            if H0604s is not None:
                H6x.append(H0604s[1])
                H6y.append(H0604s[2])
            if H0605s is not None:
                H6x.append(H0605s[1])
                H6y.append(H0605s[2])
            if H0606s is not None:
                H6x.append(H0606s[1])
                H6y.append(H0606s[2])
            if H0607s is not None:
                H6x.append(H0607s[1])
                H6y.append(H0607s[2])
            if H0608s is not None:
                H6x.append(H0608s[1])
                H6y.append(H0608s[2])
            if H0609s is not None:
                H6x.append(H0609s[1])
                H6y.append(H0609s[2])
        
            #pivot_H6 = input("Does this need to be pivoted? ('y','n')")
            pivot_H6 = 'y'
            if pivot_H6  == 'y' and missing_H600 == False:
                
                H06x = [H0600s[0],H0600s[1],H0601s[1]]
                H0600new = H06x+H6x
                
                for i in H0600new:
                    i = i.strip()
                H06y = [H0601s[0],H0600s[2],H0601s[2]]
                H0601new = H06y+H6y
                for i in H0601new:
                    i = i.strip()
                
                H0600newline = str(delimiter.join(H0600new))
                H0601newline = str(delimiter.join(H0601new))
                
            if pivot_H6  != 'y' and missing_H600 == False:
                H0600newline = str(delimiter.join(H0600s)).strip().rstrip(str(delimiter))
                H0601newline = str(delimiter.join(H0601s)).strip().rstrip(str(delimiter))
                pass
                

                      
#            sample_lk_dict = {'0':'soil','1':'rockchip','2':'float','3':'stream','4':'costean','5':'lag','6':'minespoil','7':'drillspoil','8':'water','9':'vegetation','10':'unknown','11':'surf_drill'}
#            sample_lk_dict = collections.OrderedDict(sorted(sample_lk_dict.items()))
#            
#            print ('0:soil\n1:rockchip\n2:float\n3:stream\n4:costean\n5:lag\n6:minespoil\n7:drillspoil\n8:water\n9:vegetation\n10:unknown\n11:surf_drill\n')
#            
#            for H0601value in H0601newline.split(delimiter):
#                if H0601value not in ['Sample_type','H0601','Sample_Type','Sample Type','Sample type']:
#                    if H0601value not in H0601_lk_dict:
#                        converison = input("enter the conversion for %s: " % H0601value)
#                        H0601_lk_dict[H0601value] = sample_lk_dict[converison]
#                else:
#                    pass
#            print (H0601_lk_dict)
                
            H8x = []
            H8y = []
            H8z = []
            if H0802s is not None:
                try:
                    H8x.append(H0802s[1])
                except:
                    pass
                try:
                    H8y.append(H0802s[2])
                except:
                    pass
            try:
                H8z.append(H0802s[3])
            except:
                pass

            if H0803s is not None:
                try:
                    H8x.append(H0803s[1])
                except:
                    pass
                try:
                    H8y.append(H0803s[2])
                except:
                    pass
            try:
                H8z.append(H0803s[3])
            except:
                pass
            
            if H0804s is not None:
                H8x.append(H0804s[1])
                H8y.append(H0804s[2])
            try:
                H8z.append(H0804s[3])
            except:
                pass
            if H0805s is not None:
                H8x.append(H0805s[1])
                H8y.append(H0805s[2])
            try:
                H8z.append(H0805s[3])
            except:
                pass
            if H0806s is not None:
                H8x.append(H0806s[1])
                H8y.append(H0806s[2])
            try:
                H8z.append(H0806s[3])
            except:
                pass
            if H0807s is not None:
                H8x.append(H0807s[1])
                H8y.append(H0807s[2])
            try:
                H8z.append(H0807s[3])
            except:
                pass
            if H0808s is not None:
                H8x.append(H0808s[1])
                H8y.append(H0808s[2])
            try:
                H8z.append(H0808s[3])
            except:
                pass
            if H0809s is not None:
                H8x.append(H0809s[1])
                H8y.append(H0809s[2])
            try:
                H8z.append(H0809s[3])
            except:
                pass
                                    
            print ("Checking H0801-H0802-ASSAY_CODES/ASSAY_DESC/ASSAY_COMPANY Header lines...")
            
            if H0800s != None:
                print("File H0800 line is: %s" % str(delimiter.join(H0800s)).strip().rstrip(str(delimiter)))
            else:
                H0800newline = delimiter.join(['H0800','ASSAY_CODE','unk'])
                missing_H800 = True
                
            if H0801s != None:
                print("File H0801 line is: %s" % str(delimiter.join(H0801s)).strip().rstrip(str(delimiter)))
            else:
                H0801newline = delimiter.join(['H0801','ASSAY_DESC','unk'])    
            
            if H0802s != None:
                print("File H0802 line is: %s" % str(delimiter.join(H0802s)).strip().rstrip(str(delimiter)))
            else:
                H0802newline = delimiter.join(['H0802','ASSAY_COMPANY','unk'])  
                
            if H0803s != None:
                print("File H0803 line is: %s" % str(delimiter.join(H0803s)).strip().rstrip(str(delimiter)))
            if H0804s != None:
                print("File H0804 line is: %s" % str(delimiter.join(H0804s)).strip().rstrip(str(delimiter)))
            if H0805s != None:
                print("File H0805 line is: %s" % str(delimiter.join(H0805s)).strip().rstrip(str(delimiter)))
            if H0806s != None:
                print("File H0806 line is: %s" % str(delimiter.join(H0806s)).strip().rstrip(str(delimiter)))
            if H0807s != None:
                print("File H0807 line is: %s" % str(delimiter.join(H0807s)).strip().rstrip(str(delimiter)))
            if H0808s != None:
                print("File H0808 line is: %s" % str(delimiter.join(H0808s)).strip().rstrip(str(delimiter)))
            if H0809s != None:
                print("File H0809 line is: %s" % str(delimiter.join(H0809s)).strip().rstrip(str(delimiter)))
                
            #pivot_H8 = input("Does this need to be pivoted? ('y','n')")
            pivot_H8 = 'y'
            
            
            if pivot_H8 == 'y' and missing_H800 == False:
                H08x = [H0800s[0].rstrip('\n'),H0800s[1].rstrip('\n'),H0801s[1].rstrip('\n')]
                H0800new = H08x+H8x
                H0800newline = str(delimiter.join(H0800new).rstrip('\n'))
                
                for i in H0800new:
                    i = i.strip().rstrip('\n')
                H08y = [H0801s[0].rstrip('\n'),H0800s[2].rstrip('\n'),H0801s[2].rstrip('\n')]
                H0801new = H08y+H8y
                H0801newline = str(delimiter.join(H0801new).rstrip('\n'))
                
                for i in H0801new:
                    i = i.strip().rstrip('\n')
            try:
                H08z = [H0802s[0].rstrip('\n'),H0800s[3].rstrip('\n'),H0801s[3].rstrip('\n')]
                H0802new = H08z+H8z
                for i in H0802new:
                    i = i.strip().rstrip('\n')
                H0802newline = str(delimiter.join(H0802new).rstrip('\n'))
            except:
                pass
            
            if pivot_H8 != 'y' and missing_H800 == False:
                H0800newline = str(delimiter.join(H0800s)).strip().rstrip(str(delimiter))
                H0801newline = str(delimiter.join(H0801s)).strip().rstrip(str(delimiter))
                try:
                    H0802newline = str(delimiter.join(H0802s)).strip().rstrip(str(delimiter))
                except:
                    pass
                pass
            
            check_H1000lk(H1000s,H1000lk)
            if 'H1000' in headers:
                H1000fixed = fix_H1000(H1000s,H1000fix,H1000lk)

            if 'H1000' not in headers:
                
                print ('No H1000 field')
                No_H1000_path  = os.path.join(r"X:\_SS_RELOAD\issues_missing_H1000_line",folder)
                
                if not os.path.exists(No_H1000_path):
                    os.makedirs(No_H1000_path)
                
                move_to_path =  str(os.path.join(No_H1000_path,file))
                
                shutil.move(filepath,move_to_path)
                break
            
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
            
            if 'H1001' not in headers and 'H1002' not in headers:
                for idx, column in enumerate(H1000):
                    headersdict[column] = H1000fixed[idx],'unk','unk'
                
            outfile.write(str(list(newv)[0]))
            outfile.write(str(list(newd)[0]))
            outfile.write(str(list(newt)[0]))
            outfile.write(str(list(newh)[0]))
            outfile.write(str(list(newp)[0]))
            outfile.write(str(list(newtm)[0]))
            outfile.write(str(H0531new)+'\n')
            outfile.write(str(H0501new)+'\n')
            outfile.write(str(H0600newline)+'\n')
            outfile.write(str(H0601newline)+'\n')
            outfile.write(str(H0800newline)+'\n')
            outfile.write(str(H0801newline)+'\n')
            outfile.write(str(H0802newline)+'\n')
        
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
                               
            for key, val in headersdict.items():
                if headersdict[key][0][1] != 'unk':
                    if 'H1001' in headers:
                        if headersdict[key][1] != headersdict[key][0][1]:
                            print ("the header %s units do not match between the H1000: %s and H1001: %s" % (str(key),headersdict[key][1],headersdict[key][0][1]))
                            outfile.write("the header %s units do not match between the H1000: %s and H1001: %s\n" % (str(key),headersdict[key][1],headersdict[key][0][1]))

            for key, val in headersdict.items():
                if headersdict[key][0][2] in ['XRF','XRF_err']:
                    print ("header method needs to include XRF values")
                    print (headersdict[key])
                    
##XRF H1002 field updates

#                if headersdict[key][0][2] == 'XRF':
#                    print (headersdict[key][0][2])

            df = pd.DataFrame(columns = H1000convert)
            print (list(df))
            
            with open(filepath) as load_to_df:
                print (filepath)
                for line in load_to_df:
                    if line.startswith('D'):
                        line = line.split(delimiter)
                        line = [item.strip() for item in line]
                        df.loc[-1] = line
                        df.index = df.index + 1
                        
            dropcolumns = []
            for idx, column in enumerate(H1000convert):
                if column == 'IGNORE':
                    dropcolumns.append(idx)
                    
            df.drop(df.columns[dropcolumns], axis=1,inplace=True)
            df.dropna(axis=1, how='all')
            df = df.rename(columns=renamer())

            dfnumeric = df.convert_objects(convert_numeric=True)
            headers = df.dtypes.index
            
            elements = ['Au','Cu','Hg']
            
            for idx, col in enumerate(headers):                
                if col in elements:
                    headerdict_key = H1000s[idx]
                    print("\n-----\n")
                    print (col)
#                    print (headersdict[headerdict_key])
                    
                    
                    if headersdict[headerdict_key] in ['ppm','ppb','pct']:
                        print ("Unit is defined as '%s' in original H1001 field" %str(headersdict[headerdict_key][1]))
                    else:
                        print ("Unit is not defined in original H1001 field")
                        print ("Unit is defined as '%s' in H1000 field" %str(headersdict[headerdict_key][0][1]))
                    
                    print("\n-----\n")
                    print (dfnumeric[col].describe())
                    print("\n-----\n")
                    
#TODO MAKE SOME UNIT SUGGESTIONS BASED ON THE VALUES
                    
                    try:
                        fig = dfnumeric[col].plot.hist(bins=25)
                        fig = plt.figure()
                        fig.show()
                        plt.pause(0.1)
                        
                        #graphinput = input() 
                        graphinput = 'c'
                        if graphinput == 'q':
                            break
                        elif graphinput != 'q':
                            pass
                    except:
                        pass
            
            uni = set()
            for i in H1000convert:
                if i in elements:
                    uniques = df[i].unique().tolist()
                    for u in uniques:
                        uni.add(u)

            not_numbers = [x for x in list(uni) if not is_number(x) == True]
            print("\n-----\n")
            
            for i in not_numbers:
                if i in non_numeric_lk:
                    df = df.replace(i, non_numeric_lk[i])
                else:
                    print ("None numeric values in table: '%s'" % i)
                    update_not_number_lk(i.strip(), non_numeric_lk)
                    df = df.replace(i, non_numeric_lk[i])
        
            print(df)
            print("\n-----\n")
                
main()

outfile.close()


        
        
        
        
        
        
        
        
        
        
        
        
        
    
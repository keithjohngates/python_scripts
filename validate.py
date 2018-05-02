# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:32:18 2018

@author: gatesk
"""
import os
from database_connection import DatabaseConnection
from folder_reader import FolderReader
from file_reader import FileReader
from report_errors import ReportErrors
from data_records import DataRecords
from lookups import generate_h1000lk, h1001lk, valid_h1001_codes, dbconnection_string
from make_corrections import MakeCorrections
from gather_db_data import GatherDatabaseData


validation_report = open('validation_report.csv', 'w' )

h1000lk = generate_h1000lk()
rootpath = r'X:\_SS_RELOAD\PENDING\R00029160'


def validate(file):
    fdict = FileReader(file).fdict    
    
    delimiter = fdict['delimiter']
    validator = ReportErrors(fdict,file,h1000lk)   
    
    errors = validator.run()
    headers_fix =  validator.set_to_fix()    
    
    return file, fdict, errors, delimiter, headers_fix


def correct(file, fdict, errors, delimiter, rin, headers_fix):
    for i in errors:
        validation_report.write(str(i))
        print (i)
        
    zone = MakeCorrections(errors, fdict, file, delimiter, rin).guess_zone()
    datum = MakeCorrections(errors, fdict, file, delimiter, rin).guess_geodetic()
    
    pivot_h0600 = MakeCorrections(errors, fdict, file, delimiter, rin).pivot_h0600()
    
    pivot_h0800 = MakeCorrections(errors, fdict, file, delimiter, rin).pivot_h0800()
    
    if 'H1000' in fdict['headers']:
        convert_h1000 = MakeCorrections(errors, fdict, file, delimiter, rin).convert_h1000(h1000lk)
    else:
        pass
    
    if 'H1001' in fdict['headers']:
       convert_h1001 = MakeCorrections(errors, fdict, file, delimiter, rin).convert_h1001(h1001lk, valid_h1001_codes)
    else:
        pass
    
    db_gather = GatherDatabaseData(dbconnection_string, rin, delimiter)
    db_corrected_headers = db_gather.current_database_lookup_headers()
    db_counts = db_gather.current_database_lengths()
    
    print ('-----')
#    validation_report.write(str('-----'))
#    validation_report.write('\n')
    for i in db_corrected_headers:
        print (i)   
        validation_report.write(str(i))
        
    print (zone)
    print (datum)
#    validation_report.write(str(zone))
#    validation_report.write(str(datum))
    
    if headers_fix['H0600'] == True:
        for idx, i in enumerate(pivot_h0600):
            hfield = 'H060%s '% str(idx)
            i.insert(0, hfield)
            print (delimiter.join(i))
            
    else:
        print (delimiter.join.fdict['H0600'])
        print (delimiter.join.fdict['H0601'])
        print (delimiter.join.fdict['H0602'])
#        validation_report.write(str(delimiter.join.fdict['H0600']))
#        validation_report.write('\n')
#        validation_report.write(str(delimiter.join.fdict['H0601']))
#        validation_report.write('\n')
#        validation_report.write(str(delimiter.join.fdict['H0602']))
#        validation_report.write('\n')
        
    if headers_fix['H0800'] == True:
        for idx, i in enumerate(pivot_h0800):
            hfield = 'H080%s '% str(idx)
            i.insert(0, hfield)
            print (delimiter.join(i))
            validation_report.write(str(delimiter.join(i)))
            
    else:
        print (delimiter.join.fdict['H0800'])
        print (delimiter.join.fdict['H0801'])
        print (delimiter.join.fdict['H0802'])
#        validation_report.write(str(delimiter.join.fdict['H0800']))
#        validation_report.write('\n')
#        validation_report.write(str(delimiter.join.fdict['H0801']))
#        validation_report.write('\n')
#        validation_report.write(str(delimiter.join.fdict['H0802']))
#        validation_report.write('\n')
        
        
    if 'H1000' in fdict['headers']:
        print (convert_h1000)
#        validation_report.write(str(convert_h1000))
        
    else:
        print ("H1000 doesn't exist")
#        validation_report.write(str("H1000 doesn't exist"))
#        validation_report.write('\n')
        
    if 'H1001' in fdict['headers']:
        print (convert_h1001)
#        validation_report.write(str("convert_h1001"))
#        validation_report.write('\n')
        
    else:
        print ("H1001 doesn't exist")
#        validation_report.write(str("H1001 doesn't exist"))
#        validation_report.write('\n')
        
            
    print ('\n-----\n')
#    validation_report.write(str('\n-----\n'))
    
    return db_counts
    
def run_check_and_fix(rootpath):
    files_in_rin = FolderReader(rootpath)
    rin = os.path.split(rootpath)[1]
    
    total_file_sample_count = 0
    file_count = 0
    
    print ("Working on rin folder %s " % rin)
    validation_report.write(str("Working on rin folder %s " % rin))
#    validation_report.write('\n')
    
    for file in files_in_rin.fpaths:
        file, fdict, errors, delimiter, headers_fix = validate(file)
        db_counts = correct(file, fdict, errors, delimiter, rin, headers_fix)
        
        file_count = file_count + 1
        total_file_sample_count = total_file_sample_count + len(fdict['dlines'])
    
    print ('------')
    validation_report.write(str('------'))
    validation_report.write('\n')
    print ('db file count : ', db_counts[1])
    validation_report.write(str('db file count : ', db_counts[1]))
    validation_report.write('\n')
    print ('total_file_count : ', file_count)
    validation_report.write(str('total_file_count : ', file_count))
    validation_report.write('\n')
    print ('db sample count : ', db_counts[0])
    validation_report.write(str('db sample count : ', db_counts[0]))
    validation_report.write('\n')
    print ('total_file_sample_count : ', total_file_sample_count)
    validation_report.write(str('total_file_sample_count : ', total_file_sample_count))
    validation_report.write('\n')

if __name__ == "__main__":
    root = 'X:\_SS_RELOAD\PENDING'
    folders = os.listdir('X:\_SS_RELOAD\PENDING')
    for folder in folders:
        print ('Working on : ', os.path.join(root,folder))
        validation_report.write('Working on : %s' % str(os.path.join(root,folder)))
        validation_report.write('\n')
        try:
            run_check_and_fix(os.path.join(root,folder))
        except Exception as e:
            print ("Failed on rin : %s with exception : %s" % (folder,e))
            validation_report.write("Failed on rin: %s with exception : %s" % (folder,e))
            validation_report.write('\n')

#run_check_and_fix(os.path.join(root,'RE0008662'))















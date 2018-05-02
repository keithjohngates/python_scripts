# -*- coding: utf-8 -*-

import os
from database_connection import DatabaseConnection
from folder_reader import FolderReader
from file_reader import FileReader
from report_errors import ReportErrors
from data_records import DataRecords
from lookups import generate_h1000lk, h1001lk, valid_h1001_codes, dbconnection_string
from make_corrections import MakeCorrections
from gather_db_data import GatherDatabaseData
from insert_D_rows import InsertDRows
import sys
import multiprocessing as mp


def create_new_filename(delimiter, rin):
    get_new_filename = GatherDatabaseData(dbconnection_string, rin, delimiter).get_new_filename()
    return get_new_filename

def validate(file):
    fdict = FileReader(file).fdict 
    delimiter = fdict['delimiter']
    validator = ReportErrors(fdict,file,h1000lk)     
    errors = validator.run()
    headers_fix =  validator.set_to_fix()    
    return file, fdict, errors, delimiter, headers_fix

def correct(file, fdict, errors, delimiter, rin, headers_fix):        
    zone = MakeCorrections(errors, fdict, file, delimiter, rin).guess_zone()
    datum = MakeCorrections(errors, fdict, file, delimiter, rin).guess_geodetic()
    pivot_h0600 = MakeCorrections(errors, fdict, file, delimiter, rin).pivot_h0600()
    pivot_h0800 = MakeCorrections(errors, fdict, file, delimiter, rin).pivot_h0800()

def run_check_and_fix(rootpath):
    
    files_in_rin = FolderReader(rootpath)
    rin = os.path.split(rootpath)[1]
    
    for file in files_in_rin.fpaths:
        print ("FILE : %s" % os.path.split(file)[1])
        file, fdict, errors, delimiter, headers_fix = validate(file)  

if __name__ == "__main__":
    root = 'X:\_SS_RELOAD\PENDING'
    folders = os.listdir('X:\_SS_RELOAD\PENDING')
    
    for folder in folders:
        print ('FOLDER : %s \n' % os.path.join(root,folder))
        run_check_and_fix(os.path.join(root,folder))



#if __name__ == '__main__':
#    with mp.Pool() as pool:
#        tokens = pool.map(function_on_a_list, somelist)
#        print (tokens)
# -*- coding: utf-8 -*-

import os
#from database_connection import DatabaseConnection
from folder_reader import FolderReader
from file_reader import FileLoader
from report_errors import ReportErrors
from data_records import DataRecords
from lookups import h1000lk, h1001lk, sample_types_lk, dbconnection_string, elements, valid_h1001_codes
from make_corrections import MakeCorrections
from gather_db_data import GatherDatabaseData
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt, mpld3


#from insert_D_rows import InsertDRows

all_sample_types = set()
error_report = open(r'C:\Users\gatesk\Documents\_downhole_assays_fix\building_clean_versions_source_files\\ERRORS.txt','w')
unknown_sample_types =  open(r"C:\Users\gatesk\Documents\_downhole_assays_fix\building_clean_versions_source_files\unknown_sample_types.txt",'w')
justheaders =  open (r'C:\Users\gatesk\Documents\_downhole_assays_fix\building_clean_versions_source_files\just_headers.csv','w')

filebreak =   '###########################\n'
folderbreak = '***************************\n'
linebreak =   '---------------------------\n'
datanonnumerics = set()
datanonnumerics_lk = open(r'C:\Users\gatesk\Documents\_downhole_assays_fix\building_clean_versions_source_files\datanonnumerics_lk.txt','w')

def headers_suffix(header_list):
    counts = Counter(header_list) 
    for s,num in counts.items():
        if num > 1:
            for suffix in range(1, num + 1):
                header_list[header_list.index(s)] = s + str(suffix)
    return header_list

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False
    return True

def validate(file):
    loader = FileLoader()
    loader.load(file)
    
    fdict = loader.filedict
    assert fdict is not None
    
    dlines = loader.data_lines
    assert dlines is not None

    delimiter = fdict['delimiter']
    validator = ReportErrors(loader)
    errors = validator.run()
    
    make_df = (validator.data_line_errors, validator.h1000_dline_len_errors, validator.h1000_errors)
        
    headers_fix =  validator.set_to_fix()    
    
    return loader, file, fdict, errors, delimiter, headers_fix, make_df


def create_new_filename(delimiter, rin):
    get_new_filename = GatherDatabaseData(dbconnection_string, rin, delimiter).get_new_filename()
    return get_new_filename


def collect_h1000_fields(loader,delimiter,convert_h1000,convert_h1001,convert_h1000_units):
        
    if 'H1000' in loader.get_file_headers():
        h1000 = loader.get_file_headers_dict()['H1000']
        h1000.insert(0,'H1000_original')
    else:
        h1000 = []
        h1000.insert(0,'H1000_original')
        
    if 'H1001' in loader.get_file_headers():
        h1001 = loader.get_file_headers_dict()['H1001']
        h1001.insert(0,'H1001_original')
    else:
        h1001 = []
        h1001.insert(0,'H1001_original')

    if convert_h1000 is not None:
        convert_h1000 = convert_h1000.split(delimiter)
    else:
        convert_h1000 = []
        convert_h1000.insert(0,'H1000_convert_none')

    if convert_h1001 is not None:
        convert_h1001 = convert_h1001.split(delimiter)
    else:
        convert_h1001 = []
        convert_h1001.insert(0,'H1000_convert_none')
        
    if convert_h1000_units is not None:
        convert_h1000_units = convert_h1000_units.split(delimiter)
        convert_h1000_units= ['' if item == 'unk' else item for item in convert_h1000_units]

    else:
        convert_h1000_units = []
        convert_h1000_units.insert(0,'H1000_convert_none')
        
#    lengths = (len(h1000),len(h1001),len(convert_h1000),len(convert_h1001),len(convert_h1000_units))
    all_h1000_headers = [h1000,convert_h1000,h1001,convert_h1001,convert_h1000_units]

    return (all_h1000_headers)


def correct(file, loader, errors, rin, headers_fix, newfilename):
    corrector = MakeCorrections(errors, loader, file, rin)
    zone = corrector.guess_zone()
    datum = corrector.guess_geodetic()
    pivot_h0600 = corrector.pivot_h0600()
    pivot_h0800 = corrector.pivot_h0800()
    print (file)
#    fhead = os.path.split(file)[0]
    newfilename = os.path.join(r'C:\Users\gatesk\Documents\_downhole_assays_fix\converted',newfilename)
    print (newfilename)
    newfile = open(newfilename,'w')

    sample_types = set()
    
    if 'H1000' in loader.headers:
        convert_h1000 = corrector.convert_h1000(h1000lk)
    else:
        convert_h1000 = None
    
    if 'H1000' in loader.headers:
        convert_h1000_units = corrector.convert_h1000_units(h1000lk)
    else:
        convert_h1000_units = None
    
    if 'H1001' in loader.headers:
       convert_h1001 = corrector.convert_h1001(h1001lk)
    else:
        convert_h1001 = None
    
    delimiter = loader.delimiter
    db_corrected_headers = GatherDatabaseData(dbconnection_string, rin, delimiter).current_database_lookup_headers()
    headers_dict = loader.headers_dict

    error_report.write(linebreak)
    
    for i in db_corrected_headers:
        newfile.write(i+'\n')
    
    newfile.write(datum+'\n')
    newfile.write(zone+'\n')

    #H0600
    if headers_fix['H0600'] == True:
        for idx, i in enumerate(pivot_h0600):
            hfield = 'H060%s'% str(idx)
            i.insert(0, hfield)  
            newfile.write(delimiter.join(i)+'\n')
            if hfield == 'H0601':
                for samptype in i:
                    sample_types.add(samptype)
                
    else:
        if 'H0600' in headers_dict:
            newfile.write(delimiter.join(['H0600'] + headers_dict['H0600'])+'\n')
        else:
            newfile.write(delimiter.join(['H0600','Sample_Code','unk'])+'\n')

        if 'H0601' in headers_dict:
            newfile.write(delimiter.join(['H0601'] + headers_dict['H0601'])+'\n')
            for samptype in headers_dict['H0601']:
                sample_types.add(samptype)
        else:
            newfile.write(delimiter.join(['H0601','Sample_Type','unk'])+'\n')
            sample_types.add('unk')
            
        if 'H0602' in headers_dict:
            newfile.write(delimiter.join(['H0602'] + headers_dict['H0602'])+'\n')
        else:
            newfile.write(delimiter.join(['H0602','Sample_Date','unk'])+'\n')
        
    #H0800    
    if headers_fix['H0800'] == True:
        for idx, i in enumerate(pivot_h0800):
            hfield = 'H080%s'% str(idx)
            i.insert(0, hfield)
            newfile.write(delimiter.join(i)+'\n')
    else:
        
        if 'H0800' in headers_dict:
            newfile.write(delimiter.join(['H0800'] + headers_dict['H0800'])+'\n')
        else:
            newfile.write(delimiter.join(['H0800','Assay_Code','unk'])+'\n')
            
        if 'H0801' in headers_dict:
            newfile.write(delimiter.join(['H0800','Assay_Code','unk'])+'\n')
        else:
            newfile.write(delimiter.join(['H0801','Assay_description','unk'])+'\n')
            
        if 'H0802' in headers_dict:
            newfile.write(delimiter.join(['H0802'] + headers_dict['H0802'])+'\n')
        else:
            newfile.write(delimiter.join(['H0802','Assay_Date','unk'])+'\n')


    H1000fieldsdict = collect_h1000_fields(loader,delimiter,convert_h1000,convert_h1001,convert_h1000_units)
    
    converted_h1000_units = corrector.convert_h1000_units_to_consistent(h1001lk,H1000fieldsdict[-1])
    converted_h1000_units = converted_h1000_units.split(delimiter)
    converted_h1000_units[0] = 'units_from_H1000'
    
    converted_h1001_units =  H1000fieldsdict[-2]
    oldh1000 = H1000fieldsdict[0]
    newh1000 = H1000fieldsdict[1]
    
    for head in H1000fieldsdict:
        newfile.write(delimiter.join(head)+'\n')
    newfile.write(delimiter.join(converted_h1000_units)+'\n')
        
    if 'H1002' in headers_dict:
        H1002 = headers_dict['H1002']
        H1002 = [x.strip() for x in H1002]
        newfile.write(delimiter.join(['H1002'] + H1002)+'\n')
    
    for sampletype in sample_types:
        sampletype = sampletype.lower()
        if sampletype not in sample_types_lk:
            unknown_sample_types.write(sampletype+'\n')
        
    try:
        convert_h1000 = convert_h1000.split(delimiter)
    except:
        convert_h1000 = ''
    
    return oldh1000, newh1000, convert_h1000, converted_h1001_units, converted_h1000_units, newfile

def run_check_and_fix(rootpath):
    file_count = 0
    total_file_sample_count = 0
    
    files_in_rin = FolderReader(rootpath)
    rin = os.path.split(rootpath)[1]
    
    for file in files_in_rin.fpaths:        
        print ("FILE : %s" % os.path.split(file)[1])
        file_count = file_count + 1
        filecountstring = ('00%s' % file_count)
        loader, file, fdict, errors, delimiter, headers_fix, make_df = validate(file)
        sample_count_db , ss_file_count_db = GatherDatabaseData(dbconnection_string, rin, delimiter).current_database_lengths()
        newfilename = create_new_filename(delimiter, rin)
        newfilename = "%s_%s_%s_%s_%s.txt" % (newfilename[0], newfilename[1], filecountstring, 'SGC', newfilename[2]) 
        data_lines = loader.data_lines
        total_file_sample_count = total_file_sample_count + len(data_lines)
        
        oldh1000, newh1000, convert_h1000, convert_h1001, converted_h1000_units, newfile = correct(file, loader, errors, rin, headers_fix, newfilename)
        convert_h1000 = headers_suffix(convert_h1000)
        convert_h1000 = list(map(str.lower,convert_h1000))

        error_report.write(filebreak)
        error_report.write("FILE : %s \n" % os.path.split(file)[1])
        error_report.write("NEW FILE NAME : %s\n" % newfilename)

        if '' in valid_h1001_codes:
            valid_h1001_codes.remove('')
        
        if all(make_df) == False:
            try:
                data = DataRecords(convert_h1000,data_lines)
                #create a subdataframe of just the element columns to find none numerical values
                subdf = data.df.filter(items = elements, axis=1)
                for items in subdf.values:
                    for value in items:
                        if is_number(value) == False:
                            datanonnumerics.add(value)
                    
                subdf = subdf.apply(pd.to_numeric, errors = 'coerce')
                
                dfcoerced = data.df.apply(pd.to_numeric, errors = 'coerce')
                
                #compare the original units to the modified ones
                oldunits = convert_h1001
                newunits = converted_h1000_units
  
                for item in oldh1000:
                    error_report.write(str(item)+delimiter)
                error_report.write('\n')
                for item in newh1000:
                    error_report.write(str(item)+delimiter)
                error_report.write('\n')
                for item in oldunits:
                    error_report.write(str(item)+delimiter)
                error_report.write('\n')
                for item in newunits:
                    error_report.write(str(item)+delimiter)
                error_report.write('\n')
                
                
                try:
                    compareunits = list(zip(oldunits,newunits))
                    print (compareunits)
                    for item in compareunits:
                        if item[0] and item[1] in valid_h1001_codes:
                            if item[0] != item[1]:
                                error_report.write('UNIT_MISMATCH'+delimiter)
                        else:
                            error_report.write(''+delimiter)
                    error_report.write('\n')
#                    print (compareunits)
                except Exception as e:
                    print (e)
                    pass
                
                mins = pd.DataFrame(dfcoerced.describe().loc[['min']])
                for items in mins.values:
                    line = list(items)
                    for item in line:
                        error_report.write(str(item)+delimiter)
                    error_report.write('\n')

                maxs = pd.DataFrame(dfcoerced.describe().loc[['max']])
                for items in maxs.values:
                    line = list(items)
                    for item in line:
                        error_report.write(str(item)+delimiter)
                    error_report.write('\n')

                #get the max values add them to the units
                try:
                    maxvalues = []
                    for items in maxs.values:
                        line = list(items)
                        for item in line:
                            maxvalues.append(item)
                    #loop over the max values flagging the 10000ppm or >1%
                    checkhighs = list(zip(oldunits,maxvalues))
                except:
                    pass
                    
                for check in checkhighs:
                    if check[0] == 'ppm' and int(check[1]) > 10000:
                        error_report.write('HIGH'+delimiter)
                    elif check[0] == '%' and int(check[1]) > 1:
                        error_report.write('HIGH'+delimiter)
                    elif check[0] == 'ppb' and int(check[1]) > 10000000:
                        error_report.write('HIGH'+delimiter)
                    else:
                        error_report.write(''+delimiter)
                error_report.write('\n')
                    
                uniquesampletypes = []
                if 'sample_code' in list(data.df):
                    uniquesampletypes.extend(data.df['sample_code'].unique())
                    error_report.write('CHECK Unique sample codes: %s %s' % (delimiter, delimiter.join(uniquesampletypes))+'\n')
                else:
                    error_report.write("ERROR: sample_code field missing\n")
                            
                if 'sample_id' not in list(data.df):
                    error_report.write("ERROR: sample_id field missing\n")
                else:
                    error_report.write('CHECK: sample_id present\n')
            except Exception as e:
                print (e)
                

        
#        for col in list(subdf):
#            print (col)
#            fig = subdf[col].plot.hist(bins=25)
#            fig = plt.figure()
##            fig.show()
#            htmlfig = mpld3.fig_to_html(fig,template_type='general')
#            print (htmlfig)
##            with open('htmlfig_example.html','w') as fout:
##                fout.write(htmlfig)
##            mpld3.save_html(htmlfig,'test_now.html')
#            plt.pause(0.1)
            
#            try:
#                html = mpld3.fig_to_html(fig)
#                mpld3.save_html(html,'test_now.html')
#            except:
#                pass
        
            
        #write the dataframe out the file
        try:
            for item in data.df.values:
                newfile.write(delimiter.join(item)+'\n')
        except:
            pass
        
        newfile.close()
        print ('closing\n')

        for error in errors:
            error_report.write(str(error)+'\n')
        
    error_report.write(filebreak)
    error_report.write("\nFILE COUNT CHECK\n")
    error_report.write("FILE COUNT    : %s \n" % file_count)
    error_report.write("DB FILE COUNT : %s \n"% ss_file_count_db)
    error_report.write("\nSAMPLE COUNT CHECK\n")
    error_report.write("FILES SAMPLE COUNT    : %s \n" % total_file_sample_count)
    error_report.write("DB SAMPLE COUNT    : %s \n" % sample_count_db)
    
if __name__ == "__main__":
    root = r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix'
    folders = os.listdir(r'C:\Users\gatesk\Documents\_downhole_assays_fix\ones_to_fix')
    print (root)
    print (folders)
    
    for folder in folders:
        error_report.write(folderbreak)
        print ('\nFOLDER : %s' % os.path.join(root,folder))
        error_report.write('FOLDER : %s \n' % os.path.join(root,folder))
        run_check_and_fix(os.path.join(root,folder))
#    
    error_report.close()
#    unknown_sample_types.close()
#    justheaders.close()
#    
#    for item in datanonnumerics:
#        datanonnumerics_lk.write(item+'\n')
#    
#    datanonnumerics_lk.close()

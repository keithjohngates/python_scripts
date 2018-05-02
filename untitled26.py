# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 10:47:57 2018

@author: gatesk
"""

import os 
import shutil
import magic
import zipfile

local_mountpoint = r'R:\\'
base_folder = r"C:\Users\gatesk\Documents\_downhole_assays_fix\\"
unzippableroot = r'C:\Users\gatesk\Documents\_downhole_assays_fix\_unzippable'

file_exts = {
    "application/zip": "zip",
    "application/pdf": "pdf",
    "image/jpeg": "jpeg",
    "image/tiff": "tiff",
    "text/plain": "txt",
    "text/x-fortran": "f",
    "application/octet-stream": "bin"}


'''generator function to loop through a directory returning the filepaths of contents'''
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))


'''grab the rin folders as per the list and create folders and then move the files'''
def gen_RIN_folders(rin):
    rin_path = "%s/%s/%s" % (rin[0:3], rin[3:6], rin[6:9])
    rin_folder_path = os.path.join(local_mountpoint, rin_path)
    print (rin_folder_path)
    assert os.path.exists(rin_folder_path)
    assert os.path.isdir(rin_folder_path)
    out_folder = os.path.join(base_folder, rin)
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    else:
        pass
        print("output folder %s exists already." % out_folder)

    '''move the files into the folder structure'''
    rin_files = os.listdir(rin_folder_path)
    #print(len(rin_files))
    for f in rin_files:
        outfile = os.path.join(out_folder, f)
        infile = os.path.join(rin_folder_path, f)
        if not os.path.exists(outfile):
            print("Copying %s" % outfile)
            shutil.copy(infile, outfile)
        else:
            pass
            print("File %s exists already." % outfile)
            
def fix_a_file(file_path: str):
    detected = magic.from_file(file_path, mime=True)
    if detected in file_exts:
        print("%s -> %s" % (detected, file_exts[detected]))
        os.rename(file_path, file_path + "." + file_exts[detected])
    else:
        print("%s not found?" % (detected))
        assert False

def fix_files(rin):
    print(rin)
    for fin in absoluteFilePaths(os.path.join(base_folder,rin)):
        if str(fin).endswith("file"):
            try:
                fix_a_file(fin)
                print("Converted: " + str(fin))
            except Exception as e:
                print(e)
                print("Failed on:" + str(fin))
                pass
        else:
            pass
        
def unzip(rin):
    zip_extension = ".zip"
    rf = os.path.join(base_folder, rin)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(zip_extension): # check for ".zip" extension
            file_name = os.path.join(rf,item) # get full path of files
            print ("unzipping %s"%file_name)
            try:
                zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                zip_ref.extractall(rf) # extract file to dir
                zip_ref.close() # close file
                os.remove(file_name) # delete zipped file
            except Exception as e:
                newpath = os.path.join(unzippableroot,item)
                print (newpath)
                print (file_name)
                shutil.move(file_name,newpath)
                #print (file_name)
                print (e)
                pass


zip_extension = ".zip"
rf = os.path.join(base_folder, rin)    



            

import zipfile, re, os

def extract_nested_zip(zippedFile, toFolder):
    """ Extract a zip file including any nested zip files
        Delete the zip file(s) after extraction
    """
    with zipfile.ZipFile(zippedFile, 'r') as zfile:
        zfile.extractall(path=toFolder)
    os.remove(zippedFile)
    for root, dirs, files in os.walk(toFolder):
        for filename in files:
            if re.search(r'\.zip$', filename):
                fileSpec = os.path.join(root, filename)
                extract_nested_zip(fileSpec, root)




















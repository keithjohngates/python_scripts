# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 12:49:11 2017

@author: gatesk
"""

from sys import version_info
import os, zipfile, shutil #magic
from winmagic import magic

local_mountpoint = "R:\\"

if version_info[0] > 2:
    import tkinter as tk
    from tkinter.filedialog import askopenfilename, askdirectory
    from tkinter.messagebox import showerror, showinfo
else:
    import Tkinter as tk
    from tkFileDialog import askopenfilename, askdirectory
    from tkMessageBox import showerror, showinfo
    

def select_rin(entry):
    '''Select a file into entry'''
    rin = entry()
    if not rin:
        return

    entry.delete(0, tk.END)
    entry.insert(0, rin)

def select_folder(folder):
    '''Select folder destination'''
    fold_sel = askdirectory()
    if not fold_sel:
        return
        
    folder.delete(0, tk.END)
    folder.insert(0, fold_sel)    
    
def process(rin,fldout):
    print (rin,fldout)
    
    def getrinfolder(rin):
        rin_path = "%s/%s/%s" % (rin[0:3], rin[3:6], rin[6:9])
        rin_folder_path = os.path.join(local_mountpoint, rin_path)
        
        out_folder = os.path.join(fldout, rin)
        if not os.path.exists(out_folder):
            os.mkdir(out_folder)
        else:
            print("output folder %s exists already." % out_folder)
    
        rin_files = os.listdir(rin_folder_path)
        print(len(rin_files))
        for f in rin_files:
            outfile = os.path.join(out_folder, f)
            infile = os.path.join(rin_folder_path, f)
            if not os.path.exists(outfile):
                print("Copying %s" % outfile)
                shutil.copy(infile, outfile)
            else:
                print("File %s exists already." % outfile)
    
    getrinfolder(rin)
    rin_folders = os.listdir(fldout)
    
    file_exts = {
        "application/zip": "zip",
        "application/pdf": "pdf",
        "image/jpeg": "jpeg",
        "image/tiff": "tiff",
        "text/plain": "txt",
        "text/x-fortran": "f",
        "application/octet-stream": "bin"
    }
    
    def absoluteFilePaths(directory):
       for dirpath,_,filenames in os.walk(directory):
           for f in filenames:
               yield os.path.abspath(os.path.join(dirpath, f))
               
    def fixfile(file_path: str):
        detected = magic.from_file(file_path,mime=True)
        if detected in file_exts:
            print("%s -> %s" % (detected, file_exts[detected]))
            os.rename(file_path, file_path + "." + file_exts[detected])
        else:
            print("%s not found?" % (detected))
            assert False
    
    for i in absoluteFilePaths(fldout):
        if str(i).endswith("file"):
            try:
                fixfile(i)
                print ("Converted: " +str(i))
            except Exception as e:
                print (e)
                print ("Failed on:" +str(i))
                pass
        else:
            pass
    
    '''unzip the folders'''
    extension = ".zip"
    rin_folders = os.listdir(fldout)
    
    def unzip(fldout,my_zip):
            for item in os.listdir(fldout): # loop through items in dir
                if item.endswith(extension): # check for ".zip" extension
                    file_name = os.path.join(fldout,item) # get full path of files
                    try:
                        with zipfile.ZipFile(file_name) as zip_file:
                            for member in zip_file.namelist():
                                print ("the zip has : " +str(member))
                        '''keep the folders in the zip files'''          
                        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                        zip_ref.extractall(fldout) # extract file to dir
                        zip_ref.close() # close file
                        os.remove(file_name) # delete zipped file
                    except Exception as e:
                        pass
            print('...')
    
    for r in rin_folders:
        rf = os.path.join(fldout, r)
        for item in os.listdir(rf): # loop through items in dir
            if item.endswith(extension): # check for ".zip" extension
                file_name = os.path.join(rf,item) # get full path of files            
                unzip(rf,item)
			
def main():
    root = tk.Tk()
    root.title("GET RAW RIN FILES")

	# Destination Folder: _________________ [...]
    frame = tk.Frame(root)
    tk.Label(frame, text="Destination Folder:").pack(side=tk.LEFT)
    fold = tk.Entry(frame, width=60)
    fold.pack(side=tk.LEFT)
    tk.Button(frame, text="...",
              command=lambda: select_folder(fold)).pack(side=tk.LEFT)
    frame.pack()
    
	# Select RIN: _________________ [...]
    frame = tk.Frame(root)
    tk.Label(frame, text="Enter RIN:").pack(side=tk.LEFT)
    rin = tk.Entry(frame, width=60)
    rin.pack(side=tk.LEFT)
    frame.pack()
    
    # [Convert] [Quit]
    frame = tk.Frame(root)
    tk.Button(frame, text="Get Raw RIN Files", command=lambda: process(rin.get(),fold.get())).pack(side=tk.LEFT) 
    frame.pack(side=tk.LEFT)

    root.mainloop()
    print ('done')

if __name__ == "__main__":
    main()  
import os
import magic
import shutil
import multiprocessing as mp
import shelve

import threading
from queue import Queue


q = Queue(maxsize=0)
num_threads = 50


local_mountpoint = r'R:\\'
base_folder = r"C:\Users\gatesk\Documents\Lithology_files\RINS\\"
#rin_folders = os.listdir(base_folder)

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

#checked_dict =  shelve.open(r"G:\Transit\kgates\checked_dict_RINS.db")
#def gen_rin_list():
#    for i in checked_dict.items():
#        if i[1] == False:
#            q.put(i[0])

def gen_rin_list():
    with open(r"C:\Users\gatesk\Documents\_downhole_assays_fix\DDZ_ASSAY_DH_DRILL_UNIQUE_RINS.csv",'r') as rins:
        for line in rins:
            rin = line.strip().strip('"')
            q.put(rin)
   
gen_rin_list()

def get_files(q):
    while not q.empty():
        rin =  q.get()
        print (rin)
        gen_RIN_folders(rin)
        q.task_done()


def main():
    for i in range(num_threads):
      worker = threading.Thread(target=get_files, args=(q,))
      worker.start()

main()
print ('Please wait - we are working on it')
q.join()


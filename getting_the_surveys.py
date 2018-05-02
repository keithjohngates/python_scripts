import os, zipfile, shutil #magic
from winmagic import magic

local_mountpoint = "R:\\"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"

'''get the RIN LIST'''
RINS = []
RINSin = open(r"C:\Users\gatesk\Documents\missing_\RIN_LIST.txt",'r')
for line in RINSin:
    RINS.append(line.rstrip())
    
'''get the list of holes'''    
HOLEIDS = []
HOLEIDSin = open(r"C:\Users\gatesk\Documents\missing_\HOLEIDS_LIST.txt")
for line in HOLEIDSin:
    HOLEIDS.append(line.rstrip())

getlines = open(r"C:\\Users\\gatesk\\Documents\missing_\\linesofsurveydata.txt",'w')
    
'''GRAB THE RINS'''
for rin in RINS:
    rin_path = "%s/%s/%s" % (rin[0:3], rin[3:6], rin[6:9])
    #din_file_path = os.path.join(local_mountpoint, rin_path)
    rin_folder_path = os.path.join(local_mountpoint, rin_path)
    #print(rin_folder_path)
    assert os.path.exists(rin_folder_path)
    assert os.path.isdir(rin_folder_path)

#    if not os.path.exists(base_folder):
#        os.mkdir(base_folder)
#    else:
#        print("output folder %s exists already." % out_folder)

    out_folder = os.path.join(base_folder, rin)
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


rin_folders = os.listdir(base_folder)

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

for i in absoluteFilePaths(base_folder):
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
import zipfile
extension = ".zip"
base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH"
rin_folders = os.listdir(base_folder)

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    #print (rf)
    for item in os.listdir(rf): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.join(rf,item) # get full path of files
            #print (file_name)
            try:
                zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                zip_ref.extractall(rf) # extract file to dir
                zip_ref.close() # close file
                os.remove(file_name) # delete zipped file
            except Exception as e:
                print (file_name)
                print (e)
                pass


'''get the lines from survey files'''
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))
           
for i in absoluteFilePaths(r"C:\Users\gatesk\Documents\missing_"):
    try:
        #print (i)
        if 'urv' in str(i):
            if '78BP3' in open(i).read():
                print("This survey file has the hole you are looking for: " + str(i))
                os.startfile((i),'open')
                with open(i) as f:
                    for line in f:
                        if 'H1000' in line:
                            getlines.write(line)
                        if '78BP3' in line:
                            print (line)
                            getlines.write(line)
    except:
        pass
getlines.close()
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 08:02:46 2017

@author: gatesk
"""

import os
from winmagic import magic

base_folder = r"C:\\Users\\gatesk\\Documents\\missing_\\RINS_SEARCH\R00029712\\"

file_exts = {
    "application/zip": "zip",
    "application/pdf": "pdf",
    "image/jpeg": "jpeg",
    "image/tiff": "tiff",
    "text/plain": "txt",
    "text/x-fortran": "f",
    "application/octet-stream": "bin"
}


def fix_a_file(file_path: str):
    detected = magic.from_file(file_path,mime=True)
    if detected in file_exts:
        print("%s -> %s" % (detected, file_exts[detected]))
        os.rename(file_path, file_path + "." + file_exts[detected])
    else:
        print("%s not found?" % (detected))
        assert False


rin_folders = os.listdir(base_folder)

for r in rin_folders:
    rf = os.path.join(base_folder, r)
    print (rf)
    if os.path.isdir(rf):
        rin_files = os.listdir(rf)
        print("%s %s" % (r, len(rin_files)))
        for f in rin_files:
            print (f)
            ext = os.path.splitext(f)[1]
            print(ext)
            f_path = os.path.join(rf, f)
            if ext == '.file':
                fix_a_file(f_path)
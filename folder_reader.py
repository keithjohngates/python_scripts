# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:30:00 2018

@author: gatesk
"""
import os

class FolderReader(object):
    def __init__(self,folderpath):
        self.folderpath = folderpath
        self.rin = self.get_rin()
        self.files = self.get_file_names()
        self.fpaths = self.get_file_paths()

    def get_rin(self):
        return os.path.split(self.folderpath)[1]
    
    def get_file_names(self):
        return os.listdir(self.folderpath)
         
    def get_file_paths(self):
        filepaths = []
        for f in self.files:
            filepaths.append(os.path.join(self.folderpath,f))
            
        return filepaths
    

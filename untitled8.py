# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:12:17 2018

@author: gatesk
"""
#import os
#
#class iterfolder(object):
#    def __init__(self,folder):
#        self.index = 0
#        self.folder = folder
#        self.folders = os.listdir(self.folder)
#        
#    def __iter__(self):
#        return self
#    
#    def __next__(self):
#        try:
#            result = os.path.join(self.folder, self.folders[self.index])
#        except IndexError:
#            raise StopIteration
#        self.index += 1
#        return result
#    
#folders = iterfolder('X:\_SS_RELOAD\PENDING')
#
#def yieldfiles(folders):
#    for folder in folders:
#        files = os.listdir(folder)
#        for file in files:
#            yield file
#            
#for file in yieldfiles(folders):
#    print (file)

x = [1,2,3,4,5]
  
def func(x,y):
    return x*x
    

y  = [10,20,30,40,50]

z = list(zip(x,y))

z = list(zip(x,map(func,x,y)))

print (z)
zz  = list(zip(*z))
print (zz)
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:42:57 2018

@author: gatesk
"""
import pandas as pd

class DataRecords(object):
    def __init__(self):
        self.pandas_dfs = []    
    
    def build_pandas_data_df(self,columns,datarows):
        
        self.dataframe = pd.DataFrame(columns = columns)
        
        for row in datarows:
            self.dataframe.loc[len(self.dataframe)] = row
            
        self.pandas_dfs.append(self.dataframe)
            
    

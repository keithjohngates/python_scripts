# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:17:21 2017

@author: gatesk
"""

import pandas as pd
import numpy as np

survey = pd.read_csv(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_SVY_DATA_INTERNAL.csv",sep='|')
collar = pd.read_csv(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_LOC_DATA_INTERNAL_v2.csv",sep='|')

#surveyholes = survey.groupby(['RPT_ID','HOLEID'], as_index=False)
surveys_rpt_holes = set()
collar_rpt_holes = set()

for i, g in  survey.groupby(['RPT_ID','HOLEID'], as_index=False):
    surveys_rpt_holes.add(i)

for i, g in  collar.groupby(['RPT_ID','HOLEID'], as_index=False):
    collar_rpt_holes.add(i)
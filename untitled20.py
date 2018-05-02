# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:46:19 2017

@author: gatesk
"""

import pandas as pd

#DDZ_ASSAY_SURFSAMP = pd.read_csv(r"C:\Users\gatesk\Documents\SURFACE_SAMPLE_ASSAY_VALUE_ERRORS\DDZ_ASSAY_SURFSAMP_v5.csv",sep='|')
#DDZ_ASSAY_SURFSAMP_GROUPED = DDZ_ASSAY_SURFSAMP.groupby(['FILE_ID'], as_index=False).describe()
#DDZ_ASSAY_SURFSAMP_GROUPED.to_csv(r"C:\Users\gatesk\Documents\SURFACE_SAMPLE_ASSAY_VALUE_ERRORS\DDZ_ASSAY_SURFSAMP_GROUPED.csv",sep='|')

DD_SGC_DATA = 

DD_SGC_SAMPLE =  pd.read_csv(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_SGC_SAMPLE.csv",sep=',',encoding = "ISO-8859-1")

DD_RPT_FILE =  pd.read_csv(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_RPT_FILE.csv",sep=',',encoding = "ISO-8859-1")
DD_RPT_GENERAL =  pd.read_csv(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_RPT_GENERAL.csv",sep=',',encoding = "ISO-8859-1")


DD_SGC_SAMPLE_DD_RPT_FILE = pd.merge(DD_SGC_SAMPLE , DD_RPT_FILE, left_on = ['FILE_ID'], right_on = ['FILE_ID'], how = 'left')

DD_SGC_SAMPLE_DD_RPT_FILE_DD_RPT_GENERAL = pd.merge(DD_SGC_SAMPLE_DD_RPT_FILE, DD_RPT_GENERAL, left_on = ['RPT_ID_x'], right_on = ['RPT_ID'], how = 'left')

DD_SGC_SAMPLE_DD_RPT_FILE_DD_RPT_GENERAL.to_csv(r"C:\Users\gatesk\Documents\state_data_downloads\NSW\ASSAY_FME_48187571_1509400468370_3808\GSNSWDataset\DD_SGC_SAMPLE_DD_RPT_FILE_DD_RPT_GENERAL.csv",sep='|',index=False)
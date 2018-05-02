# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:56:30 2017

@author: gatesk
"""

import pandas as pd

#DDZ_ASSAY_SURFSAMP = pd.read_csv(r"C:\Users\gatesk\Documents\SURFACE_SAMPLE_ASSAY_VALUE_ERRORS\DDZ_ASSAY_SURFSAMP_v5.csv",sep='|')
#DDZ_ASSAY_SURFSAMP_GROUPED = DDZ_ASSAY_SURFSAMP.groupby(['FILE_ID'], as_index=False).describe()
#DDZ_ASSAY_SURFSAMP_GROUPED.to_csv(r"C:\Users\gatesk\Documents\SURFACE_SAMPLE_ASSAY_VALUE_ERRORS\DDZ_ASSAY_SURFSAMP_GROUPED.csv",sep='|')

DDZ_ASSAY_SURFSAMP_GROUPED =  pd.read_csv(r"C:\Users\gatesk\Documents\SURFACE_SAMPLE_ASSAY_VALUE_ERRORS\DDZ_ASSAY_SURFSAMP_GROUPED.csv",sep='|')
DD_RPT_FILE =  pd.read_csv(r"C:\Users\gatesk\Documents\missing_\_STAGE_DOS_REJOIN\DD_RPT_FILE.csv",sep='|',encoding = "ISO-8859-1")
DD_RPT_GENERAL =  pd.read_csv(r"C:\Users\gatesk\Documents\missing_\_STAGE_DOS_REJOIN\DD_RPT_GENERAL.csv",sep='\t',encoding = "ISO-8859-1")


DDZ_ASSAY_SURFSAMP_GROUPED_DD_RPT_FILE = pd.merge(DDZ_ASSAY_SURFSAMP_GROUPED , DD_RPT_FILE, left_on = ['FILE_ID'], right_on = ['FILE_ID'], how = 'left')

DDZ_ASSAY_SURFSAMP_GROUPED_DD_RPT_FILE_DD_RPT_GENERAL = pd.merge(DDZ_ASSAY_SURFSAMP_GROUPED_DD_RPT_FILE, DD_RPT_GENERAL, left_on = ['RPT_ID'], right_on = ['RPT_ID'], how = 'left')


DDZ_ASSAY_SURFSAMP_GROUPED_DD_RPT_FILE_DD_RPT_GENERAL.to_csv(r"C:\Users\gatesk\Documents\SURFACE_SAMPLE_ASSAY_VALUE_ERRORS\DDZ_ASSAY_SURFSAMP_GROUPED_DD_RPT_FILE_DD_RPT_GENERAL.csv",sep='|')


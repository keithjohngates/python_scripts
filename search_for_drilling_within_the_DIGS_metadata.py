# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:38:18 2017

@author: gatesk
"""

import pandas as pd
df = pd.read_csv(r"G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DiGS_GBjoinAll.csv",sep='|')

df['MR_SUBJECT_drill'] = df['MR_SUBJECT'].str.contains('svy|survey|SVY|Survey|surv|Surv|surveys|Surveys|SURVEY|SURVEYS|SURV')
df['AB_ABSTRACT_drill'] = df['AB_ABSTRACT'].str.contains('svy|survey|SVY|Survey|surv|Surv|surveys|Surveys|SURVEY|SURVEYS|SURV')
df['MD_DOCDESC_drill'] = df['MD_DOCDESC'].str.contains('svy|survey|SVY|Survey|surv|Surv|surveys|Surveys|SURVEY|SURVEYS|SURV')
df.sort(['SITE_ID'])
df[0:10000].to_csv(r"C:\Users\gatesk\Documents\DiGS_GBjoinAll_flagged_surveys.csv",sep='|')

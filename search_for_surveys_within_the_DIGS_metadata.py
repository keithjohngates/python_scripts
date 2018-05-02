i# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:38:18 2017

@author: gatesk
"""

import pandas as pd
df = pd.read_csv(r"G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\Archive\UpdateRINS_GS_REPORT\DiGS_GBjoinAll.csv",sep='|')

df['MR_SUBJECT_drill'] = df['MR_SUBJECT'].str.contains('svy|survey|SVY|Survey|surv|Surv|surveys|Surveys|SURVEY|SURVEYS|SURV')
df['AB_ABSTRACT_drill'] = df['AB_ABSTRACT'].str.contains('svy|survey|SVY|Survey|surv|Surv|surveys|Surveys|SURVEY|SURVEYS|SURV')
df['MD_DOCDESC_drill'] = df['MD_DOCDESC'].str.contains('svy|survey|SVY|Survey|surv|Surv|surveys|Surveys|SURVEY|SURVEYS|SURV')
df.sort_values(['SITE_ID'])

'''get the list of holes'''    
SITEIDS = []
SITEIDSin = open(r"C:\Users\gatesk\Documents\missing_\SITE_LIST.txt")
for line in SITEIDSin:
    line = str(int(line))
    line = line.lstrip('0') or '0'
    SITEIDS.append(line.rstrip())
    
dfsurveys =  df[df['SITE_ID'].isin(SITEIDS)]

dfsurveys.to_csv(r"C:\Users\gatesk\Documents\DiGS_GBjoinAll_flagged_surveys_all_sites.csv",sep='|')
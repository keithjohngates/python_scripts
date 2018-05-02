# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:38:18 2017

@author: gatesk
"""

import pandas as pd
df = pd.read_csv(r"G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Drilling\DiGS_GBjoinAll.csv",sep='|')

df['MR_SUBJECT_drill'] = df['MR_SUBJECT'].str.contains('drill|Drill|drilling|Drilling|drillhole|Drillhole|rc|RC|diamond|Diamond|aircore|Aircore|rab|Rab|RAB|percussion|Percussion|rotary|Rotary')
df['AB_ABSTRACT_drill'] = df['AB_ABSTRACT'].str.contains('drill|Drill|drilling|Drilling|drillhole|Drillhole|rc|RC|diamond|Diamond|aircore|Aircore|rab|Rab|RAB|percussion|Percussion|rotary|Rotary')
df['MD_DOCDESC_drill'] = df['MD_DOCDESC'].str.contains('drill|Drill|drilling|Drilling|drillhole|Drillhole|rc|RC|diamond|Diamond|aircore|Aircore|rab|Rab|RAB|percussion|Percussion|rotary|Rotary')
df.sort(['SITE_ID'])
df[0:10000].to_csv(r"C:\Users\gatesk\Documents\DiGS_GBjoinAll_flagged.csv",sep='|')

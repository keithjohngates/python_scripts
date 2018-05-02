# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:13:06 2018

@author: gatesk
"""

import sqlite3
import os
import geopandas as gpd
import pandas as pd


conn = sqlite3.connect(r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT.db")
print ('connected')

dbfs = [r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\Q20162\Q20162\DIP001\GIS_ESRI_Files\NT_DrillholeSamplesOpen.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\Q20162\Q20162\DIP001\GIS_ESRI_Files\NT_DrillholeCollarsOpen.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\Q20162\Q20162\DIP001\GIS_ESRI_Files\NT_RockChips.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\Q20162\Q20162\DIP001\GIS_ESRI_Files\NT_Soils.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\Q20162\Q20162\DIP001\GIS_ESRI_Files\NT_StreamSediments.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\Q20162\Q20162\DIP001\GIS_ESRI_Files\NT_WholeRock.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\Q20162\Q20162\DIP001\GIS_ESRI_Files\NT_Boundary.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\Q20162\Q20162\DIP001\GIS_ESRI_Files\NT_MapSheetIndex_100K.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\Q20162\Q20162\DIP001\GIS_ESRI_Files\NT_MapSheetIndex_250K.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_Geochemistry_shape\GEOCHEM_ROCKCHIPS.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_Geochemistry_shape\GEOCHEM_SOILS.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_Geochemistry_shape\GEOCHEM_STREAM_SEDIMENTS.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_Geochemistry_shape\GEOCHEM_WHOLEROCK.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_Drilling_shape\CORE_SAMPLES.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_Drilling_shape\DRILLHOLES.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_Drilling_shape\DRILLING_DIA_DIM_POSITIVE.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_Drilling_shape\DRILLING_DIA_KIMBERLITE.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_Drilling_shape\DRILLING_DIA_MACRO_POSITIVE.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_Drilling_shape\DRILLING_DIA_MICRO_POSITIVE.dbf",
r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\NT_Drilling_shape\PETROLEUMWELLS.dbf"]

for dbf in dbfs:
    name = os.path.split(dbf)[1]
    name = name.split('.')[0]
    print (name)
    df = gpd.read_file(dbf)
    df.to_csv(fr"C:\\Users\\gatesk\\Documents\\___aaa___PERSONAL\\NT\\{name}.csv")
    df = pd.read_csv(fr"C:\\Users\\gatesk\\Documents\\___aaa___PERSONAL\\NT\\{name}.csv",encoding = "ISO-8859-1")    
#    df.to_csv(fr"C:\\Users\\gatesk\\Documents\\___aaa___PERSONAL\\NT\\{name}.csv")
    df.to_sql(name, conn, flavor=None, schema=None, if_exists='fail', index=True, index_label='index', chunksize=None, dtype=None)
    conn.commit()
    
conn.close()
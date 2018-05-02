import pandas as pd
import os

filesin = ["G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Timbarra Geochem\Twelfth_annual_exploration_report,_EPLs_R00019462_2017-10-23\R00019462_Lab_ALS_KG_v2.xlsx",
 "G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Timbarra Geochem\Twelfth_annual_exploration_report,_EPLs_R00019462_2017-10-23\R00019462_Lab_ALS_Brisbane_KG_v2.xlsx",
"G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Timbarra Geochem\Twelfth_annual_exploration_report,_EPLs_R00019462_2017-10-23\R00019462_Lab_Analabs_KG_v2.xlsx",
"G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Timbarra Geochem\Twelfth_annual_exploration_report,_EPLs_R00019462_2017-10-23\R00019462_Lab_missing_KG_v2.xlsx",
"G:\Geosurvey\GeoInfo\Databases\Geoscience Data Warehouse\Data Management\Contractors_2017\Timbarra Geochem\Twelfth_annual_exploration_report,_EPLs_R00019462_2017-10-23\R00019462_Lab_SGS_Sydney_KG_v2.xlsx"]

for f in filesin:
    fname = os.path.split(f)
    fname = os.path.splitext(fname[1])
    df = pd.read_excel(open(f,'rb'), sheetname='Sheet1')
    df[['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']] = df[['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']].fillna(value=0)
    print (len(df))
    #print (df.Au_Technique.unique())
    #input()
    count = 0
    for i, g in df.groupby(['Au_Technique','Bi_Technique','Mo_Technique','Ag_Technique','As_Technique','Cu_Technique','Pb_Technique','Zn_Technique']):
        g=g.dropna(axis=1,how='all')
        #colcount = "'',"*(len(list(g)))
        #print (colcount)
        #g.loc[0]=[str(colcount)]
        g.to_csv('{}.csv'.format('C:\\Users\\gatesk\\.spyder-py3\\R00019462\\'+str(fname[0])+'_'+str(i).replace('/','_')), header=True, index=False,sep='|')
        count = count+len(g)
    print (count)
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:07:02 2018

@author: gatesk
"""
import shelve
import matplotlib.pyplot as plt

print ('Reading data')
db =  shelve.open(r"G:\Transit\kgates\DDZ_ASSAY_DH_DRILL_UNIQUE_RINS.db")
print ('Reading check dict')
checked_dict =  shelve.open(r"G:\Transit\kgates\checked_dict_RINS.db")
    
to_check = input('check for new? (y/n)')
if to_check == 'y':
    print ('Adding new items to the check dictonary')
    for rin, state in db.items():
        print (f'checking rin {rin}')
        if rin not in checked_dict:
            print (f'adding {rin}')
            checked_dict[rin] = None
        else:
            pass
else:
    pass

#with shelve.open(r"G:\Transit\kgates\checked_dict_RINS.db") as checked_dict:
#    remaining = 0
#    for rin, state in checked_dict.items():
#        if checked_dict[rin] == None:
#            remaining = remaining +1
#    print (remaining)

counter = 0
print ('Commencing the processing....')
print ("Please enter 't: True, e: Error, q: Quit'")
with shelve.open(r"G:\Transit\kgates\checked_dict_RINS.db") as checked_dict:
    print (len(checked_dict))
    for rin, state in checked_dict.items():
            if checked_dict[rin] == None:
                counter = counter + 1
                df = db[rin]
                dfau = df.loc[df['ELEMENT'] == 'Au']
                #print (list(dfau))
                print (counter)
                print (rin)
                print (dfau[['ELEMENT', 'RESULT', 'UNITS', 'CONV_ELEMENT', 'CONV_RESULT', 'CONV_UNITS', 'HEADING']].describe())
                print (dfau['CONV_UNITS'].describe())
                if len(dfau) == 0:
                    print ("no gold")
                    pass
                
                
                try:
                    dfau['CONV_RESULT'].plot.hist()
                    plt.show()
                    
                    
                    checked = input()
                    
                    
                except TypeError as e:
                    print (e)
                    checked = ""
                    pass
                
                
                if checked == "":
                    checked_dict[rin] = True
                elif checked == ';':
                    checked_dict[rin] = False
                else:
                    break
                if counter %101 == 0:
                    print ("KEEP GOING !!!")
            else:
                pass
            
            
        
#import pandas as pd
#from scipy import stats
#values = []
#
#for rin,df in db.items():
#        dfau = df.loc[df['ELEMENT'] == 'Au']
#        dfau = pd.DataFrame(db[rin]['CONV_RESULT'])
#        dfau = df.loc[df['ELEMENT'] == 'Au']
#        dfau = dfau[~(dfau['CONV_RESULT'] < 0.0001)]
#        print (f"working on {rin}")
#        #print (kurtosis(dfau['CONV_RESULT']))
#        if len(dfau) > 8:
#            #normality = scipy.stats.kstest(dfau['CONV_RESULT'], "lognorm", scipy.stats.lognorm.fit(dfau['CONV_RESULT']))
#            #print (normality)
#            #print (scipy.stats.kstest(dfau['CONV_RESULT'], "lognorm", scipy.stats.lognorm.fit(dfau['CONV_RESULT'])))
#            #values.append(normality)
#            k2, p = stats.normaltest(dfau['CONV_RESULT'])
#            values.append((rin, k2))
            
            
         
import csv, os
from collections import defaultdict
from H1000_survey_lk import surveyheaders, surveyheaders2
import re
import pandas as pd

rinholes = defaultdict(list)
root = r'C:/Users/gatesk/Documents/missing_/RINS_SEARCH'

problemfiles = open("problem_files.txt",'w')

with open(r"C:/Users/gatesk/Documents/missing_/RIN_HOLES_MASTER.csv") as master:
    rdr = csv.reader(master, delimiter='|')
    for line in rdr:
        #print (line)
        rin = line[2]
        hole = line[5]
        rinholes[hole].append(rin)

all_rins = set()

for hole,rins in rinholes.items():
    for rin in rins:
        all_rins.add(rin)
        
rinfiles = defaultdict(list)

def findsurveys(fold):
    def absoluteFilePaths(directory):
       for dirpath,_,filenames in os.walk(directory):
           for f in filenames:
               yield os.path.abspath(os.path.join(dirpath, f))
    
    def is_a_survey(headerline):
        elements = re.split('[ \t,]', headerline)
        #if headers suggests it is a survey file
        for e in elements:
           if e in  surveyheaders:
               return True
                
        
    def isH1000(fin):
        with open(fin) as f:
            for idx, line in enumerate(f):
                if idx > 100:
                    break
                if line.startswith('H1000'):
                    return idx,line
                if line.startswith('"H1000'):
                    return idx,line
            return -1, None
    
    surveyfiles = []
    
    def detect_delimter(fin):
        try:
            with open(fin, 'r') as f:
                dialect = csv.Sniffer().sniff(f.read())    
            return dialect.delimiter
        except Exception as e:
            problemfiles.write("failed to detect delimiter|"+str(fin)+'|'+str(e)+'\n')
            print (fin,e)
            pass
            
    
    for f in absoluteFilePaths(fold):
        ext = os.path.splitext(f)[1]
        if ext not in ['.txt']:
            continue
        idx, line = isH1000(f)
        if idx != -1:
            if is_a_survey(line):
                sep = detect_delimter(f)
                surveyfiles.append([f,idx,line,None,sep])
            
    return surveyfiles

surveyfiles_by_rin = defaultdict(list)

for rin in all_rins:
    rinfolder = os.path.join(root,rin)
    #print (rinfolder)
    foundsurveys = findsurveys(rinfolder)
    #print (rin,len(foundsurveys))
    #print (rin,foundsurveys)
    surveyfiles_by_rin[rin] = foundsurveys

'''cleanup the headers to dict mappings for survey files'''
for rin,surveys in  surveyfiles_by_rin.items():
    #print (rin,len(surveys))
    for s in surveys:
        f = s[0]
        idx = s[1]
        line = s[2]
        elements = re.split('[ \t,]', line.strip())
        #print (elements)
        newheader = []
        for e in elements:
            if e in surveyheaders:
                realheader = surveyheaders[e]
                newheader.append(realheader)
            elif e in surveyheaders2:
                realheader = surveyheaders2[e]
                newheader.append(realheader)
            else:
                newheader.append(e)
        s[3] = newheader
        #print (s)
        
        
survey_dfs = dict()

for rin,surveys in  surveyfiles_by_rin.items():
    for s in surveys:
        f = s[0]
        idx = s[1]
        line = s[2]
        newheaders = s[3]
        delimiter = s[4]
        #print (rin,f)
        #assert "BHID" in newheaders
        #assert "DEPTH" in newheaders
        if "BHID" not in newheaders:
            #print ("rejecting file - no BHID: ", newheaders)
            continue
        if "DIP" not in newheaders:
            print ("rejecting file - no DIP: ", newheaders)
            continue
        #print (idx)
        print (idx,f,delimiter)
        try:
            df = pd.read_csv(f,sep=delimiter,skiprows=idx,names=newheaders)
            #df = pd.read_csv()
            #print (df)
            #return df
        except UnicodeDecodeError as readerror:
            df = pd.read_csv(f,sep=delimiter,skiprows=idx,names=newheaders,encoding='windows-1252')
            #return df
        except Exception as e:
            #raise (e)
            print ("failed to read into df: ",idx,f,e)
            problemfiles.write("failed to read into df|"+'|'+str(f)+'|'+str(e)+'\n')
            #os.startfile((f),'open')
            pass
        print (f)
        survey_dfs[f] = df
                
#print (len(survey_dfs))
merged = pd.DataFrame(columns=['BHID_COL','RIN','FILE','BHID','DEPTH','DIP','AZI_UNK','AZI_MAG','AZI_UTM','AZI_LOCAL'])
col_list = ['BHID_COL','RIN','FILE','BHID','DEPTH','DIP','AZI_UNK','AZI_MAG','AZI_UTM','AZI_LOCAL']

for hole,rins in rinholes.items():
    for rin in rins:
        surveys = surveyfiles_by_rin[rin]
        for s in surveys:
            try:
                f = s[0]
                df = survey_dfs[f]
                df['RIN'] = rin
                df['FILE'] = f
                df['BHID_COL'] = hole
                #print (survey_dfs[s[0]])
                #print (hole)
                #print ('\n')
                cols_we_have = [col for col in col_list if col in df]
                holes_df  = df[df['BHID'] == hole]
                holes_df = holes_df[cols_we_have]
                #print (type(holes_df))
                merged = merged.append(holes_df)
                #print (len(merged))
            except:
                pass

merged = merged.sort_values(by=['BHID','DEPTH'])
merged.to_csv('merged_out_v7.csv',sep='|',index=False)

problemfiles.close()
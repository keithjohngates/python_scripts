# -*- coding: utf-8 -*-

dbconnection_string = r'DSN=GEODWH;UID=gatesk;PWD=Oldsp00n'

key_headers = ['H0002','H0004','H0100','H0202','H0501','H0531','H0600','H0601','H0800','H0801','H0802','H0803','H1000','H1001','H1002','H1003']

valid_h1001_codes = ['metres','degrees','ppm','ppb','%','g/bcm','ppt']

valid_sample_codes = ['soil','rockchip','float','stream','costean','lag','minespoil','drillspoil','water','vegetation','unknown','surf_drill']

valid_template_formats = ['LOC','DG1','DGC','DS1','SVY','SG1','SGC','DL1','LTH']

validzones = ['54','55','56','57']

validdatums = ['GDA','AGD','MGA','AMG']

h1001lk = {'pct':'%','percent':'%','m':'metres','units':''}

valid_h1001_codes = ['metres','degrees','ppm','ppb','%','g/bcm','ppt']

#TODO: valid_tenement_strings = []

def generate_h1000lk():
    H1000lk = dict()
    with open(r"h1000lk_conversions.csv",'r') as fin:
        for line in fin:
            items = line.split(',')
            H1000lk[items[0]] = items[1:]    
    return H1000lk

h1000lk = generate_h1000lk()



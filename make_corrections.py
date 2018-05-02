# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 09:24:17 2018

@author: gatesk
"""
import itertools

class MakeCorrections(object):
    def __init__(self,errors,fdict,file, delimiter, rin):
        self.file = file
        self.rin = rin
        self.delimiter = delimiter
        self.errors = errors
        self.fdict = fdict        
        self.potential_h0500_fields = []
        self.pivot_h0600_fields = []
        self.pivot_h0800_fields = []
        
        for i in ['H0502','H0503','H0504','H0505','H0506','H0507','H0508','H0509','H0530']:
            try:
                for item in fdict['headers_dict'][i]:
                    self.potential_h0500_fields.append(item)
            except:
                pass
            
        for i in ['H0600','H0601','H0602','H0603','H0604','H0605','H0606','H0607','H0608','H0609']:
            try:
                self.pivot_h0600_fields.append(fdict['headers_dict'][i])
            except:
                pass
            
        for i in ['H0800','H0801','H0802','H0803','H0804','H0805','H0806','H0807','H0808','H0809']:
            try:
                self.pivot_h0800_fields.append(fdict['headers_dict'][i])
            except:
                pass
            
        self.zone = self.guess_zone()
        self.datum  = self.guess_geodetic()
        self.pivot_h0600()
        self.pivot_h0800()
        
    def guess_zone(self):
        validzones = ['55','56','57','54']
        found = None
        for zone in validzones:
            for item in self.potential_h0500_fields:
                if str(zone) in str(item):
                    found = self.delimiter.join(['H0531','Projection_zone',str(zone)])
        if found is not None:
            return found
        else:
            return self.delimiter.join(['H0531','Projection_zone','unk_zone'])
                 
    def guess_geodetic(self):
        validdatums = ['GDA','AGD','MGA','AMG']
        found = None
        for datum in validdatums:
            for item in self.potential_h0500_fields:
                if str(datum) in str(item):
                    found = self.delimiter.join(['H0501','Geodetic_datum',str(datum)])
        if found is not None:
            return found
        else:
            return self.delimiter.join(['H0501','Geodetic_datum','unk_datum'])    
                
    def pivot_h0600(self):
        pivoted_h0600 = list(map(list, itertools.zip_longest(*self.pivot_h0600_fields, fillvalue='unk')))
        return pivoted_h0600
    
    def pivot_h0800(self):
        pivoted_h0800 = list(map(list, itertools.zip_longest(*self.pivot_h0800_fields, fillvalue='unk')))
        return pivoted_h0800
    
    
    def convert_h1000(self,h1000lookup):
        new_h1000 = []
        converted_h1000 = self.fdict['headers_dict']['H1000']
        for item in converted_h1000:
            item = item.strip()
            if item in h1000lookup:
                converted_value = h1000lookup[item]
                #print ('converting %s : %s '% (item, converted_value[0]))
                new_h1000.append(converted_value[0])
            else:
                converted_value = 'NEEDS_DEF'
                #print ('%s %s' % (item, converted_value))
                new_h1000.append(converted_value)
        new_h1000.insert(0,'H1000')
        return self.delimiter.join(new_h1000)
    
    
    def convert_h1001(self,h1001lookup,valid_h1001_codes):
        new_h1001 = []
        converted_h1001 = self.fdict['headers_dict']['H1001']
        for item in converted_h1001:
            item = item.strip()
            if item in valid_h1001_codes:
                new_h1001.append(item)
            else:
                if item in h1001lookup:
                    converted_value = h1001lookup[item]
                    new_h1001.append(converted_value)
                else:
                    converted_value = 'NEEDS_DEF'
                    new_h1001.append(converted_value)
        new_h1001.insert(0,'H1001')
        return self.delimiter.join(new_h1001)
    

    def convert_sample_types(self,h0601):
        #must be completed post pivot
        pass
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
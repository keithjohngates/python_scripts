# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:31:21 2018

@author: gatesk
"""
from lookups import h1000lk
from lookups import valid_h1001_codes
from lookups import valid_template_formats
from lookups import validzones
from lookups import validdatums

class ReportErrors(object):
    def __init__(self,fdict,filepath,h1000lk):
        self.validation_status = True
        self.H0202_update_db = False
        self.H0002_update_db = True
        self.H0004_update_db = True
        self.H0100_update_db = True
        self.H0101_update_db = True
        self.H0102_update_db = True
        self.H0501_update_db = False
        self.H0531_update_db = False
        self.H0600_pivot = False
        self.H0800_pivot = False
        
        self.filepath = filepath
        self.fdict = fdict
        self.h1000lk = h1000lk
        
    def run(self):
        print ("\n-----\nValidating %s\n-----\n" % self.filepath)
        errors = []
        errors.extend(self.data_len_check())
        errors.extend(self.data_key_header_check())
        errors.extend(self.h0202_check())
        errors.extend(self.h0501_check())
        errors.extend(self.h0531_check())
        errors.extend(self.h0600_pivot_check())
        errors.extend(self.h0800_pivot_check())
        errors.extend(self.h1000_conversion_check())
        errors.extend(self.h1001_check())
        return errors
    
    
    def data_len_check(self):
        self.len_H1000_line = len(self.fdict['headers_dict']['H1000'])
        self.len_d_lines = len(self.fdict['dlines_set'])
        self.len_d_lines_set = self.fdict['dlines_set']
        errors = []
        
        if self.len_d_lines == 0:
            errors.append('Failed: No D lines are present')
            self.validation_status = False
            
        elif self.len_d_lines > 1:
            errors.append('Failed: Data lines have inconsistent lengths : %s' % str(self.len_d_lines))
            self.validation_status = False
                                
        elif self.len_d_lines == 1:
            print("Passed: All data lines have consistent lengths")
            
        else:
            errors.append("Failed: Some other reason")
            self.validation_status = False
            
        if self.len_d_lines == 1:
            if list(self.len_d_lines_set)[0]-1 != self.len_H1000_line:
                errors.append('Failed: H1000 (%s) and data lines (%s) have inconsistent lengths '% (self.len_H1000_line, list(self.len_d_lines_set)[0]-1))
                self.validation_status = False
            else:
                print("Passed: H1000 and data lines have consistent lengths")
        return errors


    def data_line_count(self):
        pass
        

    def data_key_header_check(self):
        self.h1000_headers = self.fdict['headers']
        errors = []
        headerrepeat_check = len(self.h1000_headers) - len(set(self.h1000_headers))
        
        if headerrepeat_check != 0:
            errors.append("Failed: Some headers are repeated")
            self.validation_status = False
        if headerrepeat_check == 0:
            print ("Passed: No headers are repeated")
        return errors
    
    def h0600_pivot_check(self):
        errors = []
        self.h0600 = self.fdict['headers_dict']['H0600']
        checklist = ['desc','date','type']
        for idx, i in enumerate(checklist):
            if i in str(self.h0600[1:]).lower():
                errors.append('H0600 (%s) appears to need to be pivoted due to %s' % (self.h0600, i))
                self.validation_status = False
                self.H0600_pivot = True            
        return errors


    def h0800_pivot_check(self):
        errors = []
        self.h0800 = self.fdict['headers_dict']['H0800']
        checklist = ['desc','date','comp']
        for i in checklist:
            if i in str(self.h0800[1:]).lower():
                errors.append('H0800 (%s) appears to need to be pivoted due to %s' % (self.h0800, i))
                self.validation_status = False
                self.H0800_pivot = True
        return errors
    
    
    def h0501_check(self):
        errors = []
        self.validzones = validzones
        
        if 'H0501' in self.fdict['headers_dict']:
            self.h0501 = self.fdict['headers_dict']['H0501'][1]
            if self.h0501.lower() not in validzones:
                errors.append("H0501 (zone) value: (%s) is not valid" % self.h0501)
                self.validation_status = False
                self.H0501_update_db = True
        else:
            errors.append("H0501 (zone) header row does not exist")
            self.validation_status = False
            self.H0501_update_db = True
        return errors


    def h0531_check(self):
        errors = []
        self.validdatums = validdatums
        
        if 'H0531' in self.fdict['headers_dict']:
            self.h0531 = self.fdict['headers_dict']['H0531'][1]
            if self.h0531.lower() not in validdatums:
                errors.append("H0531 (geodetic-datum) value: (%s) is not valid" % self.h0531)
                self.validation_status = False
                self.H0531_update_db = True
        else:
            errors.append("H0531 (geodetic-datum) header row does not exist")
            self.validation_status = False
            self.H0531_update_db = True
        return errors


    def h0202_check(self):
        errors = []
        self.valid_template_formats = valid_template_formats
        
        if 'H0202' in self.fdict['headers_dict']:
            self.h0202 = self.fdict['headers_dict']['H0202'][1]
            if self.h0202.lower() not in valid_template_formats:
                errors.append("H0202 (template-format) value: (%s) is not valid" % self.h0202)
                self.validation_status = False
                self.H0202_update_db = True
        else:
            errors.append("H0202 (template-format) header row does not exist")
            self.validation_status = False
            self.H0202_update_db = True
        return errors


    def h1000_conversion_check(self):
        errors = []
        
        if 'H1000' in self.fdict['headers']:
            
            for item in self.fdict['headers_dict']['H1000']:
                if item.strip() not in h1000lk:
                    #errors.append("The following items do exist in h1000 lookup table: %s" % item )
                    with open('h1000lk_additions.csv', 'a') as h1000lk_additions:
                        h1000lk_additions.write(str(item)+'\n')
                    self.validation_status = False
                    
        return errors
                
    
    def h1001_check(self):
        errors = []
        self.valid_h1001_codes = valid_h1001_codes
        
        if 'H1001' in self.fdict['headers']:
            
            for item in self.fdict['headers_dict']['H1001']:
                if item.strip() not in valid_h1001_codes:
                    #errors.append("The following value isn't valid for h1001: %s" % item )
                    with open('h1001lk_additions.csv', 'a') as h1001lk_additions:
                        h1001lk_additions.write(str(item)+'\n')
                    self.validation_status = False
                
        return errors
    
    
    def set_to_fix(self):
        set_fixes = {
        'H0202': self.H0202_update_db,
        'H0002': self.H0002_update_db,
        'H0004': self.H0004_update_db,
        'H0100': self.H0100_update_db,
        'H0101': self.H0101_update_db,
        'H0102': self.H0102_update_db,
        'H0501': self.H0501_update_db,
        'H0531': self.H0531_update_db,
        'H0600': self.H0600_pivot,
        'H0800': self.H0800_pivot
        }
        return set_fixes
    
    












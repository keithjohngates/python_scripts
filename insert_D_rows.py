# -*- coding: utf-8 -*-




class InsertDRows(object):
    def __init__(self,fdict):
        self.fdict = fdict
        self.otherlines = fdict['other_lines']
        self.headers = fdict['headers']
        self.fix_other_lines()
        
    def fix_other_lines(self):
        if 'H1000' in self.headers:
            self.H1000len = len(self.fdict['headers_dict']['H1000'])
        
            if len(self.otherlines[0]) != 0:
                if len(self.otherlines[1]) == 1:
                    otherlineslen = int(list(self.otherlines[1])[0])
                    if int(self.H1000len)+1 == otherlineslen:
                        print ("Should be safe to insert 'D' rows in overwrite mode")
                else:
                    print ("Data rows have inconsistent lengths")
                    
        else:
            print ("Doesn't contains H1000 records")
#            print (self.H1000len, self.otherlines[1])
#            for item in self.otherlines[0]:
#                print (item)
                
                
            




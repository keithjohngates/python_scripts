# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:56:47 2017

@author: gatesk
"""
import re



BHID = '79BHIG'

h = re.compile(".*?".join(BHID))
print (h.match('79 B H-IG '))
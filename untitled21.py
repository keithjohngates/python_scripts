# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:04:08 2017

@author: gatesk
"""

import pandas as pd
import sqlite3
conn = sqlite3.connect('samples_dict.db')
c = conn.cursor()

DD_RPT_FILE = pd.read_sql_query("Select * from DD_RPT_FILE", conn)
DD_RPT_GENERAL = pd.read_sql(DD_RPT_GENERAL, conn)

DD_SGC_SAMPLE = pd.read_sql(DD_SGC_SAMPLE, conn)
DD_SGC_DATA = pd.read_sql(DD_SGC_DATA, conn)



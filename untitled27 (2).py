# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 07:33:03 2017

@author: gatesk
"""


import pandas as pd
import sqlite3
from flask import Flask

app = Flask(__name__)
connection_db = r"C:\Users\gatesk\Documents\SURFACE_SAMPLE_ASSAY_VALUE_ERRORS\samples_dict.db"
table = None

def load_table(connection_db):
    print ('....')
    print ("importing data from {}".format(connection_db))
    conn = sqlite3.connect(connection_db)
    DD_RPT_FILE = pd.read_sql_query("Select * from DD_RPT_FILE", conn)
    return DD_RPT_FILE
    
@app.route("/raw")
def read_df():
    html  = table.to_html()
    return html

@app.route("/")
def index_df():
    html = []
    for idx, row in table.iterrows():
        template = '<a href="/file_id/%d">%s</a>'
        file_id = int(row['FILE_ID'])
        entry = template %(file_id,file_id)
        html.append(entry)
        
    html  = '\n'.join(html)
    return html

@app.route("/file_id/<file_id>")
def show_file(file_id):
    file_id = int(file_id)
    return "file_id: {}".format(file_id)

if __name__== "__main__":
    table  = load_table(connection_db)
    app.run(debug=True)
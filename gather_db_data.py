# -*- coding: utf-8 -*-


from database_connection import DatabaseConnection
from lookups import dbconnection_string

class GatherDatabaseData(object):
    def __init__(self,rin,delimiter):
        self.rin = rin
        self.delimiter = delimiter
        
    def current_database_lookup_headers(self):
        dbconn = DatabaseConnection(dbconnection_string, self.rin, self.delimiter)
        dbconn.connect()
        rpt_general = dbconn.rpt_general()
        rpt_file = dbconn.rpt_file()
        rpt_file = rpt_file.reset_index(drop=True)
        filetype = rpt_file.FILETYPE[0]
        version_db = rpt_general[5]
        date_db = rpt_general[1]
        tenement_db = rpt_general[0] 
        holder_db = rpt_general[6]
        project_db = rpt_general[7]

        sample_count_db = rpt_general[3]
        ss_file_count_db = len(rpt_file)
        
        print ('sample_count_db: ', sample_count_db)
        print ('ss_file_count_db: ', ss_file_count_db)
        
        db_corrected_headers = [
        self.delimiter.join(['H0002','Version',str(version_db)]),
        self.delimiter.join(['H0004','Reporting end date',str(date_db)]),
        self.delimiter.join(['H0100','Tenement_ID',str(tenement_db)]),
        self.delimiter.join(['H0101','Tenement_holder',str(holder_db)]),
        self.delimiter.join(['H0102','Project_name',str(project_db)]),
        self.delimiter.join(['H0202','Template_format',str(filetype)])
        ]
         
        return db_corrected_headers

    def current_database_record_lengths(self):
        pass


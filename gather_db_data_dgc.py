# -*- coding: utf-8 -*-


from database_connection_dgc import DatabaseConnection
dbconnection_string = r'DSN=GEODWH;UID=gatesk;PWD=Oldsp00n'


class GatherDatabaseData(object):
    def __init__(self, dbconn, rin, delimiter):
        self.dbconn = dbconn
        self.rin = rin
        self.delimiter = delimiter
        dbconn = DatabaseConnection(self.dbconn, self.rin, self.delimiter)
        dbconn.connect()
        self.rpt_general = dbconn.rpt_general()
        self.rpt_file = dbconn.rpt_file()
        self.rpt_file = self.rpt_file.reset_index(drop=True)
        
    def current_database_lookup_headers(self):
        filetype = self.rpt_file.FILETYPE[0]
        version_db = self.rpt_general[5]
        date_db = self.rpt_general[1]
        tenement_db = self.rpt_general[2] 
        holder_db = self.rpt_general[6]
        project_db = self.rpt_general[7]

        db_corrected_headers = [
        self.delimiter.join(['H0002','Version',str(version_db)]),
        self.delimiter.join(['H0004','Reporting end date',str(date_db)]),
        self.delimiter.join(['H0100','Tenement_ID',str(tenement_db)]),
        self.delimiter.join(['H0101','Tenement_holder',str(holder_db)]),
        self.delimiter.join(['H0102','Project_name',str(project_db)]),
        self.delimiter.join(['H0202','Template_format',str(filetype)]) 
        ]
        return db_corrected_headers
    
    def current_database_lengths(self):
        sample_count_db = self.rpt_general[3]
        ss_file_count_db = len(self.rpt_file)
        
        print ('sample_count_db: ', sample_count_db)
        print ('ss_file_count_db: ', ss_file_count_db)
        return sample_count_db , ss_file_count_db
    
    def get_new_filename(self):
        rin = self.rin
        tenement_db = self.rpt_general[2].split(',')[0]
        version_db = self.rpt_general[5]
        return rin,tenement_db,version_db
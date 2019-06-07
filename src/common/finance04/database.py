import pyodbc

__author__ = 'nabee1'

class Database(object):
    URI = "###"
    DATABASE = "###"
    cnxn = None

    @staticmethod
    def initialize():
        Database.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + Database.URI + ';DATABASE=' \
                                       + Database.DATABASE + ';Trusted_Connection=yes;APP=nabeelh python3.7 via pyodbc;')

    @staticmethod
    def query(sql_query):
        query_results = list()
        cursor = Database.cnxn.cursor()
        cursor.execute(sql_query)
        row = cursor.fetchone()
        while row:
            #print(row)
            query_results.append(list(row))
            row = cursor.fetchone()
        return query_results
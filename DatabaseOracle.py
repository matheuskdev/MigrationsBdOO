import cx_Oracle
from Database import Database

class DatabaseOracle(Database):
    def __init__(self, user, password, host, database):
        super().__init__(user, password, host, database)

    def connect(self):
        cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_21_7",
                                config_dir=r"C:\orant\NETWORK\ADMIN\TNSNAMES.ORA")

        self.conn = cx_Oracle.connect(self.user+"/"+self.password+"@"+self.host+"/"+self.database) 
        self.cursor = self.conn.cursor()
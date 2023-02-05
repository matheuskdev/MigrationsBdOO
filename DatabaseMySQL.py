import mysql.connector
from Database import Database

class DatabaseMySQL(Database):
    def __init__(self, user, password, host, database):
        super().__init__(user, password, host, database)

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database)
        self.cursor = self.conn.cursor()
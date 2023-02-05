class Database:
    def __init__(self, user, password, host, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = None
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, query):
        self.cursor.execute(query)
    
    def execute_commit(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def is_connected(self):
        return self.conn.is_connected()
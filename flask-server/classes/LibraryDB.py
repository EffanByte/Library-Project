import mysql.connector

class LibraryDB :
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
    
    def close_connection(self):
        self.cursor.close()
        self.conn.close()
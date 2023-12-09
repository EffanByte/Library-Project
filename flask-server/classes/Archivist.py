import mysql.connector

class Archivist:
    def __init__(self, archivist_id, name, db_connection):
        self.archivist_id = archivist_id
        self.name = name
        self.db_connection = db_connection

    def add_paper(self, title, archivist_id):
        query = "INSERT INTO Paper (Title, ArchivistID) VALUES (%s, %s)"
        values = (title, archivist_id)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

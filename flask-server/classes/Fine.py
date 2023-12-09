import mysql.connector

class Fine:
    def __init__(self, fine_id, fine_applicable, db_connection):
        self.fine_id = fine_id
        self.fine_applicable = fine_applicable
        self.db_connection = db_connection

    def apply_fine(self, qalam_id, fine_applicable):
        query = "INSERT INTO Fine (FineApplicable) VALUES (%s)"
        values = (fine_applicable,)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

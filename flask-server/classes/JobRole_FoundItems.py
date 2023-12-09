import mysql.connector

class JobRole_FoundItems:
    def __init__(self, item_id, job_id, db_connection):
        self.item_id = item_id
        self.job_id = job_id
        self.db_connection = db_connection

    def assign_found_item(self, item_id, job_id):
        query = "INSERT INTO JobRole_FoundItems (ItemID, JobID) VALUES (%s, %s)"
        values = (item_id, job_id)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

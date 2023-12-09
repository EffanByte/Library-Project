import mysql.connector

class JobRole_LostItems:
    def __init__(self, item_id, job_id, db_connection):
        self.item_id = item_id
        self.job_id = job_id
        self.db_connection = db_connection

    def assign_lost_item(self, item_id, job_id):
        query = "INSERT INTO JobRole_LostItems (ItemID, JobID) VALUES (%s, %s)"
        values = (item_id, job_id)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

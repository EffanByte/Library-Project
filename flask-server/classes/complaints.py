import mysql.connector

class Complaint:
    def __init__(self, complaint_id, complaint_description, db_connection):
        self.complaint_id = complaint_id
        self.complaint_description = complaint_description
        self.db_connection = db_connection

    def save_to_database(self):
        insert_query = "INSERT INTO complaints (complaintID, complaint_description) VALUES (%s, %s)"
        cursor = self.db_connection.cursor()
        cursor.execute(insert_query, (self.complaint_id, self.complaint_description))
        self.db_connection.commit()
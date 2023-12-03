import mysql.connector

class JobRole_ActionReport:
    def __init__(self, job_id, action_id, db_connection):
        self.job_id = job_id
        self.action_id = action_id
        self.db_connection = db_connection

    def assign_action_report(self, job_id, action_id):
        query = "INSERT INTO JobRole_ActionReport (JobID, ActionID) VALUES (%s, %s)"
        values = (job_id, action_id)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

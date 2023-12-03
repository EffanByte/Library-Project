import mysql.connector

class Fine_Overdue:
    def __init__(self, overdue_issue_id, fine_id, db_connection):
        self.overdue_issue_id = overdue_issue_id
        self.fine_id = fine_id
        self.db_connection = db_connection

    def assign_fine_overdue(self, overdue_issue_id, fine_id):
        query = "INSERT INTO Fine_Overdue (OverDueIssuesID, FineID) VALUES (%s, %s)"
        values = (overdue_issue_id, fine_id)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()


import mysql.connector

class OverdueIssues:
    def __init__(self, overdue_issues_id, issued_id, fine_id, qalam_id, days_overdue, db_connection):
        self.overdue_issues_id = overdue_issues_id
        self.issued_id = issued_id
        self.fine_id = fine_id
        self.qalam_id = qalam_id
        self.days_overdue = days_overdue
        self.db_connection = db_connection

    def report_overdue_issue(self, issued_id, fine_id, qalam_id, days_overdue):
        query = "INSERT INTO OverdueIssues (IssuedID, FineID, QalamID, DaysOverdue) VALUES (%s, %s, %s, %s)"
        values = (issued_id, fine_id, qalam_id, days_overdue)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

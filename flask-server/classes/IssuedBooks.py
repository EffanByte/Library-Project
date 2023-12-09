import mysql.connector

class IssuedBooks:
    def __init__(self, issued_id, qalam_id, book_id, job_id, db_connection):
        self.issued_id = issued_id
        self.qalam_id = qalam_id
        self.book_id = book_id
        self.job_id = job_id
        self.db_connection = db_connection

    def issue_book(self, qalam_id, book_id, job_id):
        query = "INSERT INTO IssuedBooks (QalamID, BookID, JobID) VALUES (%s, %s, %s)"
        values = (qalam_id, book_id, job_id)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()


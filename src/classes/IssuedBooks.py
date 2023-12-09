class IssuedBooks:
    def __init__(self, issued_id, qalam_id, book_id, job_id, db_connection):
        self.issued_id = issued_id
        self.qalam_id = qalam_id
        self.book_id = book_id
        self.job_id = job_id
        self.db_connection = db_connection

    def issue_book(self, qalam_id, book_id, job_id):
        call_proc = "CALL IssueBook(%s, %s, %s)"
        values = (qalam_id, book_id, job_id)
        self.db_connection.cursor.execute(call_proc, values)
        self.db_connection.conn.commit()



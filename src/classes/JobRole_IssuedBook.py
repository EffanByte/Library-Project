class JobRole_IssuedBook:
    def __init__(self, issued_id, job_id, db_connection):
        self.issued_id = issued_id
        self.job_id = job_id
        self.db_connection = db_connection

    def assign_issued_book(self, issued_id, job_id):
        call_proc = "CALL AssignIssuedBook(%s, %s)"
        values = (issued_id, job_id)
        self.db_connection.cursor.execute(call_proc, values)
        self.db_connection.conn.commit()

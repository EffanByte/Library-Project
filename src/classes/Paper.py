class Paper:
    def __init__(self, paper_id, title, archivist_id, db_connection):
        self.paper_id = paper_id
        self.title = title
        self.archivist_id = archivist_id
        self.db_connection = db_connection

    def upload_paper(self, job_id, paper_id, upload_status, date_of_request, request_id):
        call_proc = "CALL UploadPaper(%s, %s, %s, %s, %s)"
        values = (job_id, paper_id, upload_status, date_of_request, request_id)
        self.db_connection.cursor.execute(call_proc, values)
        self.db_connection.conn.commit()

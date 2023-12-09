class JobRole_ActionReport:
    def __init__(self, job_id, action_id, db_connection):
        self.job_id = job_id
        self.action_id = action_id
        self.db_connection = db_connection

    def assign_action_report(self, job_id, action_id):
        call_proc = "CALL AssignActionReport(%s, %s)"
        values = (job_id, action_id)
        self.db_connection.cursor.execute(call_proc, values)
        self.db_connection.conn.commit()


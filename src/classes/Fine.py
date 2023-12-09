class Fine:
    def __init__(self, fine_id, fine_applicable, db_connection):
        self.fine_id = fine_id
        self.fine_applicable = fine_applicable
        self.db_connection = db_connection

    def apply_fine(self, qalam_id, fine_applicable):
        call_proc = "CALL ApplyFine(%s, %s)"
        values = (qalam_id, fine_applicable)
        self.db_connection.cursor.execute(call_proc, values)
        self.db_connection.conn.commit()


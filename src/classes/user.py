class User:
    def __init__(self, qalam_id, email, name, password, db_connection):
        self.qalam_id = qalam_id
        self.email = email
        self.name = name
        self.password = password
        self.db_connection = db_connection

    def get_issued_books(self):
        call_proc = "CALL GetIssuedBooks(%s)"
        self.db_connection.cursor.execute(call_proc, (self.qalam_id,))
        issued_books = self.db_connection.cursor.fetchall()
        return issued_books

    def get_reserved_rooms(self):
        call_proc = "CALL GetReservedRooms(%s)"
        self.db_connection.cursor.execute(call_proc, (self.qalam_id,))
        reserved_rooms = self.db_connection.cursor.fetchall()
        return reserved_rooms

    def report_lost_item(self, item_description, date_reported):
        call_proc = "CALL ReportLostItem(%s, %s, %s)"
        values = (self.qalam_id, item_description, date_reported)
        self.db_connection.cursor.execute(call_proc, values)
        self.db_connection.conn.commit()

    def report_found_item(self, item_description, date_reported):
        call_proc = "CALL ReportFoundItem(%s, %s, %s)"
        values = (self.qalam_id, item_description, date_reported)
        self.db_connection.cursor.execute(call_proc, values)
        self.db_connection.conn.commit()

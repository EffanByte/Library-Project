class BookFormat:
    def __init__(self, type_id, format_type, db_connection):
        self.type_id = type_id
        self.format_type = format_type
        self.db_connection = db_connection

    def get_books(self):
        call_proc = "CALL GetBooksByTypeID(%s)"
        self.db_connection.cursor.execute(call_proc, (self.type_id,))
        books = self.db_connection.cursor.fetchall()
        return books

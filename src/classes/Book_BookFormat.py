class Book_BookFormat:
    def __init__(self, book_id, type_id, db_connection):
        self.book_id = book_id
        self.type_id = type_id
        self.db_connection = db_connection

    def add_book_format(self, book_id, type_id):
        call_proc = "CALL AddBookFormatProcedure(%s, %s)"
        values = (book_id, type_id)
        self.db_connection.cursor().execute(call_proc, values)
        self.db_connection.conn.commit()

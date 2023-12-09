class Book:
    def __init__(self, book_id, name, author, description, genre, type_id, db_connection):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.description = description
        self.genre = genre
        self.type_id = type_id
        self.db_connection = db_connection

    def get_available_formats(self):
        call_proc = "CALL GetBookFormats(%s)"
        self.db_connection.cursor().execute(call_proc, (self.type_id,))
        formats = self.db_connection.cursor().fetchall()
        return formats

    def get_issued_details(self):
        call_proc = "CALL GetIssuedBookDetails(%s)"
        self.db_connection.cursor().execute(call_proc, (self.book_id,))
        issued_details = self.db_connection.cursor().fetchall()
        return issued_details

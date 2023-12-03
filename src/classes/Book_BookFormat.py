import mysql.connector

class Book_BookFormat:
    def __init__(self, book_id, type_id, db_connection):
        self.book_id = book_id
        self.type_id = type_id
        self.db_connection = db_connection

    def add_book_format(self, book_id, type_id):
        query = "INSERT INTO Book_BookFormat (BookID, TypeID) VALUES (%s, %s)"
        values = (book_id, type_id)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

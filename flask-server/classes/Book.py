import mysql.connector

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
        query = "SELECT * FROM BookFormat WHERE TypeID = %s"
        self.db_connection.cursor.execute(query, (self.type_id,))
        formats = self.db_connection.cursor.fetchall()
        return formats

    def get_issued_details(self):
        query = "SELECT * FROM IssuedBooks WHERE BookID = %s"
        self.db_connection.cursor.execute(query, (self.book_id,))
        issued_details = self.db_connection.cursor.fetchall()
        return issued_details

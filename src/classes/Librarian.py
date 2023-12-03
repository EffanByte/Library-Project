import mysql.connector

class Librarian:
    def __init__(self, librarian_id, email, name, password, db_connection):
        self.librarian_id = librarian_id
        self.email = email
        self.name = name
        self.password = password
        self.db_connection = db_connection

    def add_book(self, book_details):
        query = "INSERT INTO Book (Name, Author, Description, Genre, TypeID) VALUES (%s, %s, %s, %s, %s)"
        values = (book_details['Name'], book_details['Author'], book_details['Description'], book_details['Genre'], book_details['TypeID'])
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

    def issue_book(self, book_id, user_id):
        query = "INSERT INTO IssuedBooks (QalamID, BookID) VALUES (%s, %s)"
        values = (user_id, book_id)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

    def generate_action_report(self, action_description):
        query = "INSERT INTO ActionReport (LibrarianID, ActionDescription, TimeOfAction) VALUES (%s, %s, NOW())"
        values = (self.librarian_id, action_description)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

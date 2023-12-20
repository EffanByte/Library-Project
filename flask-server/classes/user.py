import mysql.connector
import bcrypt


class User:
    def __init__(self, qalam_id, email, name, password, db_connection):
        self.qalam_id = qalam_id
        self.email = email
        self.name = name
        self.password = password
        self.db_connection = db_connection

    def get_issued_books(self):
        query = "SELECT * FROM IssuedBooks WHERE QalamID = %s"
        self.db_connection.cursor.execute(query, (self.qalam_id,))
        issued_books = self.db_connection.cursor.fetchall()
        return issued_books

    def get_reserved_rooms(self):
        query = "SELECT * FROM Room WHERE QalamID = %s AND ReservationStatus = 'Reserved'"
        self.db_connection.cursor.execute(query, (self.qalam_id,))
        reserved_rooms = self.db_connection.cursor.fetchall()
        return reserved_rooms

    def report_lost_item(self, item_description, date_reported):
        query = "INSERT INTO LostItems (QalamID, ItemDescription, DateReported) VALUES (%s, %s, %s)"
        values = (self.qalam_id, item_description, date_reported)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

    def report_found_item(self, item_description, date_reported):
        query = "INSERT INTO FoundItems (QalamID, ItemDescription, DateReported) VALUES (%s, %s, %s)"
        values = (self.qalam_id, item_description, date_reported)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

    @staticmethod
    def signup_user(qalamID, email, name, password, db_connection):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        query = "INSERT INTO User (QalamID, Email, Name, Password) VALUES ( %s, %s, %s, %s)"
        values = (qalamID, email, name, hashed_password)
        cursor = db_connection.cursor()
        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()

    @staticmethod
    def get_user_info(user_id, db_connection):
        # Assuming db_connection is available here, maybe passed during class instantiation
        cursor = db_connection.cursor(dictionary = True)
        call_proc = "CALL GetUserInfo(%s)"
        cursor.execute(call_proc, (user_id,))
        user_info = cursor.fetchone()
    
        cursor.close()
        return user_info
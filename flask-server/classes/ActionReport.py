import mysql.connector

class ActionReport:
    def __init__(self, action_id, librarian_id, action_description, time_of_action, db_connection):
        self.action_id = action_id
        self.librarian_id = librarian_id
        self.action_description = action_description
        self.time_of_action = time_of_action
        self.db_connection = db_connection

    def generate_action_report(self, librarian_id, action_description, time_of_action):
        query = "INSERT INTO ActionReport (LibrarianID, ActionDescription, TimeOfAction) VALUES (%s, %s, %s)"
        values = (librarian_id, action_description, time_of_action)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

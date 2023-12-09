import mysql.connector

class ActionReport:
    def __init__(self, action_id, librarian_id, action_description, time_of_action, db_connection):
        self.action_id = action_id
        self.librarian_id = librarian_id
        self.action_description = action_description
        self.time_of_action = time_of_action
        self.db_connection = db_connection

    def generate_action_report(self, librarian_id, action_description, time_of_action):
        call_proc = "CALL GenerateActionReport(%s, %s, %s)"
        values = (librarian_id, action_description, time_of_action)
        self.db_connection.cursor.execute(call_proc, values)
        self.db_connection.conn.commit()




# Example Usage:
# Replace the database connection details with your actual database credentials
# db = mysql.connector.connect(host='your_host', user='your_user', password='your_password', database='your_database')
# action_report = ActionReport(action_id=1, librarian_id=1, action_description='Performed action', time_of_action='2023-12-09', db_connection=db)
# action_report.generate_action_report(librarian_id=action_report.librarian_id, action_description='Performed another action', time_of_action='2023-12-09')

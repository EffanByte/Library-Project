import mysql.connector

class JobRole:
    def __init__(self, job_id, librarian_id, supervisor_id, role_name, db_connection):
        self.job_id = job_id
        self.librarian_id = librarian_id
        self.supervisor_id = supervisor_id
        self.role_name = role_name
        self.db_connection = db_connection

    def assign_supervisor(self, librarian_id, supervisor_id, role_name):
        query = "INSERT INTO JobRole (LibrarianID, SupervisorID, RoleName) VALUES (%s, %s, %s)"
        values = (librarian_id, supervisor_id, role_name)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()


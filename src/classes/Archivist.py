import mysql.connector

import mysql.connector

class Archivist:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_paper(self, title, archivist_id):
        try:
            cursor = self.db_connection.cursor()
            call_proc = "CALL AddPaper(%s, %s)"
            values = (title, archivist_id)
            cursor.execute(call_proc, values)
            self.db_connection.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Error: {}".format(err.msg))

# Example usage:
# Replace the database connection details with your actual database credentials
# db = mysql.connector.connect(host='your_host', user='your_user', password='your_password', database='your_database')
# archivist = Archivist(db)
# archivist.add_paper(title="New Paper", archivist_id=1)


# Usage example:
# Replace the database connection details with your actual database credentials
# db = mysql.connector.connect(host='your_host', user='your_user', password='your_password', database='your_database')
# archivist = Archivist(archivist_id=1, name='John Doe', db_connection=db)
# archivist.add_paper(title='Sample Paper', archivist_id=archivist.archivist_id)

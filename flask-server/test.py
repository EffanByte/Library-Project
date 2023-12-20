import mysql.connector
import base64
import bcrypt
# API KEY for Google Books API here
#api_key = "AIzaSyC0duRJFDy8vZLT8-rnXqa6JawDxT8t-tQ"

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',   
        database='virtual_library'
    )

def signup_Librarian(librarianID, email, name, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    print(librarianID, email, name, hashed_password)
    query = "INSERT INTO librarian (LibrarianID, Email, Name, Password) VALUES ( %s, %s, %s, %s)"
    values = (librarianID, email, name, hashed_password)
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(query, values)
    db_connection.commit()
    cursor.close()

signup_Librarian(3, "aharoon.bscs22seecs@seecs.edu.pk", "Arham Haroon", "123")


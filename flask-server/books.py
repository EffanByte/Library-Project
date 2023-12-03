import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='virtual_library'
    )

def get_books():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books




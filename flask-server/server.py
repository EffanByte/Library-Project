from flask import Flask, jsonify, request
from flask_cors import CORS
from books import *
from classes.user import *
from werkzeug.security import check_password_hash


app = Flask(__name__)
CORS(app)

# function to establish database connection
def get_db_connection():
    return mysql.connector.connect(
        # MODIFY ACCORDING TO YOUR OWN DATABASE
        host='localhost',
        user='root',
        password='',
        database='virtual_library'
    )

# Route to get all books for display in Catalogue.svelte
@app.route('/api/books', methods=['GET'])
def api_get_books():
    try:
        books = get_books()  # Assuming this returns a list of dictionaries
        return jsonify(books) # return books to frontend component in JSON format
    except Exception as e:
        return jsonify(error=str(e)), 500



# Route to get books by ID to display in BookDetail.svelte
@app.route('/api/books/<int:book_id>', methods=['GET'])
def api_get_book_by_id(book_id):

    try:
        book = get_book_by_id(book_id)
        if book:
            return jsonify(book)
        else:
            return jsonify({"error": "Book not found"}), 404
    except Exception as e:
        return jsonify(error=str(e)), 500    
    

# Route to sign up user using User.signup_user method in user.py
@app.route('/api/signup', methods=['POST'])
def api_signup():
    try:
        # Extract the data from the request
        data = request.json
        qalamId = data['QalamID']
        email = data['Email']
        name = data['Name']
        password = data['Password']

        # Establish a database connection
        db_connection = get_db_connection()

        # Call the signup_user method to sign up the user
        User.signup_user(qalamId, email, name, password, db_connection)

        # Close the database connection
        db_connection.close()

        # Return a success message
        return jsonify({"message": "User signed up successfully"}), 201

    except Exception as e:
        # If an error occurs, return an error message
        return jsonify(error=str(e)), 500    


# Route to handle user logging in
# First checks if the email entered is in user table, then checks librarian table
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('Email')
    password = data.get('Password').encode('utf-8')  # Ensure password is encoded to bytes

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Query for user
    cursor.execute('SELECT * FROM user WHERE Email = %s', (email,))
    user = cursor.fetchone()

    # Query for librarian if user is not found
    if user is None:
        cursor.execute('SELECT * FROM librarian WHERE Email = %s', (email,))
        user = cursor.fetchone()
        user_type = 'librarian'
    else:
        user_type = 'user'

    # Close the database connection
    cursor.close()
    conn.close()

    if user and bcrypt.checkpw(password, user['Password'].encode('utf-8')):
        # If password matches
        return jsonify({
            'email': user['Email'],
            'name': user['Name'],
            'userType': user_type
        }), 200
    else:
        # If password does not match
        return jsonify({'error': 'Invalid credentials'}), 401
    
# running the flask server    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug=True)
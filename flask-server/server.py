import bcrypt
from flask import Flask, jsonify, request
from flask_cors import CORS
from books import *
from classes.user import *
from werkzeug.security import check_password_hash
import re


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
    

@app.route('/api/books', methods=['POST'])
def add_book():
    try:
        # Extracting text fields
        title = request.form['Title']
        author = request.form['Author']
        genre = request.form['Genre']
        description = request.form['Description']
        type_id = request.form['TypeID']

        # Extracting file fields
        cover_image = request.files.get('coverImage')
        pdf_file = request.files.get('PDF')

        cover_image_data = cover_image.read() if cover_image else None
        pdf_data = pdf_file.read() if pdf_file else None

        # Add the book to the database
        book_id = add_book_to_db(title, author, genre, description, type_id, cover_image_data)

        # Add PDF to the BookPDFs table
        if pdf_data:
            add_pdf_to_book(book_id, pdf_data)

        return jsonify({'message': 'Book added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to check if a book exists by Title in BookManage.svelte
@app.route('/api/books/check', methods=['POST'])
def check_book_exists():
    try:
        data = request.json
        book_title = data.get('Title')
        book = get_book_by_title(book_title)
    
        if book:
            # If book exists
            return jsonify({'exists': True, 'book': book}), 200
        else:
            # If book does not exist
            return jsonify({'exists': False}), 404
    except Exception as e:
        return jsonify(error=str(e)), 500 
    


@app.route('/api/books/<int:book_id>', methods=['PUT'])
def api_update_book(book_id):
    try:
        print(data)
        data = request.json
        if update_book(book_id, data):
            return jsonify({'message': 'Book updated successfully'}), 200
        else:
            return jsonify({'error': 'Book not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/books/update/pdf/<int:book_id>', methods=['PUT'])
def update_book_pdf(book_id):
    pdf_file = request.files.get('PDF')

    if pdf_file:
        pdf_data = pdf_file.read()
        update_pdf_for_book(book_id, pdf_data)
        return jsonify({"message": "PDF updated successfully"}), 200
    else:
        return jsonify({"error": "No PDF file provided"}), 400
    

    

# Route to sign up user using User.signup_user method in user.py
'''
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
        '''



# Route to sign up user using User.signup_user method in user.py
@app.route('/api/signup', methods=['POST'])
def api_signup():
    try:
        # Extract the data from the request
        data = request.json
        qalamId = str(data['QalamID'])  # Ensure qalamId is treated as a string
        email = data['Email']
        name = data['Name']
        password = data['Password']

        # Validate name (should not contain numbers)
        if any(char.isdigit() for char in name):
            return jsonify({"error": "Name should not contain numbers"}), 400

        # Validate CMS (should be 6 digits long)
        if not (qalamId.isdigit() and len(qalamId) == 6):
            return jsonify({"error": "CMS should be 6 digits long"}), 400

        # Validate email (should have @ and .com in it)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({"error": "Invalid email format"}), 400

        # Establish a database connection
        db_connection = get_db_connection()
        cursor = db_connection.cursor()

        # Check if a user with the same QalamID already exists
        cursor.execute("SELECT * FROM user WHERE QalamID = %s", (qalamId,))
        if cursor.fetchone():
            cursor.close()
            db_connection.close()
            return jsonify({"error": "User with this QalamID already exists"}), 409
        

         # Check if a user with the same QalamID already exists
        cursor.execute("SELECT * FROM user WHERE Email = %s", (email,))
        if cursor.fetchone():
            cursor.close()
            db_connection.close()
            return jsonify({"error": "This email is already associated with another QalamID"}), 409


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
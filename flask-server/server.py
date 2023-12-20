import bcrypt
from flask import Flask, jsonify, request
from flask_cors import CORS
from books import *
from classes.user import *
from werkzeug.security import check_password_hash
from datetime import datetime
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

def book_room():
    try:
        data = request.json
        room_no = data.get('RoomNo')
        qalam_id = data.get('QalamID')
        reservation_time = data.get('ReservationTime')

        room = next((r for r in rooms if r["RoomNo"] == room_no), None)

        if room and room["ReservationStatus"] == "Available":
            room["QalamID"] = qalam_id
            room["ReservationTime"] = reservation_time
            room["ReservationStatus"] = "Booked"
            room["BookedTimings"].append(reservation_time)

            return jsonify({"message": "Room booked successfully"}), 200
        else:
            return jsonify({"error": "Room not available for booking"}), 400
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
    role = ''
    # Query for librarian if user is not found
    if user is None:
        cursor.execute('SELECT * FROM librarian WHERE Email = %s', (email,))
        user = cursor.fetchone()
        user_type = 'librarian'
        
    else:
        user_type = 'user'

        # Inside your login function, after you determine the user_type
    if user:
        if user_type == 'librarian':
            cursor.execute('SELECT RoleName FROM jobrole JOIN librarian USING (LibrarianID) WHERE Email = %s', (email,))
            role = cursor.fetchone()
            role = role['RoleName'] if role else 'No role found'
       
        

    # Close the database connection
    cursor.close()
    conn.close()

    if user and bcrypt.checkpw(password, user['Password'].encode('utf-8')):
        # If password matches
        return jsonify({
            'email': user['Email'],
            'name': user['Name'],
            'userType': user_type,
            'role': role
        }), 200
    else:
        # If password does not match
        return jsonify({'error': 'Invalid credentials'}), 401
    
def is_room_available(room_no, reservation_time):
    # Check if the room is available at the specified time
    room = next((r for r in rooms if r["RoomNo"] == room_no), None)
    return room and room["ReservationStatus"] == "Available" and reservation_time not in room["BookedTimings"]


rooms = [
    {"RoomNo": 1, "ReservationStatus": "Available", "BookedTimings": []},
    {"RoomNo": 2, "ReservationStatus": "Available", "BookedTimings": []},
    # Add more rooms with their bookedTimings as needed
]
def is_room_available(room_no, reservation_time):
    room = next((r for r in rooms if r["RoomNo"] == room_no), None)
    return (
        room
        and room["ReservationStatus"] == "Available"
        and reservation_time not in room["BookedTimings"]
    )



@app.route('/api/room', methods=['POST'])
def book_room():
    try:
        data = request.json
        room_no = data.get('RoomNo')
        qalam_id = data.get('QalamID')
        reservation_time = data.get('ReservationTime')

        if is_room_available(room_no, reservation_time):
            # Find the room in the list
            room = next((r for r in rooms if r["RoomNo"] == room_no), None)
            if room:
                # Update the room reservation details
                room["QalamID"] = qalam_id
                room["ReservationTime"] = reservation_time
                room["ReservationStatus"] = "Booked"
                
                # Update the booked timings for the room
                room["BookedTimings"].append(reservation_time)

                return jsonify({"message": "Room booked successfully"}), 200
            else:
                return jsonify({"error": "Room not found"}), 404
        else:
            return jsonify({"error": "Room not available for booking"}), 400
    except Exception as e:
        return jsonify(error=str(e)), 500

# running the flask server    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug=True)
import bcrypt
import mysql.connector
import mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS
from books import *
from classes.user import *
from werkzeug.security import check_password_hash
from classes.FoundItems import *
from classes.LostItems import *
from classes.IssuedBooks import *
from classes.complaints import *
from classes.IssuedBooks import *
from classes.complaints import *
from datetime import datetime
import re


app = Flask(__name__)
#CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})


# function to establish database connection
def get_db_connection():
    return mysql.connector.connect(
        # MODIFY ACCORDING TO YOUR OWN DATABASE
        host='localhost',
        user='root',
        password='',
        database='virtual_library'
    )

@app.route('/api/rooms', methods=['GET'])
def get_all_rooms_from_db():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    RoomsDB = []
    try:
        # Fetch all rooms from the "room" table
        cursor.execute("SELECT * FROM room")
        rooms = cursor.fetchall()
        # Convert BLOB data to base64 if needed
        # For example, if you have an attribute like "coverImage" in the "room" table

        # rooms = convert_blob_to_base64(rooms)
        return rooms
    except Exception as e:
        print("Error fetching rooms:", e)
    finally:
        cursor.close()
        connection.close()   


@app.route('/api/rooms1', methods=['POST'])
def post_to_room():
    try:
        data = request.json
        RoomNo = data.get('RoomNo')
        QalamID = str(data.get('QalamID'))
        ReservationTime = data.get('ReservationTime')
        ReservationStatus = data.get('ReservationStatus')

        db_connection = get_db_connection()
        cursor = db_connection.cursor()
        print(RoomNo, QalamID, ReservationTime, ReservationStatus)
        cursor.execute(
            "INSERT INTO room (RoomNo, QalamID, ReservationTime, ReservationStatus) VALUES (%s, %s, %s, %s)",
            (RoomNo, QalamID, ReservationTime, ReservationStatus)
        )
        print("Works")
        db_connection.commit()
        cursor.close()
        db_connection.close()

        return jsonify({"message": "Data added to the room table successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500





@app.route('/api/remove_bookings', methods=['POST'])
def remove_user_bookings():
    try:
        data = request.json
        qalam_id = data.get('QalamID')

        db_connection = get_db_connection()
        cursor = db_connection.cursor()

        # Delete all bookings for the specified user
        cursor.execute("DELETE FROM room WHERE QalamID = %s and reservationtime != '2023-12-20 08:00:00'", (qalam_id,))
        db_connection.commit()
        db_connection.close()

        return jsonify({"message": "All bookings removed successfully"}), 200

    except Exception as e:
        return jsonify(error=str(e)), 500


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
        conn = get_db_connection()
        # Extract text fields
        title = request.form['Title']
        author = request.form['Author']
        genre = request.form['Genre']
        description = request.form['Description']
        type_id = request.form['TypeID']

        # Extract file fields
        cover_image = request.files.get('coverImage')
        pdf_file = request.files.get('PDF')

        # Read file data if files are present
        cover_image_data = cover_image.read() if cover_image and cover_image.filename else None
        pdf_data = pdf_file.read() if pdf_file and pdf_file.filename else None

        # Insert book details into the books table
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (Title, Author, Genre, Description, TypeID, coverImage) VALUES (%s, %s, %s, %s, %s, %s)",
                       (title, author, genre, description, type_id, cover_image_data))
        book_id = cursor.lastrowid

        # Insert PDF data into BookPDFs table if PDF is provided
        if pdf_data:
            cursor.execute("INSERT INTO BookPDFs (BookID, PDF) VALUES (%s, %s)", (book_id, pdf_data))

        conn.commit()
        cursor.close()

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
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Start a database transaction
        conn.start_transaction()

        # Extracting text fields
        title = request.form.get('Title')
        genre = request.form.get('Genre')
        description = request.form.get('Description')
        type_id = request.form.get('TypeID')

        # Extracting file fields
        cover_image = request.files.get('coverImage')
        cover_image_data = cover_image.read() if cover_image and cover_image.filename else None

        # Prepare the base update query
        update_query = """
            UPDATE books
            SET Title = %s, Genre = %s, Description = %s, TypeID = %s
        """
        values = [title, genre, description, type_id]

        # Add cover image data to the query only if a new image is provided
        if cover_image_data:
            update_query += ", coverImage = %s"
            values.append(cover_image_data)

        # Add the WHERE clause to the update query
        update_query += " WHERE BookID = %s"
        values.append(book_id)

        # Execute the update query
        cursor.execute(update_query, values)

        # If a new PDF is provided, check if an entry exists and update or insert accordingly
        pdf_file = request.files.get('PDF')
        if pdf_file and pdf_file.filename:
            pdf_data = pdf_file.read()
            # Check if PDF already exists
            cursor.execute("""
                SELECT COUNT(1) FROM BookPDFs WHERE BookID = %s
            """, (book_id,))
            pdf_exists = cursor.fetchone()[0]
            
            if pdf_exists:
                # Update existing PDF
                cursor.execute("""
                    UPDATE BookPDFs SET PDF = %s WHERE BookID = %s
                """, (pdf_data, book_id))
            else:
                # Insert new PDF
                cursor.execute("""
                    INSERT INTO BookPDFs (BookID, PDF) VALUES (%s, %s)
                """, (book_id, pdf_data))
        
        # Commit the transaction
        conn.commit()

        return jsonify({'message': 'Book and PDF updated successfully'}), 200

    except mysql.connector.Error as e:
        # Rollback the transaction in case of error
        conn.rollback()
        return jsonify({'error': str(e)}), 500

    finally:
        # Make sure to close the cursor and connection
        cursor.close()
        conn.close()




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
        # Fetching the ID for a librarian, for example
        cursor.execute('SELECT LibrarianID FROM librarian WHERE Email = %s', (email,))
        id = cursor.fetchone()
        id = id['LibrarianID'] if id else None


        
    else:
        # Fetching the QalamID for a user
        cursor.execute('SELECT QalamID FROM user WHERE Email = %s', (email,))
        id = cursor.fetchone()
        id = id['QalamID'] if id else None
        user_type = 'user'

    # Inside login function, after determining the user_type
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
        'id': id,  # Make sure 'id' is the actual ID value, not a dictionary
        'email': user['Email'],
        'name': user['Name'],
        'userType': user_type,
        'role': role  # Ensure this is a string, not a dictionary
    }), 200

    else:
        # If password does not match
        return jsonify({'error': 'Invalid credentials'}), 401


@app.route('/api/allUsers', methods=['GET'])
def get_all_users():
    try:
        # Assuming you have a method to get the database connection
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Get information for all users
        all_users_info = User.get_all_users_info(conn)
        print(all_users_info)
        cursor.close()
        conn.close()
        
       
        return jsonify(all_users_info), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

'''@app.route('/api/all_issued_books_library', methods=['GET'])
def get_all_issued_books_library():
    try:
        # Create a cursor
        cur = mysql.connection.cursor()

        # Call the MySQL stored procedure
        cur.callproc('GetAllIssuedBooksLibrary')

        # Fetch all the rows
        result_set = cur.fetchall()
        print(result_set)

        # Convert the result set to a list of dictionaries for JSON serialization
        issued_books = [{'BookID': row[0], 'Title': row[1], 'IssuedBy': row[2]} for row in result_set]

        # Close the cursor
        cur.close()

        return jsonify(issued_books), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500  '''
    
@app.route('/api/allIssuedBooksLibrary', methods=['GET'])
def get_all_issued_books_library():
    try:
        # Create a cursor
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Call the MySQL stored procedure
        issuedbookInfo=IssuedBooks.GetAllIssuedBooksLibrary(conn)
        cursor.close()
        conn.close()
        
       
        return jsonify(issuedbookInfo), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
 
'''   
@app.route('/api/all_found_items', methods=['GET'])
def get_all_found_items():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Assuming you have a method in your FoundItems class to get all found items
        found_items = FoundItems.get_all_found_items(conn)

        conn.close()
        cursor.close()
        return jsonify(found_items), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
'''

'''
@app.route('/api/all_lost_items', methods=['GET'])
def get_all_lost_items():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Assuming you have a method in your LostItems class to get all lost items
        lost_items = LostItems.get_all_lost_items(conn)

        conn.close()
        cursor.close()
        return jsonify(lost_items), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
'''        
    

@app.route('/api/reportFoundItem', methods=['POST'])
def report_found_item():
    try:
        userID = request.args.get('id') 
        data = request.json
        
       # item_description = data['ItemDescription']
       # date_reported = data['DateReported']
        
        item_description = data.get('foundItemDescription')
        date_reported = data.get('foundDateReported')

        conn = get_db_connection()
        cursor = conn.cursor()

        #cursor.execute("CALL ReportFoundItem(%s, %s, %s)", (userID, item_description, date_reported))
        cursor.execute("INSERT INTO founditems (QalamID,ItemDescription,DateReported) VALUES (%s,%s,%s)", (userID,item_description,date_reported,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Found item reported successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/reportLostItem', methods=['POST'])
def report_lost_item():
    try:
        userID = request.args.get('id') 
        data = request.json
        
        
        #qalam_id = data['qalam_id']
        item_description = data.get('lostItemDescription')
        date_reported = data.get('lostDateReported')

        conn = get_db_connection()
        cursor = conn.cursor()

       # cursor.execute("CALL ReportLostItem(%s, %s, %s)", (userID, item_description, date_reported))
        cursor.execute("INSERT INTO lostitems (QalamID,ItemDescription,DateReported) VALUES (%s,%s,%s)", (userID,item_description,date_reported,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Lost item reported successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500 
    




@app.route('/api/users/<int:qalam_id>', methods=['PUT'])
def update_user(qalam_id):
    try:
        data = request.json
        new_email = data['Email']
        new_name = data['Name']

        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            return jsonify({"error": "Invalid email format"}), 400

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Check if the new email is associated with another user
        cursor.execute("SELECT * FROM user WHERE Email = %s AND QalamID != %s", (new_email, qalam_id))
        if cursor.fetchone():
            cursor.close()
            conn.close()
            return jsonify({"error": "This email is associated with another QalamID"}), 409

        # Update user details
        cursor.execute("UPDATE user SET Email = %s, Name = %s WHERE QalamID = %s", (new_email, new_name, qalam_id))
        conn.commit()

        cursor.close()
        conn.close()
        return jsonify({"message": "User updated successfully"}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/submitComplaints', methods=['POST'])
def submit_complaint():
    try:
        userID = request.args.get('id')  
        print(userID)
        data = request.json
        
        complaint_details = data.get('complaint_description')

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert the complaint data into the database
        cursor.execute("INSERT INTO complaints (complaint_description,QalamID) VALUES (%s,%s)", (complaint_details,userID,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Complaint submitted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/complaints', methods=['GET'])
def get_complaints():
    try:
        # Assuming you have a method to get the database connection
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Assuming your complaints table has complaintID and complaint_description columns
        cursor.execute("SELECT complaintID, complaint_description FROM complaints")
        complaints_info = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(complaints_info), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/all_found_items', methods=['GET'])
def get_all_found_items():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Assuming you have a method in your FoundItems class to get all found items
        found_items = FoundItems.get_all_found_items(conn)

        conn.close()
        cursor.close()
        return jsonify(found_items), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/all_lost_items', methods=['GET'])
def get_all_lost_items():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Assuming you have a method in your LostItems class to get all lost items
        lost_items = LostItems.get_all_lost_items(conn)

        conn.close()
        cursor.close()
        return jsonify(lost_items), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
# Flask server code

@app.route('/api/deleteItem', methods=['DELETE'])
def delete_item():
    try:
        item_id = request.args.get('id')
        conn = get_db_connection()
        cursor = conn.cursor()

        # Assuming you have a method to delete an item by ID
        cursor.execute("DELETE FROM lostitems WHERE ItemID = %s", (item_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Item deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/markItemFound', methods=['POST'])
def mark_item_found():
    try:
        item_id = request.args.get('id')
        conn = get_db_connection()
        cursor = conn.cursor()

         

        # Assuming you have a method to mark an item as found by ID
        cursor.execute("INSERT INTO founditems (SELECT * FROM lostitems WHERE ItemID = %s)", (item_id,))
        cursor.execute("DELETE FROM lostitems WHERE ItemID = %s", (item_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Item marked as found successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500    



@app.route('/api/setLastBookRead', methods=['POST'])
def set_last_book_read():
    data = request.get_json()
    user_id = data.get('userId')
    book_id = data.get('bookId')

    if not user_id or not book_id:
        return jsonify({'error': 'Missing user ID or book ID'}), 400

    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check if a last read book already exists for the user
        cursor.execute('SELECT * FROM LastBookRead WHERE QalamID = %s', (user_id,))
        last_read = cursor.fetchone()
        
        if last_read:
            # If it exists, update it
            cursor.execute('UPDATE LastBookRead SET BookID = %s WHERE QalamID = %s', (book_id, user_id))
            print("UPDATE query ran")
        else:
            # If not, insert a new record
            cursor.execute('INSERT INTO LastBookRead (QalamID, BookID) VALUES (%s, %s)', (user_id, book_id))
        
        conn.commit()
        return jsonify({'message': 'Last read book updated successfully'}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# running the flask server    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug=True)
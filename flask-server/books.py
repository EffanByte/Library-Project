import mysql.connector
import base64
# API KEY for Google Books API here
#api_key = "AIzaSyC0duRJFDy8vZLT8-rnXqa6JawDxT8t-tQ"

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',   
        database='virtual_library'
    )

'''
def fetch_books_from_google(query):
    api_key = 'YOUR_API_KEY'
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=10&key={api_key}'
    response = requests.get(url)
    books_data = response.json()
    return books_data

def insert_book_into_db(book):
    conn = get_db_connection()
    cursor = conn.cursor()
    add_book = ("INSERT INTO books "
                "(Title, Author, Description, Genre, TypeID, coverUrl) "
                "VALUES (%s, %s, %s, %s, %s, %s)")
    book_data = (book['title'], book['authors'][0], book['description'], book['categories'][0], 1, book['thumbnail'])
    cursor.execute(add_book, book_data)
    conn.commit()
    cursor.close()
    conn.close()

# Fetch books data from Google Books API
books_data = fetch_books_from_google('undergraduate+studies')

book_count = 0 # counter to hold number of books processed

# Loop through the books and insert them into the database
for item in books_data['items']:
    # if 100 books inserted, break
    if book_count >= 100:
        break
    volume_info = item['volumeInfo']
    book = {
        'title': volume_info.get('title'),
        'authors': volume_info.get('authors', [''])[0],  # Assuming the first author
        'description': volume_info.get('description', ''),
        'categories': volume_info.get('categories', [''])[0],  # Assuming the first category
        'thumbnail': volume_info['imageLinks']['thumbnail'] if 'imageLinks' in volume_info else ''
    }
    # Insert the book into the database
    insert_book_into_db(book)
    book_count += 1 


'''


def get_books():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute('SELECT BookID, Title, Author, Description, Genre, TypeID, coverImage FROM books')
    books = cursor.fetchall()

    # Convert BLOB to base64 for each book
    for book in books:
        if book['coverImage']:
            book['coverImage'] = base64.b64encode(book['coverImage']).decode('utf-8')
    
    #print(books)        
    cursor.close()
    conn.close()
    return books

def get_book_by_id(book_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM books WHERE BookID = %s', (book_id,))
    book = cursor.fetchone()
    
    if book['coverImage']:
        book['coverImage'] = base64.b64encode(book['coverImage']).decode('utf-8')
    cursor.close()
    conn.close()
    return book

def get_book_by_title(book_title):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute('SELECT * FROM books WHERE LOWER(Title) = LOWER(%s)', (book_title,))
    book = cursor.fetchone()
    
    if book and book['coverImage']:
        book['coverImage'] = base64.b64encode(book['coverImage']).decode('utf-8')
    cursor.close()
    conn.close()
    return book

def add_book_to_db(title, author, genre, description, type_id, cover_image):
    conn = get_db_connection()
    cursor = conn.cursor()

    # If cover_image is a base64 string, decode it to binary
    if cover_image:
        cover_image = base64.b64decode(cover_image)

    query = '''INSERT INTO books (Title, Author, Genre, Description, TypeID, coverImage)
               VALUES (%s, %s, %s, %s, %s, %s)'''
    
    cursor.execute(query, (title, author, genre, description, type_id, cover_image))
    conn.commit()

    cursor.close()
    conn.close()

def add_pdf_to_book(book_id, pdf_data):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO BookPDFs (BookID, PDF) VALUES (%s, %s)"
    cursor.execute(query, (book_id, pdf_data))
    conn.commit()
    cursor.close()
    conn.close()

def update_book(book_id, book_data):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            query = """
            UPDATE books
            SET Title = %s, Author = %s, Description = %s, Genre = %s, TypeID = %s
            WHERE BookID = %s
            """
            values = (book_data['Title'], book_data['Author'], book_data['Description'], book_data['Genre'], book_data['TypeID'], book_id)
            cursor.execute(query, values)
            affected_rows = cursor.rowcount

            # If there's a new PDF, update it
            if 'PDF' in book_data and book_data['PDF']:
                update_pdf_for_book(book_id, book_data['PDF'])

            conn.commit()

        return affected_rows > 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        conn.close()


def update_pdf_for_book(book_id, pdf_file):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            pdf_data = pdf_file.read()  # Assuming pdf_file is a file object
            query = "UPDATE BookPDFs SET PDF = %s WHERE BookID = %s"
            cursor.execute(query, (pdf_data, book_id))
            conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


# Function to manually insert an image of book cover into the database
def insert_image(book_id, file_path):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Read the image file in binary mode
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    
    # Prepare the update statement
    query = "UPDATE books SET coverImage = %s WHERE BookID = %s"
    
    # Execute the query
    cursor.execute(query, (binary_data, book_id))
    
    # Commit the changes
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()

get_books()

# manually calling function for image insertion
'''book_id = 7
file_path = '/Users/hamzariaz/VSCODE/Virtual Library Project/Library-Project/public/bookCovers/id=7_cover.jpeg'  
insert_image(book_id, file_path)'''




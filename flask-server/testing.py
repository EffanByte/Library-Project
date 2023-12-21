from server import *

qalam_id = 414577
conn = get_db_connection()
cursor = conn.cursor(dictionary=True)
call_proc = "Call getLastBookRead(%s)"
cursor.execute(call_proc, (qalam_id,))
#cursor.callproc('getLastBookRead', [qalam_id])
last_book_read = cursor.fetchone()

cursor.close()
conn.close()
if last_book_read and last_book_read['coverImage']:
    # Convert BLOB data to base64
    cover_image_base64 = base64.b64encode(last_book_read['coverImage']).decode('utf-8')
    last_book_read['coverImage'] = cover_image_base64
    print(last_book_read)
#return jsonify(last_book_read), 200
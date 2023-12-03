from flask import Flask, jsonify
from flask_cors import CORS
from books import *

app = Flask(__name__)
CORS(app)



@app.route('/api/books', methods=['GET'])
def api_get_books():
    try:
        books = get_books()
        return jsonify(books)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug=True)

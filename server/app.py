import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

# a list of books
BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False
    # BOOKS[:] = [book for book in BOOKS if book['id'] != book_id]
    # return bool(len(BOOKS) < len(BOOKS[:]))


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# get all books or add a new book
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # check for required fields
        if not post_data.get('title') or not post_data.get('author'):
            response_object['message'] = 'Missing required fields.'
            return jsonify(response_object), 400
        if not post_data.get('read'):
            post_data['read'] = False
        # check if book already exists
        if any(book['title'] == post_data.get('title') and book['author'] == post_data.get('author') for book in BOOKS):
            response_object['message'] = 'Book already exists!'
            return jsonify(response_object), 400
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

# update or delete a book
@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if remove_book(book_id):
        if request.method == 'PUT':
            post_data = request.get_json()
            BOOKS.append({
                'id': uuid.uuid4().hex,
                'title': post_data.get('title'),
                'author': post_data.get('author'),
                'read': post_data.get('read')
            })
            response_object['message'] = 'Book updated!'
        if request.method == 'DELETE':
            response_object['message'] = 'Book removed!'
        return jsonify(response_object)
    else:
        response_object['message'] = 'Book not found!'
        return jsonify(response_object), 404


if __name__ == '__main__':
    app.run()

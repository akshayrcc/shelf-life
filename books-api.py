from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from api_constants import mongdb_username, mongodb_pass, mongdb_dbname
import urllib

# from  flask_mysqldb import MySQL
import pymysql
from flask_cors import CORS

# import MySQLdb.cursors
# import re
# from datetime import timedelta

app = Flask(__name__)

# DB_URI = "mongodb+srv://{}:{}@cluster0.jgh89vm.mongodb.net/{}".format(
#     urllib.parse.quote_plus(mongdb_username), urllib.parse.quote_plus(mongodb_pass), mongdb_dbname,
# )

DB_URI = "mongodb+srv://akshayrc:Pass%40007@cluster0.jgh89vm.mongodb.net/API"

app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)

# CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def index():
    return "Hello, World!"


# create Book model
class Book(db.Document):
    title = db.StringField(required=True)
    author = db.StringField(required=True)
    price = db.FloatField(required=True)


# create routes for CRUD operations
# @app.route('/books', methods=['POST'])
# def create_book():
#     book_data = request.json
#     book = Book(**book_data).save()
#     return jsonify({'message': 'Book created successfully'})

@app.route('/books', methods=['POST'])
def create_book():
    books = request.json
    created_books = []
    for book_data in books:
        book = Book(**book_data)
        book.save()
        created_books.append(book)
    return jsonify(created_books), 201


@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.objects.all()
    response = []
    for book in books:
        response.append({'title': book.title, 'author': book.author, 'price': book.price})
    return jsonify(response)


@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book = Book.objects(id=id).first()
    if book:
        response = {'title': book.title, 'author': book.author, 'price': book.price}
    else:
        response = {'message': 'Book not found'}
    return jsonify(response)


@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    book_data = request.json
    result = Book.objects(id=id).update_one(**book_data)
    if result:
        response = {'message': 'Book updated successfully'}
    else:
        response = {'message': 'Book not found'}
    return jsonify(response)


@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    result = Book.objects(id=id).delete()
    if result:
        response = {'message': 'Book deleted successfully'}
    else:
        response = {'message': 'Book not found'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)  # application will start listening for web request on port 5000

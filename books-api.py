from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from mongoengine import connect, Document, StringField, FloatField, DoesNotExist, ValidationError
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

from api_constants import mongdb_username, mongodb_pass, mongdb_dbname
import urllib

# from  flask_mysqldb import MySQL
import pymysql
from flask_cors import CORS

# import MySQLdb.cursors
# import re
# from datetime import timedelta

app = Flask(__name__)

DB_URI = "mongodb+srv://{}:{}@cluster0.jgh89vm.mongodb.net/{}".format(
    urllib.parse.quote_plus(mongdb_username), urllib.parse.quote_plus(mongodb_pass), mongdb_dbname,
)

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
    title = db.StringField(required=True, max_length=100)
    author = db.StringField(required=True, max_length=100)
    price = db.FloatField(required=True, min_value=0)


# create routes for CRUD operations
# @app.route('/books', methods=['POST'])
# def create_book():
#     book_data = request.json
#     book = Book(**book_data).save()
#     return jsonify({'message': 'Book created successfully'})

@app.route('/books', methods=['POST'])
def create_book():
    try:
        book_data = request.json
        book = Book(**book_data)
        book.save()
        return book.to_json(), 201
    except (ValueError, KeyError):
        raise BadRequest("Invalid book data")


@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.objects().to_json()
    return books, 200


@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
        return book.to_json(), 200
    except DoesNotExist:
        raise NotFound("Book not found")
    except ValidationError:
        raise BadRequest("Invalid book ID")


@app.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    try:
        book = Book.objects(id=book_id).first()
        if not book:
            raise NotFound("Book not found")
        book_data = request.json
        book.update(**book_data)
        return book.to_json(), 200
    except (ValueError, KeyError):
        raise BadRequest("Invalid book data")


@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return '', 204  #returning No Content after deletion
    except DoesNotExist:
        raise NotFound("Book not found")
    except ValidationError:
        raise BadRequest("Invalid book ID")



@app.errorhandler(BadRequest)
@app.errorhandler(NotFound)
@app.errorhandler(InternalServerError)
def handle_errors(error):
    response = jsonify({'error': str(error)})
    response.status_code = error.code if hasattr(error, 'code') else 500
    return response


if __name__ == '__main__':
    app.run(debug=True)  # application will start listening for web request on port 5000

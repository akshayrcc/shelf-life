# Shelf Life: Books API

Building a RESTful API with Flask - Error Handling, Authentication, and
File Handling with Public and Admin Routes

## Setup:

### Steps to run:

    python -m venv env
    source env/bin/activate  OR  .\venv\Scripts\activate.bat
    pip install -r requirements.txt
    python3 books-api.py
    hit localhost:5000.

### Command for virtual env:

    python3 -m venv venv --system-site-packages
    source venv/bin/activate
    deactivate

### Dependencies:

    Install python, flask, mysql.
    pip3 install mongoengine flask-mongoengine dnspython

## Requirements:

### Task 1: Setting up the Flask application

</br>● Create a new Flask application and set up the necessary packages and modules.
</br>● Create a virtual environment for the application.
</br>● Connect your Flask application with the Database (MySQL preferably.)

### Task 2: Error Handling

</br>● Implement error handling for your API to ensure that it returns proper error
messages and status codes.
</br>● Create error handlers for ex. 400, 401, 404, 500, and any other errors that you feel
are necessary.
</br>● Make sure that error messages are returned in a consistent format.

### Task 3: Authentication

</br>● Implement authentication for your API using JWT Authentication.
</br>● Create a user model with username and password fields.
</br>● Implement a login endpoint that authenticates the user and returns a JWT token.
</br>● Implement a protected endpoint that requires a valid JWT token to access.

### Task 4: File Handling

</br>● Implement file handling for your API to allow users to upload files.
</br>● Create an endpoint that allows users to upload files.
</br>● Implement file validation to ensure that only certain file types are allowed.
</br>● Implement file size validation to ensure that files are uploaded within the allowed
file size limit.
</br>● Store uploaded files in a secure location. (A folder in your project’s folder
structure.)

### Task 5: Public Route

</br>● Create a public route that allows users to view public information.
</br>● Implement an endpoint that returns a list of items that can be viewed publicly.
</br>● Ensure that this endpoint does not require authentication.

# User Guide for the Flask-based Books Management API

Welcome to the user guide for the Flask-based Books Management API. This guide will walk you through the various features and functionalities of the API, providing instructions on how to register, log in, manage books, and upload files.

## User Registration

1. To create a new account, visit the `/register` endpoint.
2. Provide your desired username and password in the JSON payload.
3. Upon successful registration, you will receive a JSON response containing your user ID, username, and a JWT token. Keep this token safe as it will be required for accessing protected routes.

## User Authentication

1. To log in to your existing account, use the `/login` endpoint.
2. Provide your username and password in the JSON payload.
3. A successful login will return a JSON response containing a JWT token. This token is essential for accessing protected routes.

## Book Management

### Viewing a List of Books

1. To view a list of all available books, visit the `/books` endpoint.
2. The response will include a list of JSON objects, each representing a book. Each object will contain the title and ID of the book.

### Searching for Books by Title

1. To search for books by title, use the `/books/search?title=<title>` endpoint.
2. Replace `<title>` with the title of the book you are looking for.
3. The response will include a list of JSON objects, each representing a book matching the given title. The objects will contain the title and ID of each book.

### Getting Detailed Information about a Book

1. To get detailed information about a specific book, use the `/books/<book_id>` endpoint.
2. Replace `<book_id>` with the ID of the book you want to view.
3. The response will provide complete details of the book, including its title, author, price, and other relevant information.

### Adding a New Book

1. To add a new book, you will need to have a valid JWT token from a successful login.
2. Use the `/books` endpoint and provide the book's title, author, and price in the JSON payload.
3. Make sure to include the JWT token in the Authorization header of the request.
4. Upon successful creation, the API will return a JSON response containing the newly created book's details.

## File Uploading

1. To upload a file, use the `/upload-file` endpoint.
2. The endpoint accepts multi-part file uploads, allowing you to upload various types of files.
3. Ensure that the file you are uploading meets the specified requirements, such as file type and size restrictions.

## Public Route

The `/books` endpoint is accessible without authentication, allowing anyone to view a list of available books.

## General Guidelines

- The API handles errors gracefully and provides informative error messages.
- All user input is validated to prevent malicious or invalid data from being entered.
- Uploaded files are validated to ensure they are of the correct type and do not exceed the maximum file size.
- Uploaded files are stored securely on the server.
- JWT authentication protects sensitive routes, preventing unauthorized access.
- Error messages are clear, concise, and informative, adhering to a consistent format.
- The user model securely stores user credentials, including usernames and passwords.
- The login endpoint returns a JWT token for accessing protected routes.
- The protected endpoint requires a valid JWT token in the Authorization header.
- The endpoint for uploading files allows users to upload files within the specified type and size limits.

## Project Details:

Flask routes:

    GET /:
    Returns a simple "Hello, World!" message.

    POST /register:
    Registers a new user with the given username and password in the JSON payload. The response includes the user's id, username, and a JWT token.

    POST /login:
    Logs in a user with the given username and password in the JSON payload. The response includes a JWT token that needs to be used for accessing the protected routes.

    GET /books:
    Returns a list of all the books available in the database with only title and id fields.

    POST /books:
    Adds a new book with the given title, author, and price in the JSON payload. This endpoint is protected and needs a JWT token in the Authorization header.

    GET /books/search?title=<title>:
    Searches for books by their title. The response includes a list of books matching the given title with only title and id fields.

    GET /books/<book_id>:
    Gets the details of a book with the given book_id. The response includes the details of the book including title, author, and price. This endpoint is protected and needs a JWT token in the Authorization header.

    POST /upload-file
    Uploads a multi-part file to uploads directory.

MongoDB models:

    User: Represents a user with username and password fields.
    Book: Represents a book with title, author, and price fields.

Function:

    authenticate_user that takes a JWT token as input and returns the corresponding user if the token is valid and has not expired.
    This function is used to authenticate requests to the /books and /books/<book_id> routes.

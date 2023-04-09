# My Flask App
## Setup:
### Steps to run:
    Create a directory for Flask. e.g. D:\Flask\
    In cmd, cd D:\Flask.
    pip install virtualenv
    .\venv\Scripts\activate.bat
    pip install Flask
    create app.py
    write code there and python app.py
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

MongoDB models:

    User: Represents a user with username and password fields.
    Book: Represents a book with title, author, and price fields.

Function:

    authenticate_user that takes a JWT token as input and returns the corresponding user if the token is valid and has not expired. 
    This function is used to authenticate requests to the /books and /books/<book_id> routes.
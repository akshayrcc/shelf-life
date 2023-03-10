from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config[‘MYSQL_USER’] = ‘USERNAME  goes here’ 
app.config[‘MYSQL_PASSWORD’] = ‘PASSWORD  goes here’ 
app.config[‘MYSQL_HOST’] = ‘Name of HOST (server) goes here’ 
app.config[‘MYSQL_DB’] = ‘DATABASE name goes here’ 
app.config[‘MYSQL_CURSORCLASS’] = DictCursor // A cursor which returns results as a dictionary
mysql = MySQL(app)

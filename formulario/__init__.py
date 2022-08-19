from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

"""
import secrets
secrets.token_hex(16)
Gera uma 'secret_key'
"""
app.config['SECRET_KEY'] = 'dba3334567fe8cfcf7c36678c5587b36'
app.config['MYSQL_HOST'] = 'your localhost'
app.config['MYSQL_USER'] = 'your user'
app.config['MYSQL_PASSWORD'] = 'your password'
app.config['MYSQL_DB'] = 'your DB'

mysql = MySQL(app)

from formulario import routes

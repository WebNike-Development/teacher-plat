from flask import Flask, request, render_template, session, redirect, url_for, json
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)

mysql = MySQL(app)
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_PORT']= 3306
# app.config['MYSQL_DB'] = 'website_tp'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# app.config['SECRET_KEY'] = 'KHEZ1RQUCB8ZIT0GA9AU18X9H0CLGNW5OTH86P0C764W4QQ5Z0'

app.config['MYSQL_USER'] = 'sql6518557'
app.config['MYSQL_PASSWORD'] = '7meuSewnL7'
app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_PORT']= 3306
app.config['MYSQL_DB'] = 'sql6518557'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = 'KHEZ1RQUCB8ZIT0GA9AU18X9H0CLGNW5OTH86P0C764W4QQ5Z0'

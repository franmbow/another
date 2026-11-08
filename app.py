from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# crear base de datos sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mibase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
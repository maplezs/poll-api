from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask('__main__')
CORS(app)

app.config['SECRET_KEY'] = 'xxyyzz'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:9gYnTWLACG3dkhA@34.121.171.7/hayuk_test'

db = SQLAlchemy(app)

from script import routes
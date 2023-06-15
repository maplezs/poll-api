from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Konfigurasi dasar aplikasi
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'xxyyzz'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:9gYnTWLACG3dkhA@34.121.171.7/hayuk_test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/hayuk_test'

# Membuat koneksi ke database
db = SQLAlchemy(app)

# Membuat alat enkripsi password
bcrypt = Bcrypt(app)

# Membuat sistem login
login_manager = LoginManager(app)
login_manager.view = 'login'
login_manager.login_message_category = 'danger'

from script import routes
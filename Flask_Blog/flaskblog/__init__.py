from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)


# Generate a secret key
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# Set up location of database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Hash the password
bcrypt = Bcrypt()

# Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Config email infomation
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'chaoya_d@126.com'
app.config['MAIL_PASSWORD'] = 'JinYan1211'
mail = Mail(app)

from flaskblog import routes
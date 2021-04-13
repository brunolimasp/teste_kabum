from flask import *
import os
from werkzeug.utils import secure_filename
from flask_pymysql import MySQL
from flask_recaptcha import ReCaptcha
from flask_mail import Mail, Message
import boto3
from botocore.client import Config
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask_script import Manager
from flask_migrate  import Migrate, MigrateCommand



# ------------------------------ FLASK ---------------------------------
app = Flask(__name__)
   


# ------------------------ CONFIGURAÇÂO CORS API ------------------------------
CORS(app, resources={r"/*": {"origins": "*"}})

# ------------------------------ FLASK-EMAIL ---------------------------------
mail = Mail(app)
app.config['MAIL_SERVER'] = "mail.transparency.com.br"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "doors@transparency.com.br"
app.config['MAIL_PASSWORD'] = "transparency@13"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail.init_app(app)

# ---------------------------CHAVE GOOGLE reCAPTCHA-----------------------------

recaptcha = ReCaptcha(app=app)
app.config.update(dict(
    RECAPTCHA_ENABLED=True,
    RECAPTCHA_SITE_KEY="6LcrrKcZAAAAALexI0sezl8gOb4FaueucQ01CAZM",
    RECAPTCHA_SECRET_KEY="6LcrrKcZAAAAACMIjpgCjgq0DJ3wdnAQwsiZc-zN"
))
recaptcha.init_app(app)

# ------------------------ CONEXAO COM O BANCO DE DADOS  ----------------------

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:32961018@bbreno.ddns.net/Banco'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:32961018@bbreno.ddns.net/doors'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# ------------------------------ MIGRATE PARA O BANCO DE DADOS ---------------------------------
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# ---------------------------- SESSÃO DO USAUARIO --------------------------------

app.secret_key = 'Kamehamehaaaaaaaaaaaaaaaaaaa'
app.config["SESSION_PERMANENT"] = True

# ---------------------------CHAMADA DOS CONTROLLERS------------------------------
from app.controllers.www import index
from app.controllers.system import login, dashboard, profile
from app.controllers.suprimentos import main
from app.controllers.rm import main
from app.controllers.vistoria import main


# ----------------------CHAMADA DOS MODELS BANCO DE DADOS--------------------------
from app.models.system import users, modules
from app.models.suprimentos import estoque
from app.models.rm import rm



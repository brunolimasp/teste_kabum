from flask import *
from flask_cors import CORS, cross_origin



# ------------------------------ FLASK ---------------------------------
app = Flask(__name__)  
# ------------------------ CONFIGURAÇÂO CORS API ------------------------------
CORS(app, resources={r"/*": {"origins": "*"}})


# ---------------------------CHAMADA DOS CONTROLLERS------------------------------
from app.controllers.www import index
from app.controllers.api import api_frete



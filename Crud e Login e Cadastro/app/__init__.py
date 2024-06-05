from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from app.models import user, product
from app.views import auth, product as product_view

app.register_blueprint(auth.auth_bp)
app.register_blueprint(product_view.product_bp)
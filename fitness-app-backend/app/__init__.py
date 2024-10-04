from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from .routes.auth import auth_blueprint

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
jwt = JWTManager(app)

app.register_blueprint(auth_blueprint, url_prefix='/api/auth')

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

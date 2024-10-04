from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == 'testuser' and check_password_hash('hashed_password', password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad username or password"}), 401
from alembic.operations import Operations
from flask import request, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import create_access_token
from models import User
from werkzeug.security import check_password_hash

auth_blp = Blueprint('auth', __name__,description="Operations on todos" ,url_prefix='/auth')

@auth_blp.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        print('if not request.is_json')
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        print('if not username or password')
        return jsonify({"msg": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    print("user here?",user)
    print("user here?",user)
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"msg":"Invalid username or password"}), 401
#API LIST
#전체 유저 데이터 조회 GET
#특정 유저 데이터 조회 GET
#유저 생성  POST
#특정 유저 데이터 업데이트 PUT
#특정 유저 삭제 DELETE

from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import User

user_blp = Blueprint('Users','users',description="Operations on board",url_prefix= '/user')

@user_blp.route('/')
class Userlist(MethodView):
    def get(self,user):
        users = User.query.all()
        #for user in users:
        #print(user.id)
        #print(user.name)
        #print(user.email)

        user_data = [
            {"id":user.id,"name":user.name,"email":user.email} for user in users
        ]

        return jsonify(user_data)

    def post(self):
        data = request.get_json()
        new_user = User(name=data['name'],email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'msg':"success create new user"}),201

@user_blp.route('/<int:user_id>')
class UserResource(MethodView):
    def get(self,user_id):
        user = User.query.get_or_404(user_id)
        return jsonify({'name':user.name,'email':user.email})

    def put(self,user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json

        user.name = data['name']
        user.email = data['email']

        db.session.commit()

        return jsonify({'msg':"success update user"}),201

    def delete(self,user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'msg':"success delete user"}),201
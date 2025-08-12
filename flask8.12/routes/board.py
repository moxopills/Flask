#전체 게시글을 가져오는 API GET
#게시글을 작성하는 API POST

#하나의 게시글 불러오기 GET
#특정게시글 수정 PUT
#특정게시글 삭제 DELETE

from flask_smorest import Blueprint
from flask import request, jsonify, Flask
from flask.views import MethodView
from db import db
from models import Board

board_blp = Blueprint('Boards','boards',description='Operations on board', url_prefix='/board')

@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()
      #  for board in boards:
       #     print('id',board.id)
        #    print('title', board.title)
         #   print('content', board.content)
          #  print('user_id', board.user_id)
           # print('auther_name', board.auther_name)
            #print('auther_email', board.auther_email)
        return jsonify({"id":board.id,"title":board.title,"content":board.content,"auther_name":board.auther.name,"auther_email":board.auther.email}for board in boards)

    def post(self):
        data = request.get_json()
        new_board = Board(title=data['title'],content=data['content'],user_id=['user.id'])
        db.session.add(new_board)
        db.session.commit()
        return jsonify({'msg':"success create new board"}),201

@board_blp.route('/<int:id>')
class Boardresource(MethodView):
    def get(self):
        board = Board.query.get_or_404(id)
        return jsonify({"id":board.id,
                        "title":board.title,
                        "content":board.content,
                        "user_id":board.user_id,
                        "auther_name":board.auther.name,
                        "auther_email":board.auther.email
                        })

    def put(self,board_id):
        board = Board.query.get_or_404(board_id)

        data = request.get_json()
        board.title = data('title')
        board.content = data('content')

        db.session.commit()
        return jsonify({'msg':"success update board data"}),201

    def delete(self,board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()
        return jsonify({'msg':"success delete board data"}),201
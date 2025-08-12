#model 만든다는것은 테이블을 만드는 것
#게시글 - board
#유저 - user

from db import db

class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    email = db.Column(db.String(100), nullable=False)
    boards = db.relationship("Board", back_populates="author",lazy="dynamic")

class Board(db.Model):
    __tablename__ = "Boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100) , nullable=False)
    content = db.column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
    author = db.relationship("User", back_populates="boards")
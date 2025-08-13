from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_posts_blueprint(mysql):
    posts_blp = Blueprint("posts", __name__, description="posts api", url_prefix="/posts")

    @posts_blp.route("/", methods=["GET", "POST"])
    def posts():
        cursor = mysql.connection.cursor()

        if request.method == "GET":
            sql = "SELECT * FROM posts"
            cursor.execute(sql)
            posts_data = cursor.fetchall()
            cursor.close()

            post_list = []
            for post in posts_data:
                post_list.append({
                    'id': post[0],
                    'title': post[1],
                    'content': post[2],
                })
            return jsonify(post_list)

        elif request.method == "POST":
            data = request.get_json()
            if not data:
                abort(400, message="Invalid JSON")

            title = data.get('title')
            content = data.get('content')

            if not title or not content:
                abort(400, message="Title or content is empty")

            sql = "INSERT INTO posts (title, content) VALUES (%s, %s)"
            cursor.execute(sql, (title, content))
            mysql.connection.commit() # 이 부분을 추가했습니다.
            cursor.close()

            return jsonify({'msg': 'success', 'title': title, 'content': content})

    @posts_blp.route('/<int:id>', methods=["GET", "PUT", "DELETE"])
    def post_id(id):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM posts WHERE id = %s"
        cursor.execute(sql, (id,))
        post = cursor.fetchone()

        if request.method == "GET":
            cursor.close()
            if not post:
                abort(404, message="Post not found")
            return jsonify({'id': post[0], 'title': post[1], 'content': post[2]})

        elif request.method == "PUT":
            data = request.get_json()
            if not data:
                abort(400, message="Invalid JSON")
            title = data.get('title')
            content = data.get('content')

            if not title or not content:
                abort(400, message="Title and content required")
            if not post:
                abort(404, message="Post not found")

            sql = "UPDATE posts SET title=%s, content=%s WHERE id=%s"
            cursor.execute(sql, (title, content, id))
            mysql.connection.commit() # 이 부분을 추가했습니다.
            cursor.close()
            return jsonify({'msg': 'success update'})

        elif request.method == "DELETE":
            if not post:
                abort(404, message="Post not found")
            sql = "DELETE FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            mysql.connection.commit() # 이 부분을 추가했습니다.
            cursor.close()
            return jsonify({'msg': 'success delete'})

    return posts_blp
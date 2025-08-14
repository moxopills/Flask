from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = [
    {
        "username": "pedri",
        "post": [{"title": "visca barca!","Like": 2002}]
    },
    {
        "username": "Harry James Potter",
        "post": [{"title": "The Boy Who Lived","Like": 1980}]
    },
    {
        "username": "Larry Page",
        "post": [{"title": "GooGle!","Like": 1973}]
    }
]

@app.get('/')
def index():
    return render_template('index.html')

@app.get("/users")
def get_users():
    return {"users":users}

@app.post("/users")
def create_users():
    request_data = request.get_json()
    new_user = {"username": request_data["username"],"post":[{"title":"Come Back Home", "Like":818}]}
    users.append(new_user)
    return new_user

@app.get("/users/post/<string:username>")
def get_posts_of_user(username):
    for user in users:
        if user["username"] == username:
            return{"post":user["post"]}
    return {"msg":"NO User Found"}

@app.get("/users/post/Like/<string: username>/<string: title>")
def get_like_of_user(username,title):
    for user in users:
        if user["username"] == username:
            for post in user["post"]:
                if post["title"] == title:
                    post["Like"] += 1
                    return post
    return {"msg": "Post Not Found"}, 404

@app.delete("/users/<string:username>")
def delete_user(username):
    global users
    users = [user for user in users if user["username"] == username]
    return {"msg": "User Deleted"},200

if __name__ == '__main__':
    app.run(debug=True)
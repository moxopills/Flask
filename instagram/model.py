from sqlalchemy.testing.pickleable import User

users = [
    {
        "username":"pedri", "post":[{"title":"visca barca!","Like":2002}]
    },
    {
        "username":"Harry James Potter", "post":[{"title":"The Boy Who Lived","Like": 1980}]
    },
    {
        "username":"Larry Page", "post":[{"title":"GooGle!","Like": 1973}]
    },
]

def add_user(request_data):
    new_user = {"username" : request_data["username"],"post":[]}
    users.append(new_user)
    return new_user,201

def add_post_user(username, request_data):
    for user in users:
        if user["username"] == username:
            new_post = {"title": request_data["title"],"like": 0 }
            user["post"].append(new_post)
            return new_post,201
    return {"msg":"User Not Found"}

def get_user_post(username,title):
    for user in users:
        if user["username"] == username:
            for post in user["post"]:
                if post["title"] == title:
                    post["like"] = post["like"] + 1
                    return post,201
    return {"msg": "Post Not Found"},404

def delete_user(username):
    global users
    users = [user for user in users if users["username"]!=username]
    return {"msg": "User Deleted"},200
from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

users = [
    {"username": "Beginner Backend Developer", "name": "minsoo"},
    {"username": "Soccer Player", "name": "Frenkie de jong"},
    {"username": "Spider-Man", "name": "Peter Benjamin Parker"}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
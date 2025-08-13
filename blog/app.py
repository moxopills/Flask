from flask import Flask
from flask_mysqldb import MySQL
from flask_smorest import Api
import yaml
from posts_routes import create_posts_blueprint

db_info = yaml.load(open('db.yaml', 'r'), Loader=yaml.FullLoader)
app = Flask(__name__)
app.config['MYSQL_HOST'] = db_info['mysql_host']
app.config['MYSQL_USER'] = db_info['mysql_user']
app.config['MYSQL_PASSWORD'] = db_info['mysql_password']
app.config['MYSQL_DB'] = db_info['mysql_db']

mysql = MySQL(app)
app.config['API_TITLE'] = 'Blog API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
posts_blp = create_posts_blueprint(mysql)
api.register_blueprint(posts_blp)

from flask import render_template
@app.route('/blogs')
def manage_blogs():
    return render_template("posts.html")

if __name__ == '__main__':
    app.run(debug=True)
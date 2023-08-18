from flask import Flask
from flask_session import Session

from controller.authentication.login import authentication
from controller.main import teacher_route, parent_route
from model.role import Role

app = Flask(__name__)
app.secret_key = "super secret key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(authentication)
app.register_blueprint(parent_route)
app.register_blueprint(teacher_route)


@app.context_processor
def inject_role():
    return dict(Role=Role)


print(app.url_map)
app.run(host='127.0.0.1', port=1337, debug=True)

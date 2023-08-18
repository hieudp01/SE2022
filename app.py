from flask import Flask

from controller.authentication.login import authentication
from controller.main import teacher_route, parent_route

app = Flask(__name__)
app.secret_key = "super secret key"

app.register_blueprint(authentication)
app.register_blueprint(parent_route)
app.register_blueprint(teacher_route)

print(app.url_map)

app.run(host='127.0.0.1', port=1337, debug=True)

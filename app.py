from flask import Flask
from controller.authentication.login import auth
from controller.parent.route import parent_route

app = Flask(__name__)
app.secret_key = "super secret key"

app.register_blueprint(auth)
app.register_blueprint(parent_route)

app.run(host='127.0.0.1', port=1337, debug=True)

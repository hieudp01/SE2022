from flask import Flask, render_template, request, redirect, url_for, flash
from controller.authentication.login import auth

app = Flask(__name__)

app.register_blueprint(auth, url_prefix='/login')

app.run(host='127.0.0.1', port=1337, debug=True)

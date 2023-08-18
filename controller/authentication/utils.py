import bcrypt
from flask import Blueprint, render_template, request, session, redirect, url_for

from model.role import Role


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def login(user, col, role):
    if request.form.get("username") is None or request.form.get("password") is None:
        return render_template('authentication/login.html', role=role, error="Username or password is empty")

    user = user.query.where(col == request.form['username']).first()
    if user is None or not verify_password(request.form['password'], user.password):
        return render_template('authentication/login.html', role=role,
                               error="Username or password is incorrect")
    return user

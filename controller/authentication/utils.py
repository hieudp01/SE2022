import bcrypt
from flask import Blueprint, render_template, request, session, redirect, url_for

from model.role import Role
from model.Teacher import Teacher


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def verify_password_no_hash(password, db_pass):
    return password == db_pass


def login(user, col, role):
    if request.form.get("username") is None or request.form.get("password") is None:
        return render_template('authentication/login.html', role=role, error="Username or password is empty")

    print(request.form['username'])
    print(request.form['password'])

    user = user.query.where(col == request.form['username']).first()
    
    if user is None or not verify_password_no_hash(request.form['password'], user.password):
        return render_template('authentication/login.html', role=role, error="Username or password is incorrect")
    return user

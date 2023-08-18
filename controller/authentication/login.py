from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('login', __name__)


@auth.get('/')
def parent_page():
    return render_template('authentication/login.html')


@auth.post('/')
def login():
    pass


@auth.get('/teacher')
def teacher_page():
    return render_template('authentication/teacher-login.html')


@auth.post('/teacher')
def teacher_login():
    pass


@auth.get('/admin')
def admin_page():
    return render_template('authentication/admin-login.html')

@auth.get('/parents')
def parents_page():
    return render_template('authentication/parent.html')



@auth.post('/admin')
def admin_login():
    pass

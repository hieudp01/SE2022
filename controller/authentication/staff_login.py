from flask import Blueprint, render_template, request, session

from model.role import Role

staff_auth = Blueprint('login', __name__, url_prefix='/login', subdomain='staff')


@staff_auth.get('/teacher')
def teacher_page():
    return render_template('authentication/login.html', role=Role.TEACHER)


@staff_auth.post('/teacher')
def teacher_login():
    pass


@staff_auth.get('/admin')
def admin_page():
    return render_template('authentication/login.html', role=Role.ADMIN)


@staff_auth.post('/admin')
def admin_login():
    pass

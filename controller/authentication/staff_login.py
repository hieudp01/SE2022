from flask import Blueprint, render_template, session, redirect, url_for

from controller.authentication import utils
from model.Teacher import Teacher
from model.role import Role

teacher_auth = Blueprint('teacher_auth', __name__, url_prefix='/auth', subdomain='teacher')


@teacher_auth.get('/')
def index():
    return render_template('authentication/login.html', role=Role.TEACHER)


@teacher_auth.get('/logout')
def logout():
    session.clear()
    return redirect(url_for('teacher_auth.index'))


@teacher_auth.post('/')
def login():
    teacher = utils.login(Teacher, Teacher.email, Role.TEACHER)
    if type(teacher) is str:
        return teacher

    session['user'] = {
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email,
        "phone": teacher.phone,
        "role": Teacher.get_role(),
        "class_id": teacher.class_id
    }

    return render_template('index/teacher.html', role=Role.TEACHER)

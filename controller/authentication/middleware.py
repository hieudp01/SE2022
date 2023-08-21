from functools import wraps

from flask import redirect, url_for, session

from model.role import Role


def __login_required(f, role: list):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return_url = url_for("auth.index")
        if role == [Role.TEACHER.value]:
            return_url = url_for('teacher_auth.index')
        if 'user' not in session or session['user'] is None:
            return redirect(return_url)
        for r in role:
            if session['user']['role'] == r:
                return f(*args, **kwargs)
        return redirect(return_url)

    return decorated_function


def parent_required(f):
    return __login_required(f, [Role.PARENT.value])


def teacher_required(f):
    return __login_required(f, [Role.TEACHER.value])


def parent_or_teacher_required(f):
    return __login_required(f, [Role.TEACHER.value, Role.PARENT.value])


def admin_required(f):
    return __login_required(f, [Role.ADMIN.value])


def auth_required(f):
    return __login_required(f, [Role.ADMIN.value, Role.TEACHER.value, Role.PARENT.value])

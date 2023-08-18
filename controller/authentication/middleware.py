from functools import wraps

from flask import redirect, url_for, session

from model.role import Role


def login_required(f, role: list):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session or session['user'] is None:
            return redirect(url_for('login.parent_page'))
        for r in role:
            if session['user']['role'] == r:
                return f(*args, **kwargs)
        return redirect(url_for('login.parent_page'))

    return decorated_function


def parent_required(f):
    return login_required(f, [Role.PARENT.value])


def teacher_required(f):
    return login_required(f, [Role.TEACHER.value])


def admin_required(f):
    return login_required(f, [Role.ADMIN.value])

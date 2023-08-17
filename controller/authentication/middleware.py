from functools import wraps

from flask import redirect, url_for, session


def login_required(f, role: list):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session or session['user'] is None:
            return redirect(url_for('login.parent_page'))
        for r in role:
            if session['user']['role'] == r:
                return f(*args, **kwargs)

    return decorated_function


def teacher_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session or session['user'] is None:
            return redirect(url_for('login.teacher_page'))
        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session or session['user'] is None:
            return redirect(url_for('login.admin_page'))
        return f(*args, **kwargs)

    return decorated_function

from flask import Blueprint, render_template, request, session, url_for, redirect

from model.Children import Children
from model.Class import Class
from model.Parent import Parent
from controller.authentication import utils
from model.role import Role

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.get('/')
def index():
    return render_template('authentication/login.html', role=Role.PARENT)


@auth.get('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.index'))


@auth.post('/')
def login():
    parent = utils.login(Parent, Parent.id, Role.PARENT)
    if type(parent) is str:
        return parent

    session['user'] = {
        "id": parent.id,
        "name": parent.name,
        "email": parent.email,
        "phone": parent.phone,
        "role": Parent.get_role()
    }


    children = Children.query.where(Children.parent_id == parent.id).join(Class).all()
    allowed_children = [child.id for child in children]

    session['children'] = allowed_children
    return redirect(url_for('parent.index'))

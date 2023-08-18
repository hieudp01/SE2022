from flask import Blueprint, render_template, request, session, url_for, redirect

from model.Children import Children
from model.Class import Class
from model.Parent import Parent
from controller.authentication import utils
from model.role import Role

authentication = Blueprint('login', __name__, url_prefix='/login')


@authentication.get('/')
def parent_page():
    return render_template('authentication/login.html', role=Role.PARENT, role_list=Role)


@authentication.post('/')
def login():
    if request.form.get("username") is None or request.form.get("password") is None:
        return render_template('authentication/login.html', error="Username or password is empty")

    parent = Parent.query.where(Parent.id == request.form['username']).first()
    if parent is None or not utils.verify_password(request.form['password'], parent.password):
        return render_template('authentication/login.html', error="Username or password is incorrect")

    session['user'] = {
        "id": parent.id,
        "name": parent.name,
        "email": parent.email,
        "phone": parent.phone,
        "role": Parent.get_role()
    }

    children = Children.query.where(Children.parent_id == parent.id).join(Class).all()
    for idx, child in enumerate(children):
        children[idx] = child.__dict__
        children[idx].pop('_sa_instance_state', None)

    session['children'] = children
    return redirect(url_for('parent.index'))

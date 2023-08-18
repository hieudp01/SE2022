from flask import Blueprint, render_template, request, session
from sqlalchemy.orm import Session

from db_config import engine
from model.Children import Children
from model.Parent import Parent
from controller.authentication import utils

auth = Blueprint('login', __name__, url_prefix='/login')


@auth.get('/')
def parent_page():
    return render_template('authentication/login.html')


@auth.post('/add-parent')
def add_parent():
    with Session(engine) as session:
        parent = Parent()
        parent.name = request.form['name']
        parent.email = request.form['email']
        parent.phone = request.form['phone']
        parent.password = utils.hash_password(request.form['password'])
        session.add(parent)
        session.commit()
    return "ok"


@auth.post('/')
def login():
    if request.form.get("username") is None or request.form.get("password") is None:
        return render_template('authentication/login.html', error="Username or password is empty")

    children = Children.query.where(Children.id == request.form['username']).first()
    if children is None:
        return render_template('authentication/login.html', error="Children ID not found")

    parent = Parent.query.where(Parent.id == children.parent_id).first()
    if not utils.verify_password(request.form['password'], parent.password):
        return render_template('authentication/login.html', error="Username or password is incorrect")

    session["user"] = {
        "id": parent.id,
        "name": parent.name,
        "email": parent.email,
        "phone": parent.phone,
        "role": Parent.role.value
    }
    return render_template('parent/index.html')
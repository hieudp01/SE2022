from flask import Blueprint, render_template, request, session
from controller.authentication.middleware import parent_required

parent_route = Blueprint('parent', __name__, url_prefix='/parent')


@parent_route.get('/')
@parent_required
def parent_page():
    return render_template('parent/index.html')

from flask import Blueprint, render_template

from controller.authentication.middleware import parent_required

checkin = Blueprint('checkin', __name__, url_prefix='/checkin')


@checkin.get('/')
@parent_required
def parent_page():
    return render_template('checkin/parent.html', checkin_info=None)

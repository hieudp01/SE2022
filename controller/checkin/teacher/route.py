from flask import Blueprint, render_template

from controller.authentication.middleware import teacher_required

checkin = Blueprint('checkin', __name__, url_prefix='/checkin')


@checkin.get('/')
@teacher_required
def teacher_get_checkin():
    return render_template('checkin/teacher.html')


def teacher_post_checkin():
    pass

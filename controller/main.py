from flask import Blueprint, render_template

from controller.authentication.middleware import teacher_required, parent_required

parent_route = Blueprint('parent', __name__, url_prefix='/')
teacher_route = Blueprint('teacher', __name__, subdomain='teacher')


# admin_route = Blueprint('admin', __name__, subdomain='admin')


@parent_route.get('/')
@parent_required
def index():

    return render_template('index/parent.html')

@teacher_route.get('/')
@teacher_required
def index():
    return render_template('index/teacher.html')


def register_blueprint():
    register_parent_blueprint()
    register_teacher_blueprint()


def register_parent_blueprint():
    from controller.attendance.attendance_parent import attendance
    from controller.feedback.feedback_parent import feedback
    parent_route.register_blueprint(attendance)
    parent_route.register_blueprint(feedback)


def register_teacher_blueprint():
    from controller.attendance.attendance_teacher import attendance
    from controller.feedback.feedback_teacher import feedback
    teacher_route.register_blueprint(attendance)
    teacher_route.register_blueprint(feedback)


register_blueprint()

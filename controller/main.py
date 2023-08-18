from flask import Blueprint

parent_route = Blueprint('parent', __name__, url_prefix='/')
teacher_route = Blueprint('teacher', __name__, subdomain='teacher')
admin_route = Blueprint('admin', __name__, subdomain='admin')


def register_blueprint():
    register_parent_blueprint()
    register_teacher_blueprint()


def register_parent_blueprint():
    from controller.checkin.parent.route import checkin
    parent_route.register_blueprint(checkin)


def register_teacher_blueprint():
    from controller.checkin.teacher.route import checkin
    teacher_route.register_blueprint(checkin)


register_blueprint()

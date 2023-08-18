from flask import render_template

from controller.authentication.middleware import teacher_required
from controller.main import teacher_route


@teacher_route.get('/')
@teacher_required
def teacher_main():
    return render_template('index/teacher.html')

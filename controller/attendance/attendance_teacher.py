import os
from datetime import date, timedelta

from flask import Blueprint, render_template, session, request

from controller.authentication.middleware import teacher_required
from db_config import db_session
from model.Absent_request import Absent_request
from model.Attendance import Attendance
from model.Children import Children
from model.Class import Class

attendance = Blueprint('attendance', __name__, url_prefix='/attendance')


@attendance.get('/')
@teacher_required
def index():
    absent_requested_children = Children.query.join(Absent_request) \
        .where(Children.class_id == session['user']['class_id']) \
        .where(Absent_request.time >= date.today(),
               Absent_request.time < date.today() + timedelta(days=1)).all()

    attended_children = Children.query.join(Attendance) \
        .where(Attendance.time >= date.today(),
               Attendance.time < date.today() + timedelta(days=1)).all()

    if len(attended_children) != len(set(attended_children)):
        return render_template('error.html',
                               error='Database error, one child have multiple attendance check today. Please contact admin')

    children = Children.query.join(Class).where(Class.id == session['user']['class_id']).all()
    absent_children = []
    for child in children:
        if child not in attended_children and child not in absent_requested_children:
            absent_children.append(child)

    return render_template('checkin/teacher.html', absent_children=absent_children,
                           absent_requested_children=absent_requested_children,
                           attended_children=attended_children)


@attendance.get('/image/<child_id>')
@teacher_required
def image(child_id):
    if child_id not in session['children']:
        return {
            'status': 'error',
            'message': 'Invalid child id'
        }
    attendance = db_session.query(Attendance) \
        .where(Attendance.child_id == child_id,
               Attendance.time >= date.today(),
               Attendance.time < date.today() + timedelta(days=1)).one_or_none()

    if attendance is None:
        return {
            'status': 'error',
            'message': 'No attendance record found for today'
        }

    try:
        return open(f"storage/{session['user']['class_id']}/{attendance.img_name}", 'rb').read()
    except FileNotFoundError:
        return {
            'status': 'error',
            'message': 'Attendance image not found'
        }


@attendance.post('/checkin/<child_id>')
@teacher_required
def checkin(child_id):
    if child_id not in session['children']:
        return {
            'status': 'error',
            'message': 'Invalid child id'
        }

    if request.files.get('image') is None:
        return {
            'status': 'error',
            'message': 'Empty image'
        }
    # TODO: check if image is valid
    try:
        location = f"storage/{session['user']['class_id']}/{child_id}_{date.today()}.jpg"
        os.makedirs(os.path.dirname(location), exist_ok=True)
        with open(location, 'wb') as f:
            f.write(request.files['image'].read())
    except Exception as e:
        print(e)
        return {
            'status': 'error',
            'message': 'Internal Error'
        }

    attendance = Attendance(child_id=child_id, class_id=session['user']['class_id'], img_name=location)

    try:
        db_session.add(attendance)
        db_session.commit()
    except Exception as e:
        print(e)
        return {
            'status': 'error',
            'message': 'Internal Error'
        }
    return {
        'status': 'success',
        'message': 'Attendance recorded'
    }

from datetime import date, timedelta

from flask import Blueprint, render_template, session

from controller.authentication.middleware import parent_required
from model.Absent_request import Absent_request
from model.Attendance import Attendance
from model.Children import Children

from db_config import db_session
from model.Class import Class

attendance = Blueprint('attendance', __name__, url_prefix='/attendance')


@attendance.get('/')
@parent_required
def index():
    rows_attend = db_session.query(Children, Class).join(Class).join(Attendance) \
        .where(Attendance.time >= date.today(),
               Attendance.time < date.today() + timedelta(days=1)).all()

    if len(rows_attend) != len(set([row.Children.id for row in rows_attend])):
        return render_template('error.html',
                               error='Database error, one child have multiple attendance check today. Please contact teachers')

    rows_all = db_session.query(Children, Class).join(Class).all()
    rows_absent = []
    for row in rows_all:
        if row not in rows_attend:
            rows_absent.append(row)
    return render_template('checkin/parent.html', attend_children=rows_attend, absent_children=rows_absent)


@attendance.get('/image/<child_id>')
@parent_required
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

    clazz = db_session.query(Class).where(Class.id == attendance.class_id).one_or_none()
    if clazz is None:
        return {
            'status': 'error',
            'message': 'Child is not in any class'
        }

    return open(f"storage/{clazz.id}/{attendance.img_name}", 'rb').read()


@attendance.post('/request-absent/<child_id>')
@parent_required
def request_absent(child_id):
    if child_id not in session['children']:
        return {
            'status': 'error',
            'message': 'Invalid child id'
        }

    attendance = db_session.query(Attendance) \
        .where(Attendance.child_id == child_id,
               Attendance.time >= date.today(),
               Attendance.time < date.today() + timedelta(days=1)).one_or_none()

    if attendance is not None:
        return {
            'status': 'error',
            'message': 'Child already checked in today'
        }

    absent_request = db_session.query(Absent_request) \
        .where(Absent_request.child_id == child_id,
               Absent_request.time >= date.today(),
               Absent_request.time < date.today() + timedelta(days=1)).one_or_none()

    if absent_request is not None:
        return {
            'status': 'error',
            'message': 'Absent request already sent'
        }

    absent_request = Absent_request(child_id=child_id)
    try:
        db_session.add(absent_request)
        db_session.commit()
        return {
            'status': 'success',
            'message': 'Absent request sent'
        }
    except Exception as e:
        print(e)
        return {
            'status': 'error',
            'message': 'Internal error'
        }

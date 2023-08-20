from flask import Blueprint, render_template, request, session, url_for, redirect
from datetime import date, timedelta, datetime

from controller.authentication.middleware import teacher_required
from model.Attendance import Attendance
from model.Children import Children
from model.Feedback import Feedback
from model.Feedback_reply_parent import FeedbackParent
from model.Feedback_reply_teacher import FeedbackTeacher
from model.Parent import Parent
from model.Teacher import Teacher
from db_config import db_session
from controller.feedback.feedback import *

feedback = Blueprint('feedback', __name__, url_prefix='/feedback')


@feedback.get('/')
@teacher_required
def index():
    children_list = Children.query.where(Children.class_id == session['user']['class_id']).join(Attendance) \
        .where(Attendance.time >= date.today(), Attendance.time < date.today() + timedelta(days=1)).all()
    return render_template('feedback/teacher.html', children_list=children_list)


@feedback.post('/post')
@teacher_required
def post():
    # TODO: check if child already has feedback today
    child_id = request.form.get('child_id')
    feedback_content = request.form.get('feedback', '').strip()
    if child_id is None or feedback_content == '':
        return {
            "status": "error",
            "message": "Child id or feedback content is not valid"
        }

    res = Children.query.join(Attendance) \
        .filter(Children.id == child_id, Attendance.time >= date.today(),
                Attendance.time < date.today() + timedelta(days=1)).one_or_none()

    if res is None:
        return {
            "status": "error",
            "message": "Child id not found or child is not in class today"
        }

    old_feedback = Feedback.query.where(Feedback.child_id == child_id, Feedback.time >= date.today(),
                                        Feedback.time < date.today() + timedelta(days=1)).one_or_none()

    try:
        if old_feedback is None:
            feedback_post = Feedback(child_id=child_id, teacher_id=session['user']['id'], content=feedback_content)
            db_session.add(feedback_post)
        else:
            old_feedback.content = feedback_content
            old_feedback.time = datetime.now()

        db_session.commit()
        return {
            "status": "success"
        }
    except Exception as e:
        print(e)
        return {
            "status": "error",
            "message": "Something went wrong"
        }


@feedback.get('/child/<child_id>')
@teacher_required
def child(child_id):
    if child_id is None or Children.query.where(Children.class_id == session['user']['class_id']).one_or_none() is None:
        return render_template('error.html', error='Child id is not valid')

    return view_all_feedback_of_child(child_id, "teacher.feedback.detail")


@feedback.get('/detail/<feedback_id>')
@teacher_required
def detail(feedback_id):
    if feedback_id is None:
        return render_template('error.html', error='Feedback id is not valid')
    return view_one_feedback_of_child(feedback_id, session['children'])


@feedback.post('/comment/<feedback_id>')
@teacher_required
def comment(feedback_id):
    feedback_post = Feedback.query.where(Feedback.id == feedback_id).one_or_none()

    if feedback_post is None or feedback_post.child_id not in session['children']:
        return {
            "status": "error", "message": "Feedback id is not valid"
        }

    return post_comment(request.form.get('comment', ''), Role.TEACHER, feedback_id)

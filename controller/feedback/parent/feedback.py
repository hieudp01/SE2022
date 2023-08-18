from flask import Blueprint, render_template, request, session, url_for, redirect
from datetime import date

from controller.authentication.middleware import parent_required
from model.Feedback import Feedback
from model.Feedback_reply_parent import FeedbackParent
from model.Feedback_reply_teacher import FeedbackTeacher
from model.Parent import Parent
from model.Teacher import Teacher
from db_config import db_session

feedback = Blueprint('feedback', __name__, url_prefix='/feedback')


@feedback.get('/')
@parent_required
def index():
    children = session.get('children', [])
    children_list = []
    for child in children:
        latest_feedback = Feedback.query.where(Feedback.child_id == child['id']).order_by(Feedback.time).first()
        if latest_feedback is not None and latest_feedback.time.date() == date.today():
            today_feedback = latest_feedback
        else:
            today_feedback = None
        children_feedback = {
            'child': child,
            'feedback': today_feedback
        }
        children_list.append(children_feedback)
    return render_template('feedback/parent.html', children_list=children_list)


@feedback.get('/<child_id>')
@parent_required
def view(child_id):
    if child_id is None or child_id not in [child['id'] for child in session['children']]:
        return render_template('error.html', error='Child id is not valid')

    feedback_list = Feedback.query.where(Feedback.child_id == child_id).order_by(Feedback.time).all()
    return render_template('feedback/children_feedback.html', feedback_list=feedback_list)


@feedback.get('/detail/<feedback_id>')
@parent_required
def view_detail(feedback_id):
    row = db_session.query(Feedback, Teacher).where(Feedback.id == feedback_id).join(Teacher).one_or_none()
    if row is None or row.Feedback.child_id not in [child['id'] for child in session['children']]:
        return render_template('error.html', error='Feedback id is not valid')

    feedback_post = row.Feedback
    feedback_comment = db_session.query(FeedbackParent, Parent) \
        .where(FeedbackParent.feedback_id == feedback_post.id).join(Parent).all()

    feedback_comment += db_session.query(FeedbackTeacher, Teacher) \
        .where(FeedbackTeacher.feedback_id == feedback_post.id).join(Teacher).all()
    feedback_comment.sort(key=lambda x: x[0].time)
    return render_template('feedback/feedback_detail.html', feedback_post=row,
                           feedback_comment=feedback_comment)


@feedback.post('/comment/<feedback_id>')
@parent_required
def comment(feedback_id):
    feedback_post = Feedback.query.where(Feedback.id == feedback_id).one_or_none()
    if feedback_post is None or feedback_post.child_id not in [child['id'] for child in session['children']]:
        return render_template('error.html', error='Feedback id is not valid')

    content = request.form.get('comment', '')
    content = content.strip()

    if len(content) >= 500:
        return render_template('error.html', error='Comment is too long')

    if len(content) == 0:
        return render_template('error.html', error='Empty Comment')

    feedback_comment = FeedbackParent(content=content, parent_id=session['user']['id'], feedback_id=feedback_id)
    db_session.add(feedback_comment)
    db_session.commit()

    return view_detail(feedback_id)

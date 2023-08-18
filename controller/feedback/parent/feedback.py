from flask import Blueprint, render_template, request, session, url_for
from datetime import date

from controller.authentication.middleware import parent_required
from model.Feedback import Feedback
from model.Feedback_reply_parent import FeedbackParent
from model.Feedback_reply_teacher import FeedbackTeacher

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
    feedback_post = Feedback.query.get(feedback_id)
    feedback_comment = FeedbackParent.query.where(FeedbackParent.feedback_id == feedback_post.id).join(Teacher).all()
    feedback_comment += FeedbackTeacher.query.where(FeedbackTeacher.feedback_id == feedback_post.id).all()
    feedback_comment.sort(key=lambda x: x.time)
    return render_template('feedback/feedback_detail.html', feedback_post=feedback_post,
                           feedback_comment=feedback_comment)


@feedback.post('/<feedback_id>')
@parent_required
def comment(feedback_id):
    content = request.form.get('content', '')
    content = content.strip()
    if len(content) == 0:
        return {'error': 'Content is empty'}
    # feedback_comment = FeedbackParent(content=content, parent_id=session['user']['id'], feedback_id=feedback_id)

    return url_for('feedback.feedback_page', feedback_id=feedback_id)

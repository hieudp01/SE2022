from flask import Blueprint, render_template, request, session, url_for, redirect
from datetime import date, timedelta

from controller.authentication.middleware import parent_required
from controller.feedback.feedback import *
from model.Children import Children
from model.Feedback import Feedback

feedback = Blueprint('feedback', __name__, url_prefix='/feedback')


@feedback.get('/')
@parent_required
def index():
    rows = db_session.query(Children, Feedback).join(Feedback).filter(Children.parent_id == session['user']['id']) \
        .filter(Feedback.time >= date.today(),
                Feedback.time < date.today() + timedelta(days=1)).all()

    if len(rows) != len(set([row.Children.id for row in rows])):
        return render_template('error.html',
                               error='Database error, one child have multiple feedbacks today. Please contact teachers')

    return render_template('feedback/parent.html', rows=rows)


@feedback.get('/child/<child_id>')
@parent_required
def child(child_id):
    if child_id is None or child_id not in [child['id'] for child in session['children']]:
        return render_template('error.html', error='Child id is not valid')

    return view_all_feedback_of_child(child_id, "parent.feedback.detail")


@feedback.get('/detail/<feedback_id>')
@parent_required
def detail(feedback_id):
    if feedback_id is None:
        return render_template('error.html', error='Feedback id is not valid')

    return view_one_feedback_of_child(feedback_id, session['children'])


@feedback.post('/comment/<feedback_id>')
@parent_required
def comment(feedback_id):
    feedback_post = Feedback.query.where(Feedback.id == feedback_id).one_or_none()
    if feedback_post is None or feedback_post.child_id not in [child['id'] for child in session['children']]:
        return render_template('error.html', error='Feedback id is not valid')

    return post_comment(request.form.get('comment', ''), Role.PARENT, feedback_id)

from flask import render_template, session

from db_config import db_session
from model.Feedback import Feedback
from model.Feedback_reply_parent import FeedbackParent
from model.Feedback_reply_teacher import FeedbackTeacher
from model.Parent import Parent
from model.Teacher import Teacher
from model.role import Role


def view_all_feedback_of_child(child_id, feedback_url):
    feedback_list = Feedback.query.where(Feedback.child_id == child_id).order_by(Feedback.time).all()
    return render_template('feedback/children_feedback.html', feedback_url=feedback_url, feedback_list=feedback_list)


def view_one_feedback_of_child(feedback_id, allowed_children_list):
    row = db_session.query(Feedback, Teacher).where(Feedback.id == feedback_id).join(Teacher).one_or_none()
    if row is None:
        return render_template('error.html', error='Feedback id is not valid')

    if row.Feedback.child_id not in allowed_children_list:
        return render_template('error.html', error='Feedback id is not valid')

    feedback_post = row.Feedback
    feedback_comment = db_session.query(FeedbackParent, Parent) \
        .where(FeedbackParent.feedback_id == feedback_post.id).join(Parent).all()

    feedback_comment += db_session.query(FeedbackTeacher, Teacher) \
        .where(FeedbackTeacher.feedback_id == feedback_post.id).join(Teacher).all()
    feedback_comment.sort(key=lambda x: x[0].time)
    return render_template('feedback/feedback_detail.html', feedback_post=row,
                           feedback_comment=feedback_comment)


def post_comment(content, role, feedback_id):
    content = content.strip()

    if len(content) >= 500:
        return {
            "status": "error",
            "message": "Comment is too long"
        }

    if len(content) == 0:
        return {
            "status": "error",
            "message": "Comment is empty"
        }

    if role == Role.TEACHER:
        feedback_comment = FeedbackTeacher(content=content, teacher_id=session['user']['id'], feedback_id=feedback_id)
    else:
        feedback_comment = FeedbackParent(content=content, parent_id=session['user']['id'], feedback_id=feedback_id)
    try:
        db_session.add(feedback_comment)
        db_session.commit()
    except Exception as e:
        print(e)
        return {
            "status": "error",
            "message": "Something went wrong"
        }

    return {
        "status": "success"
    }

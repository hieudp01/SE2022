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

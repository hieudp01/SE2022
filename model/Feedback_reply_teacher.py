from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from model.Base import Base


class FeedbackTeacher(Base):
    __tablename__ = 'feedback_reply_teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(500), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teacher.id"), nullable=False)
    feedback_id = Column(Integer, ForeignKey("feedback.id"), nullable=False)
    time = Column(DateTime, nullable=False)

    def __init__(self, content, teacher_id, feedback_id, **kw):
        super().__init__(**kw)
        self.content = content
        self.teacher_id = teacher_id
        self.feedback_id = feedback_id
        self.time = datetime.now()

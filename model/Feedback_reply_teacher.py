from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from model.Base import Base


class Feedback_reply_teacher(Base):
    __tablename__ = 'feedback_reply_teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(500), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teacher.id") ,nullable=False)
    feedback_id = Column(Integer, ForeignKey("feedback.id"),nullable=False)
    date = Column(DateTime, nullable=False)

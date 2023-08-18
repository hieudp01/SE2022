from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from model.Base import Base


class Feedback_reply_parent(Base):
    __tablename__ = 'feedback_reply_parent'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(500), nullable=False)
    parent_id = Column(Integer, ForeignKey("parent.id") ,nullable=False)
    feedback_id = Column(Integer, ForeignKey("feedback.id"),nullable=False)
    date = Column(DateTime, nullable=False)

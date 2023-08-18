from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from model.Base import Base


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(500), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teacher.id") ,nullable=False)
    date = Column(DateTime, nullable=False)

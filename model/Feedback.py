from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from model.Base import Base


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(500), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teacher.id"), nullable=False)
    time = Column(DateTime, nullable=False)
    child_id = Column(Integer, ForeignKey("children.id"), nullable=False)

    def __init__(self, content, teacher_id, child_id, **kw):
        super().__init__(**kw)
        self.content = content
        self.teacher_id = teacher_id
        self.time = datetime.now()
        self.child_id = child_id

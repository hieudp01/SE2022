from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from model.Base import Base


class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True, autoincrement=True)
    child_id = Column(String(8), ForeignKey("children.id"), nullable=False)
    time = Column(DateTime, nullable=False)
    img_name = Column(String(50), nullable=False)

    def __init__(self, child_id, img_name, **kw):
        super().__init__(**kw)
        self.child_id = child_id
        self.time = datetime.now()
        self.img_name = img_name

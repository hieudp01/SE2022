from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from model.Base import Base


class Absent_request(Base):
    __tablename__ = 'absent_request'

    id = Column(Integer, primary_key=True, autoincrement=True)
    child_id = Column(String(8), ForeignKey("children.id"), nullable=False)
    time = Column(DateTime, nullable=False)

    def __init__(self, child_id, **kw):
        super().__init__(**kw)
        self.child_id = child_id
        self.time = datetime.now()

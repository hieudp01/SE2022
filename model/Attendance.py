from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from model.Base import Base


class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True, autoincrement=True)
    children_id = Column(String(8), ForeignKey("children.id"), nullable=False)
    time = Column(DateTime, nullable=False)
    img_name = Column(String(50), nullable=False)

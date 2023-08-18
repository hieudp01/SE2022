from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

from model.Base import Base


class Timetable(Base):
    __tablename__ = 'timetable'

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Integer, ForeignKey("class.id"), nullable = False)
    activity = Column(String(100), nullable = False)
    start_time = Column(DateTime, nullable = False)
    end_time = Column(DateTime, nullable = False)


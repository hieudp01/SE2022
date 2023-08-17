from sqlalchemy import Column, Integer, String, ForeignKey

from model.Base import Base
from model.Class import Class


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    parent_id = Column(Integer, ForeignKey("parent.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("class.id"), nullable=False)

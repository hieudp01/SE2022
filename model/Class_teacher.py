from sqlalchemy import Column, Integer, ForeignKey

from model.Base import Base


class Class_teacher(Base):
    __tablename__ = 'class_teacher'

    class_id = Column(Integer, ForeignKey("class.id"), nullable = False)
    teacher_id = Column(Integer, ForeignKey("teacher.id"), nullable = False)


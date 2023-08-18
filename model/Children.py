from sqlalchemy import Column, Integer, String, ForeignKey, Date

from model.Base import Base
from model.Class import Class


class Children(Base):
    __tablename__ = 'children'

    id = Column(String(8), primary_key=True, autoincrement=False)
    name = Column(String(100), nullable=False)
    DOB = Column(Date, nullable=False)
    parent_id = Column(Integer, ForeignKey("parent.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("class.id"), nullable=False)

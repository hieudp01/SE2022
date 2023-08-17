from sqlalchemy import Column, Integer, String

from model.Base import Base


class Class(Base):
    __tablename__ = 'class'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

from sqlalchemy import Column, Integer, String

from model.Base import Base
from model.role import Role


class Parent(Base):
    __tablename__ = 'parent'
    role = Role.PARENT

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(11), nullable=False)
    password = Column(String(20), nullable=False)

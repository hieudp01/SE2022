from sqlalchemy import Column, Integer, String

from model.Base import Base
from model.role import Role


class Parent(Base):
    __tablename__ = 'parent'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(11), nullable=False)
    password = Column(String(20), nullable=False)

    @staticmethod
    def get_role():
        return Role.PARENT.value

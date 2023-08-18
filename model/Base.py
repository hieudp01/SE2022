from sqlalchemy.orm import DeclarativeBase

from db_config import db_session


class Base(DeclarativeBase):
    query = db_session.query_property()

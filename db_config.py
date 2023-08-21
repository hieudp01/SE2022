from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

connection_string = "mysql+mysqlconnector://root:123456@localhost:3306/seedschool"
engine = create_engine(connection_string, echo=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

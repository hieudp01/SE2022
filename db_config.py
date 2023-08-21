from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from urllib.parse import quote_plus

password = quote_plus("123456aA@") 

connection_string = f"mysql+mysqlconnector://root:{password}@localhost:3306/seedschool"
engine = create_engine(connection_string, echo=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

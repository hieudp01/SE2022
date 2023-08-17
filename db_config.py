from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

connection_string = "mysql+mysqlconnector://localhost:3306/seedschool"
engine = create_engine(connection_string, echo=True)
factory = sessionmaker(bind=engine)
session = factory()

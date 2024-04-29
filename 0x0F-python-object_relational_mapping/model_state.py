# model_state.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to the MySQL server running on localhost at port 3306
    # Replace 'username', 'password', and 'database_name' with your MySQL credentials
    engine = create_engine('mysql+mysqldb://username:password@localhost:3306/database_name', pool_pre_ping=True)
    
    # WARNING: Import all classes that inherit from Base before calling Base.metadata.create_all(engine)
    Base.metadata.create_all(engine)

from sqlalchemy import Column, Integer, String, Float
from database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    cash = Column(Float)

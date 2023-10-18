from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    cash = Column(Float)

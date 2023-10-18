from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from config import Settings

settings = Settings()
print(settings.DATABASE_URL)
URL_DATABASE = settings.DATABASE_URL

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autoflush=False,autocommit=False, bind=engine)

Base = declarative_base()
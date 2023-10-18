import sys
from fastapi import FastAPI
# from dotenv import dotenv_values
from config import Settings
# imports models pydantic
from fastapi import Depends
from pydantic import BaseModel
from typing import List, Annotated, Optional
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class User(BaseModel):
    id: int | None = None
    cash: float
    # issuers: List[str] | None = []

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def hello():
    return { "message": sys.version }


@app.post("/accounts")
async def create_account(user: User, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
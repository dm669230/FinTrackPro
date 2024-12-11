from sqlalchemy import create_engine
import urllib.parse
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Request, FastAPI
from contextvars import ContextVar
from sqlalchemy.orm import sessionmaker, Session
from app.config.config import DB_NAME,DB_USER,DB_PASSWORD,SERVER_HOST,SERVER_PORT

DB_PASSWORD_PARSE = urllib.parse.quote_plus(DB_PASSWORD)
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD_PARSE}@{SERVER_HOST}:{SERVER_PORT}/{DB_NAME}"

# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# db_session : ContextVar[Session] = ContextVar('db_session')

# app = FastAPI()
#function to get the current session from the contextVar
# def get_db() -> Session:
#     return db_session.get()


BASE = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
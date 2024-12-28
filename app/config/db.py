from sqlalchemy import create_engine
import urllib.parse
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Request, FastAPI
from contextvars import ContextVar
from sqlalchemy.orm import sessionmaker, Session
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(override=True)

from app.config import config

settings = config.Settings()
# from app.config.config import DB_NAME,DB_USER,DB_PASSWORD,SERVER_HOST,SERVER_PORT

DB_PASSWORD_PARSE = urllib.parse.quote_plus(settings.DB_PASSWORD)
DATABASE_URL = f"postgresql://{settings.DB_USER}:{DB_PASSWORD_PARSE}@{settings.SERVER_HOST}:{settings.SERVER_PORT}/{settings.DB_NAME}"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BASE = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.dialects.postgresql import VARCHAR, FLOAT, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from decouple import config

DB_USER = config('POSTGRES_USER', default='postgres')
DB_PASSWORD = config('POSTGRES_PASSWORD', default='postgres')
DB_NAME = config('POSTGRES_DB', default='FIAP')
DB_HOST = config('POSTGRES_HOST', default='gestao-postgresql')

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL)

def init_db():
    Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

DB_USER = config('DB_USER', default='postgres')
DB_PASSWORD = config('DB_PASSWORD', default='postgres')
DB_HOST = config('DB_HOST', default='localhost')
DB_NAME = config('DB_NAME', default='FIAP')

Base = declarative_base()
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sync_session = sessionmaker(bind=engine)

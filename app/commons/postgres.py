from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


Base = declarative_base()
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}/{config('DB_NAME')}"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sync_session = sessionmaker(bind=engine)

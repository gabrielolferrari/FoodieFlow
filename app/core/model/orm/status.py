from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from infrastructure.database import Base

class Status(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)

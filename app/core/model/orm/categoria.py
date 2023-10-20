from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER
from sqlalchemy.ext.declarative import declarative_base

from infrastructure.database import Base

class Categoria(Base):
    __tablename__ = "categoria"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)

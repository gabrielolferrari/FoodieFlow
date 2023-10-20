from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER
from sqlalchemy.ext.declarative import declarative_base

from infrastructure.database import Base

class Categoria(Base):
    __tablename__ = "categoria"

    id = Column(INTEGER, primary_key=True, index=True)
    nome = Column(VARCHAR(255))
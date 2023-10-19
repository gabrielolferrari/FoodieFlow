from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER
from sqlalchemy.ext.declarative import declarative_base

from infrastructure.dataprovider.database import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(INTEGER, primary_key=True, index=True)
    cpf = Column(VARCHAR(11), unique=True, index=True, nullable=False)
    nome = Column(VARCHAR(255))
    email = Column(VARCHAR(255))
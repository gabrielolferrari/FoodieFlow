from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from infrastructure.dataprovider.database import Base

class Imagem(Base):
    __tablename__ = "imagem"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    caminho = Column(String, nullable=False)
    id_produto = Column(Integer, ForeignKey('produto.id'), nullable=False)
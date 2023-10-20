from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from infrastructure.dataprovider.database import Base
from core.model.orm.ingrediente import produto_ingrediente

class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(DECIMAL, nullable=False)
    id_categoria = Column(Integer, ForeignKey('categoria.id'), nullable=False)

    # Relacionamentos
    categoria = relationship("Categoria", backref="produtos")
    ingredientes = relationship("Ingrediente", secondary=produto_ingrediente, backref="produtos")
    imagens = relationship("Imagem", backref="produto")
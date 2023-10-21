from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from infrastructure.database import Base
from core.model.orm.cliente import Cliente
from core.model.orm.produto import Produto

# Tabela associativa para o relacionamento entre Pedido e Produto
pedido_produto = Table(
    'pedido_produto', Base.metadata,
    Column('id_pedido', Integer, ForeignKey('pedido.id')),
    Column('id_produto', Integer, ForeignKey('produto.id'))
)

class Pedido(Base):
    __tablename__ = "pedido"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo = Column(String, unique=True, nullable=False)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    id_status = Column(Integer, ForeignKey('status.id'), nullable=False)
    
    # Relacionamentos
    cliente = relationship("Cliente", backref="pedidos")
    status = relationship("Status", backref="pedidos")
    produtos = relationship("Produto", secondary=pedido_produto, backref="pedidos")

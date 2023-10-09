from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR, FLOAT, INTEGER

from commons.postgres import Base


class Product(Base):
    __tablename__ = 'produto'
    __table_args__ = {'schema': 'FIAP'}
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    price = Column(FLOAT)
    img = Column(VARCHAR(255))
    description = Column(VARCHAR(255))

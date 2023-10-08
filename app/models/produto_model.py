from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, VARCHAR, FLOAT

from commons.postgres import Base


class Product(Base):
    __tablename__ = 'produto'
    __table_args__ = {'schema': 'FIAP'}
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(VARCHAR(255))
    price = Column(FLOAT)

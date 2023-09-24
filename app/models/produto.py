from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, VARCHAR, FLOAT
from sqlalchemy.orm import relationship

from app.commons.postgres import Base


class produto(Base):
    __tablename__ = 'produto'
    __table_args__ = {'schema': 'FIAP'}
    id = Column(UUID(as_uuid=True), primary_key=True)
    created_at = Column(TIMESTAMP)
    nome = Column(VARCHAR(255))
    preco = Column(FLOAT)

    # Define the foreign key relationship

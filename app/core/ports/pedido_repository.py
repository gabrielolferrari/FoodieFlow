from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from core.model.pedido import Pedido as PedidoModel

class PedidoRepository(ABC):
    
    @abstractmethod
    def create_pedido(self, db: Session, pedido: PedidoModel):
        pass

    @abstractmethod
    def get_pedidos(self, db: Session, skip: int = 0, limit: int = 100):
        pass
    
    @abstractmethod
    def get_pedidos_by_status(self, db: Session, status: int, skip: int = 0, limit: int = 100):
        pass

    @abstractmethod
    def atualizar_status_para_preparacao(self, db: Session, pedido_id: int):
        pass

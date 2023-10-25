from sqlalchemy.orm import Session
from core.ports.pedido_repository import PedidoRepository
from core.model.pedido import Pedido as PedidoModel

class PedidoServiceImpl:
    def __init__(self, pedido_repository: PedidoRepository):
        self.pedido_repository = pedido_repository

    def create_pedido(self, db: Session, pedido: PedidoModel):
        return self.pedido_repository.create_pedido(db, pedido)
    
    def get_pedidos(self, db: Session, skip: int = 0, limit: int = 100):
        return self.pedido_repository.get_pedidos(db, skip, limit)
    
    def get_pedidos_by_status(self, db: Session, status: int, skip: int = 0, limit: int = 100):
        return self.pedido_repository.get_pedidos_by_status(db, status, skip, limit)
    
    def atualizar_status_para_preparacao(self, db: Session, pedido_id: int):
        return self.pedido_repository.atualizar_status_para_preparacao(db, pedido_id)

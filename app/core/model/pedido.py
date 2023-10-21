from typing import List, Optional
from pydantic import BaseModel
from core.model.cliente import Cliente
from core.model.produto import Produto
from core.model.status import Status

class PedidoBase(BaseModel):
    codigo: str
    id_cliente: int
    id_status: int
    produtos: List[int]

class Pedido(PedidoBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

class PedidoCompleto(Pedido):
    cliente: Cliente
    status: Status
    produtos: List[Produto]

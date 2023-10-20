from typing import List, Optional
from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    id_categoria: int

class Produto(ProdutoBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

class ProdutoIn(ProdutoBase):
    ingredientes: List[int] = []

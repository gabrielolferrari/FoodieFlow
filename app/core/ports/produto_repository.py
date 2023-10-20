from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from core.model.produto import Produto as ProdutoModel

class ProdutoRepository(ABC):
    
    @abstractmethod
    def create_produto(self, db: Session, produto: ProdutoModel):
        pass

    @abstractmethod
    def get_produto(self, db: Session, produto_id: int):
        pass

    @abstractmethod
    def get_produtos(self, db: Session, skip: int = 0, limit: int = 100):
        pass

    @abstractmethod
    def update_produto(self, db: Session, produto_id: int, updated_produto: ProdutoModel):
        pass

    @abstractmethod
    def delete_produto(self, db: Session, produto_id: int):
        pass

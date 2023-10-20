from sqlalchemy.orm import Session
from core.ports.produto_repository import ProdutoRepository
from core.model.produto import Produto as ProdutoModel

class ProdutoServiceImpl:
    def __init__(self, produto_repository: ProdutoRepository):
        self.produto_repository = produto_repository

    def create_produto(self, db: Session, produto: ProdutoModel):
        return self.produto_repository.create_produto(db, produto)
    
    def get_produto(self, db: Session, produto_id: int):
        return self.produto_repository.get_produto(db, produto_id)

    def get_produtos(self, db: Session, skip: int = 0, limit: int = 100):
        return self.produto_repository.get_produtos(db, skip, limit)
    
    def update_produto(self, db: Session, produto_id: int, updated_produto: ProdutoModel):
        return self.produto_repository.update_produto(db, produto_id, updated_produto)
    
    def delete_produto(self, db: Session, produto_id: int):
        return self.produto_repository.delete_produto(db, produto_id)

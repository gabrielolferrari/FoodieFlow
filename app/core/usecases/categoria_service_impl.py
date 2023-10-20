from sqlalchemy.orm import Session
from core.ports.categoria_repository import CategoriaRepository
from core.model.categoria import Categoria as CategoriaModel

class CategoriaServiceImpl:
    def __init__(self, categoria_repository: CategoriaRepository):
        self.categoria_repository = categoria_repository

    def create_categoria(self, db: Session, categoria: CategoriaModel):
        categoria_db = self.categoria_repository.get_categoria_by_nome(db, categoria.nome)
        if categoria_db:
            raise Exception("Categoria já cadastrada")
        return self.categoria_repository.create_categoria(db, categoria)
    
    def get_categoria(self, db: Session, categoria_id: int):
        return self.categoria_repository.get_categoria(db, categoria_id)

    def get_categorias(self, db: Session, skip: int = 0, limit: int = 100):
        return self.categoria_repository.get_categorias(db, skip, limit)
    
    def update_categoria(self, db: Session, categoria_id: int, updated_categoria: CategoriaModel):
        return self.categoria_repository.update_categoria(db, categoria_id, updated_categoria)
    
    def delete_categoria(self, db: Session, categoria_id: int):
        return self.categoria_repository.delete_categoria(db, categoria_id)
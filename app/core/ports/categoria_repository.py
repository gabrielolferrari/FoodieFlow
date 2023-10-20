from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from core.model.categoria import Categoria as CategoriaModel

class CategoriaRepository(ABC):
    @abstractmethod
    def create_categoria(self, db: Session, categoria: CategoriaModel):
        pass
    
    @abstractmethod
    def get_categoria(self, db: Session, categoria_id: int):
        pass

    @abstractmethod
    def get_categorias(self, db: Session, skip: int = 0, limit: int = 100):
        pass
    
    @abstractmethod
    def get_categoria_by_nome(self, db: Session, nome: str):
        pass

    @abstractmethod
    def update_categoria(self, db: Session, categoria_id: int, updated_categoria: CategoriaModel):
        pass
    
    @abstractmethod
    def delete_categoria(self, db: Session, categoria_id: int):
        pass